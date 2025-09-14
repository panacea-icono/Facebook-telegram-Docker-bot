"""
Tests para Facebook Messenger Bot
Desarrollado por Panacea Icono S.A.
"""

import pytest
import json
from unittest.mock import patch, MagicMock
from app import app, process_text_message, create_welcome_quick_replies

class TestFacebookMessengerBot:
    """Tests para la funcionalidad del bot"""
    
    def setup_method(self):
        """Configuración inicial para cada test"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_health_check(self):
        """Test del endpoint de salud"""
        response = self.app.get('/health')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert 'timestamp' in data
        assert data['service'] == 'facebook-messenger-bot'
    
    def test_home_endpoint(self):
        """Test del endpoint principal"""
        response = self.app.get('/')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'message' in data
        assert 'version' in data
        assert 'endpoints' in data
    
    def test_webhook_verification_success(self):
        """Test de verificación exitosa del webhook"""
        with patch.dict('os.environ', {'FB_VERIFY_TOKEN': 'test_token'}):
            response = self.app.get('/webhook?hub.mode=subscribe&hub.verify_token=test_token&hub.challenge=test_challenge')
            assert response.status_code == 200
            assert response.data.decode() == 'test_challenge'
    
    def test_webhook_verification_failure(self):
        """Test de verificación fallida del webhook"""
        response = self.app.get('/webhook?hub.mode=subscribe&hub.verify_token=wrong_token&hub.challenge=test_challenge')
        assert response.status_code == 403
    
    def test_process_text_message_greetings(self):
        """Test de procesamiento de saludos"""
        greetings = ['hola', 'hi', 'hello', 'buenos días', 'buenas tardes', 'buenas noches']
        
        for greeting in greetings:
            response = process_text_message('test_user', greeting)
            assert 'Hola' in response
            assert 'Panacea Icono' in response
    
    def test_process_text_message_help(self):
        """Test de comando de ayuda"""
        help_commands = ['ayuda', 'help', 'comandos']
        
        for cmd in help_commands:
            response = process_text_message('test_user', cmd)
            assert 'Comandos disponibles' in response
            assert 'info' in response
            assert 'servicios' in response
    
    def test_process_text_message_info(self):
        """Test de comando de información"""
        response = process_text_message('test_user', 'info')
        assert 'Panacea Icono S.A.' in response
        assert 'blockchain' in response
        assert 'Web3' in response
    
    def test_process_text_message_services(self):
        """Test de comando de servicios"""
        response = process_text_message('test_user', 'servicios')
        assert 'PanasToken' in response
        assert 'PanasPay' in response
        assert 'PanasShop' in response
    
    def test_process_text_message_contact(self):
        """Test de comando de contacto"""
        response = process_text_message('test_user', 'contacto')
        assert 'panacea-icono.com' in response
        assert 'info@panacea-icono.com' in response
    
    def test_process_text_message_menu(self):
        """Test de comando de menú"""
        response = process_text_message('test_user', 'menu')
        assert 'Menú Principal' in response
        assert 'Selecciona una opción' in response
    
    def test_process_text_message_unknown(self):
        """Test de mensaje desconocido"""
        response = process_text_message('test_user', 'mensaje desconocido')
        assert 'Entiendo que dices' in response
        assert 'ayuda' in response
    
    def test_create_welcome_quick_replies(self):
        """Test de creación de botones de respuesta rápida"""
        quick_replies = create_welcome_quick_replies()
        
        assert len(quick_replies) == 4
        assert all(reply['content_type'] == 'text' for reply in quick_replies)
        
        # Verificar que contienen los botones esperados
        titles = [reply['title'] for reply in quick_replies]
        assert 'ℹ️ Información' in titles
        assert '💼 Servicios' in titles
        assert '📞 Contacto' in titles
        assert '🤖 Ayuda' in titles
    
    @patch('app.bot')
    def test_webhook_message_processing(self, mock_bot):
        """Test de procesamiento de mensajes en webhook"""
        mock_bot.send_text_message.return_value = {'success': True}
        
        # Simular mensaje de Facebook
        message_data = {
            "entry": [{
                "messaging": [{
                    "sender": {"id": "test_user"},
                    "message": {"text": "hola"}
                }]
            }]
        }
        
        response = self.app.post('/webhook', 
                               data=json.dumps(message_data),
                               content_type='application/json')
        
        assert response.status_code == 200
        mock_bot.send_text_message.assert_called_once()
    
    @patch('app.bot')
    def test_webhook_postback_processing(self, mock_bot):
        """Test de procesamiento de postbacks en webhook"""
        mock_bot.send_text_message.return_value = {'success': True}
        
        # Simular postback de Facebook
        postback_data = {
            "entry": [{
                "messaging": [{
                    "sender": {"id": "test_user"},
                    "postback": {"payload": "INFO"}
                }]
            }]
        }
        
        response = self.app.post('/webhook', 
                               data=json.dumps(postback_data),
                               content_type='application/json')
        
        assert response.status_code == 200
        mock_bot.send_text_message.assert_called_once()
    
    def test_webhook_invalid_json(self):
        """Test de webhook con JSON inválido"""
        response = self.app.post('/webhook', 
                               data="invalid json",
                               content_type='application/json')
        
        assert response.status_code == 200  # El bot maneja errores graciosamente
    
    def test_webhook_empty_message(self):
        """Test de webhook con mensaje vacío"""
        response = self.app.post('/webhook', 
                               data=json.dumps({}),
                               content_type='application/json')
        
        assert response.status_code == 200

if __name__ == '__main__':
    pytest.main([__file__])
