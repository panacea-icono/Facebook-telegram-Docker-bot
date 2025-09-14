from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionShowServicesCarousel(Action):
    """Custom action para mostrar carousel de servicios"""

    def name(self) -> Text:
        return "action_show_services_carousel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Detectar el canal de comunicación
        channel = tracker.get_latest_input_channel()
        
        if channel == "facebook":
            # Carousel específico para Facebook Messenger
            message = {
                "text": "Estos son nuestros servicios disponibles:",
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "Consultoría Digital",
                                "subtitle": "Transformación digital para tu negocio",
                                "image_url": "https://via.placeholder.com/300x200?text=Consultoria",
                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": "Más información",
                                        "payload": "/ask_consulting"
                                    },
                                    {
                                        "type": "web_url",
                                        "url": "https://ejemplo.com/consultoria",
                                        "title": "Ver detalles"
                                    }
                                ]
                            },
                            {
                                "title": "Desarrollo Web",
                                "subtitle": "Sitios web modernos y responsivos",
                                "image_url": "https://via.placeholder.com/300x200?text=Web+Dev",
                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": "Más información",
                                        "payload": "/ask_webdev"
                                    },
                                    {
                                        "type": "web_url",
                                        "url": "https://ejemplo.com/webdev",
                                        "title": "Ver portfolio"
                                    }
                                ]
                            },
                            {
                                "title": "Marketing Digital",
                                "subtitle": "Estrategias efectivas para tu marca",
                                "image_url": "https://via.placeholder.com/300x200?text=Marketing",
                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": "Más información",
                                        "payload": "/ask_marketing"
                                    },
                                    {
                                        "type": "web_url",
                                        "url": "https://ejemplo.com/marketing",
                                        "title": "Ver casos"
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
            dispatcher.utter_message(json_message=message)
            
        elif channel == "telegram":
            # Keyboard inline específico para Telegram
            message = {
                "text": "🔧 **Nuestros Servicios Disponibles** 🔧\n\nElige el servicio que te interese:",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "🔧 Consultoría Digital",
                                "callback_data": "/ask_consulting"
                            },
                            {
                                "text": "💻 Desarrollo Web",
                                "callback_data": "/ask_webdev"
                            }
                        ],
                        [
                            {
                                "text": "📱 Marketing Digital",
                                "callback_data": "/ask_marketing"
                            },
                            {
                                "text": "ℹ️ Más información",
                                "url": "https://ejemplo.com"
                            }
                        ]
                    ]
                }
            }
            dispatcher.utter_message(json_message=message)
        else:
            # Fallback para otros canales
            dispatcher.utter_message(template="utter_services_carousel")

        return []


class ActionShowProductsCarousel(Action):
    """Custom action para mostrar carousel de productos"""

    def name(self) -> Text:
        return "action_show_products_carousel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        channel = tracker.get_latest_input_channel()
        
        if channel == "facebook":
            message = {
                "text": "Conoce nuestros productos:",
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "Plan Premium",
                                "subtitle": "Todo incluido para empresas grandes - $99/mes",
                                "image_url": "https://via.placeholder.com/300x200?text=Premium",
                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": "Elegir Premium",
                                        "payload": "/select_premium"
                                    },
                                    {
                                        "type": "web_url",
                                        "url": "https://ejemplo.com/premium",
                                        "title": "Ver detalles"
                                    }
                                ]
                            },
                            {
                                "title": "Plan Standard",
                                "subtitle": "Perfecto para medianas empresas - $49/mes",
                                "image_url": "https://via.placeholder.com/300x200?text=Standard",
                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": "Elegir Standard",
                                        "payload": "/select_standard"
                                    },
                                    {
                                        "type": "web_url",
                                        "url": "https://ejemplo.com/standard",
                                        "title": "Ver detalles"
                                    }
                                ]
                            },
                            {
                                "title": "Plan Básico",
                                "subtitle": "Ideal para emprendedores - $19/mes",
                                "image_url": "https://via.placeholder.com/300x200?text=Basic",
                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": "Elegir Básico",
                                        "payload": "/select_basic"
                                    },
                                    {
                                        "type": "web_url",
                                        "url": "https://ejemplo.com/basic",
                                        "title": "Ver detalles"
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
            dispatcher.utter_message(json_message=message)
            
        elif channel == "telegram":
            message = {
                "text": "💼 **Nuestros Planes Disponibles** 💼\n\n¿Cuál se adapta mejor a tu negocio?",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "⭐ Premium - $99/mes",
                                "callback_data": "/select_premium"
                            },
                            {
                                "text": "🔸 Standard - $49/mes",
                                "callback_data": "/select_standard"
                            }
                        ],
                        [
                            {
                                "text": "📦 Básico - $19/mes",
                                "callback_data": "/select_basic"
                            },
                            {
                                "text": "📋 Comparar planes",
                                "url": "https://ejemplo.com/planes"
                            }
                        ]
                    ]
                }
            }
            dispatcher.utter_message(json_message=message)
        else:
            dispatcher.utter_message(template="utter_products_carousel")

        return []


class ActionShowHelpOptions(Action):
    """Custom action para mostrar opciones de ayuda"""

    def name(self) -> Text:
        return "action_show_help_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        channel = tracker.get_latest_input_channel()
        
        if channel == "facebook":
            message = {
                "text": "¿Cómo puedo ayudarte?",
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "Documentación",
                                "subtitle": "Guías y tutoriales completos",
                                "image_url": "https://via.placeholder.com/300x200?text=Docs",
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://docs.ejemplo.com",
                                        "title": "Ver documentación"
                                    }
                                ]
                            },
                            {
                                "title": "Soporte Técnico",
                                "subtitle": "Contacta con nuestro equipo",
                                "image_url": "https://via.placeholder.com/300x200?text=Support",
                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": "Crear ticket",
                                        "payload": "/create_ticket"
                                    }
                                ]
                            },
                            {
                                "title": "FAQ",
                                "subtitle": "Preguntas frecuentes",
                                "image_url": "https://via.placeholder.com/300x200?text=FAQ",
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://ejemplo.com/faq",
                                        "title": "Ver FAQ"
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
            dispatcher.utter_message(json_message=message)
            
        elif channel == "telegram":
            message = {
                "text": "🆘 **Opciones de Ayuda** 🆘\n\n¿Qué tipo de ayuda necesitas?",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "📚 Documentación",
                                "url": "https://docs.ejemplo.com"
                            },
                            {
                                "text": "🎫 Soporte Técnico",
                                "callback_data": "/create_ticket"
                            }
                        ],
                        [
                            {
                                "text": "❓ FAQ",
                                "url": "https://ejemplo.com/faq"
                            }
                        ]
                    ]
                }
            }
            dispatcher.utter_message(json_message=message)
        else:
            dispatcher.utter_message(template="utter_help_carousel")

        return []