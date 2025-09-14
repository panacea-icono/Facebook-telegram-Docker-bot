"""
Configuración completa del Facebook Messenger Bot
Desarrollado por Panacea Icono S.A.
"""

import os
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class TelegramBot:
    """Configuración de bot de Telegram"""
    name: str
    username: str
    token: str
    function: str
    active: bool = True

@dataclass
class HerokuApp:
    """Configuración de aplicación Heroku"""
    name: str
    url: str
    account: str
    description: str

@dataclass
class APIConfig:
    """Configuración de APIs externas"""
    name: str
    api_key: str
    base_url: str
    active: bool = True

class Config:
    """Configuración principal de la aplicación"""
    
    # Configuración básica
    SECRET_KEY = os.getenv('SECRET_KEY', 'panacea_icono_facebook_bot_2025_secure_key')
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    
    # Puerto y host
    PORT = int(os.getenv('PORT', 8080))
    HOST = os.getenv('HOST', '0.0.0.0')
    
    # Facebook Messenger
    FB_VERIFY_TOKEN = os.getenv('FB_VERIFY_TOKEN', 'pon-un-token-unico-para-verificar')
    FB_PAGE_TOKEN = os.getenv('FB_PAGE_TOKEN', '')
    FB_APP_ID = os.getenv('FB_APP_ID', '1189548453208656')
    FB_APP_SECRET = os.getenv('FB_APP_SECRET', 'c502aca293c21bbd7c68a3af77c4f9fa')
    FB_API_VERSION = os.getenv('FB_API_VERSION', 'v20.0')
    FB_WEBSITE_URL = os.getenv('FB_WEBSITE_URL', 'https://kuchiuyas.com')
    
    # Telegram Bots (30+ bots activos)
    TELEGRAM_BOTS = [
        TelegramBot("ALINA", "ALINA_KUCHITV_BOT", "7736162376:AAFY-oLaHuOd3VEUlPa1fJjAnCLeow1APto", "Te lleva al mundial"),
        TelegramBot("Anastasia", "Anastasia_panacea_bot", "8113198067:AAEevfvj5k_aAzr-4fbgjxpGbpzq_PCT-Uk", "Panacea bot"),
        TelegramBot("CONDE_MORMIX", "CONDE_MORMIX_bot", "7958735108:AAEnPCdiF3_NsfgAO1ZQJK-pVVv-OzgT31k", "Mormix bot"),
        TelegramBot("Dr_Lalo", "Dr_Lalo_bot", "8144751411:AAGGRYXb9As8Kd1tJEMaVQ5qWjWfJm1WdIo", "Dr. Lalo bot"),
        TelegramBot("Panas", "Panas_token_bot", "7828486767:AAHQQ98T2orrJfDOJEyZ1_8HSvSuJ08bJzA", "PanasToken bot"),
        TelegramBot("Poci", "Pontificia_bot", "7813930559:AAEguGKbO3WlWlt1BenLkBrmATpuCUtfxZw", "Pontificia bot"),
        TelegramBot("DrAquiles", "DRAQUILES_bot", "7552009866:AAEPQrwbA4BJ6BgFkzNhUzIiz7BRLh4deuM", "Dr. Aquiles bot"),
        TelegramBot("la_chunchuna", "la_chunchuna_bot", "7584900206:AAFvBWakpuvo7kLxUcFnbzkpCTDj5GEhlb0", "KuchiTV Mundial"),
        TelegramBot("plastic_surgeon", "vaser_plastic_surgeon_bot", "7735301496:AAFhWecy29jjPIP-QLwMBHyt7W-b8MTOhX4", "Cirugía plástica"),
        TelegramBot("IVANA", "IVANA_TV_BOT", "7226803911:AAEBZa5DN7ppTGqL8WuicvH1Zpucoj0ju18", "KuchiTV"),
        TelegramBot("Catolica", "Catolica_boliviana_bot", "7837429936:AAHAiTyZncM3V7ysqwo7Fs0NVl2nOi-iE4g", "Católica boliviana"),
        TelegramBot("DR_DELA_TV", "dR_tv_BOT", "8151444219:AAHe28kkVynPKUn3o75jSVBUMUdAMoLNFHQ", "Dr. TV"),
        TelegramBot("Jabancho", "Jabancho_bot", "7715564591:AAGjqzaIQiR4JVov9ipJtnvdGB5TOzcysH4", "KuchiTV Mundial"),
        TelegramBot("monica", "monica_vaser_bot", "7164860773:AAFw0lpdE0-mby5IMQnoZFRb74giZ4zr3r0", "Monica Vaser"),
        TelegramBot("Alejandra", "Alejandra_MD_bot", "7461930898:AAHZjFntuq0IE4mIUKE3kOF7H87AJk8lYns", "Alejandra MD"),
        TelegramBot("sophie", "Sophie_DrTV_bot", "8046291328:AAFfYZ4JexrnNsqkgrGoLUHs11T1IGLoWJ8", "Sophie DrTV"),
        TelegramBot("SOCIEDAD", "Sociedad_bot", "7653405457:AAH2-RqwWOr4z0FSb7ua2B0uWfFKcfK3ox4", "Sociedad bot"),
        TelegramBot("Kuchiuya", "Kuchiuya_bot", "7630335998:AAGhGk25gfHWCxceMKGVly43WH7-W0ufC88", "Kuchiuya bot"),
        TelegramBot("Vaser_token", "CLINICA_VASER_BOT", "7622504424:AAGQjIbXs3fs9ITUiDFBuzNG5PmJHb4Sxao", "Clínica Vaser"),
        TelegramBot("dr_tapia_bot", "dr_tapia_bot", "8077214672:AAGn7tU3kcC1fMAFmA6HSQTZSCBG-3i9XPE", "Dr. Tapia bot"),
        TelegramBot("Lalo", "Lalabot007_bot", "7587868575:AAHLc_SlrzTae3Ae6u-pgMvScFSpuzmW4yM", "Lalo bot"),
        TelegramBot("Guerita", "La_guerita_bot", "7267919371:AAFLVcOeoffuTAv2S0_Dlq13L1LSNmwTAWk", "La Guerita bot"),
        TelegramBot("Joselin", "Joselin_2025_bot", "7892244472:AAFeXHfXwHJuVRg2tKs-V2xMS8JihKOaIv4", "Joselin 2025"),
        TelegramBot("carlos", "Liposuccion_bot", "8187502572:AAFn2bEOOqDipeDWTnszjyWyiBUUBsofMis", "Liposucción"),
        TelegramBot("ana_maria", "face_surgery_bot", "7835937499:AAHahj4IAghOuWRmeusvIw7RhZGWN9G23yg", "Cirugía facial"),
        TelegramBot("Ingenio", "Universidad_bot", "8187502572:AAFn2bEOOqDipeDWTnszjyWyiBUUBsofMis", "Universidad"),
        TelegramBot("Catalina", "Universidad_Catolica_bot", "7523398376:AAGhS6je5tlg0CKMW6rMGwwaBSJiJm5bpY0", "Universidad Católica"),
        TelegramBot("Analia", "Boliviana_bot", "7155901429:AAFTyNZ2VQlufM8gR-TQCiMPD1rsE1qqOAE", "Boliviana bot"),
        TelegramBot("Dra_Liliana", "Dra_Liliana_bot", "7934673190:AAFMO27pg1uYyE3jor1x6O2iGSCb7RDhKWY", "Dra. Liliana"),
    ]
    
    # Aplicaciones Heroku
    HEROKU_APPS = [
        HerokuApp("fibonacci", "https://fibonacci-b33f2f33a8ad.herokuapp.com", "personal", "Sistema Fibonacci"),
        HerokuApp("kuchiuyas-algorand", "https://kuchiuyas-algorand-d0bd2e62d823.herokuapp.com", "personal", "Kuchiuyas Algorand"),
        HerokuApp("backend-developer", "https://backend-developer-d160b40c29bc.herokuapp.com", "personal", "Backend Developer"),
        HerokuApp("api-panacea", "https://api-panacea-638dc550fab6.herokuapp.com", "personal", "API Panacea"),
        HerokuApp("ton-orquestador", "https://ton-telegram-orquestador-185e533131f8.herokuapp.com", "empresa", "TON Orquestador"),
        HerokuApp("kuchiuyas", "https://kuchiuyas-72a39bde11fc.herokuapp.com", "empresa", "Kuchiuyas"),
    ]
    
    # APIs externas
    APIS = [
        APIConfig("OpenAI_Kuchiuyas", os.getenv('OPENAI_KUCHIUYAS', ''), "https://api.openai.com/v1"),
        APIConfig("OpenAI_Fibonacci", os.getenv('OPENAI_FIBONACCI', ''), "https://api.openai.com/v1"),
        APIConfig("OpenAI_Ollama", os.getenv('OPENAI_OLLAMA', ''), "https://api.openai.com/v1"),
        APIConfig("HuggingFace", os.getenv('HUGGINGFACE_TOKEN', ''), "https://huggingface.co/api"),
        APIConfig("Google_API_1", os.getenv('GOOGLE_API_KEY_1', ''), "https://maps.googleapis.com/maps/api"),
        APIConfig("Google_API_2", os.getenv('GOOGLE_API_KEY_2', ''), "https://maps.googleapis.com/maps/api"),
        APIConfig("Shopify_1", os.getenv('SHOPIFY_TOKEN_1', ''), "https://repositorios-panaca.myshopify.com/admin/api/2024-01"),
        APIConfig("Shopify_2", os.getenv('SHOPIFY_TOKEN_2', ''), "https://repositorios-panaca.myshopify.com/admin/api/2024-01"),
    ]
    
    # Vercel
    VERCEL_TEAM = "panacea-icono"
    VERCEL_PROJECT_ID = "prj_8V2CEf88FXnIGzRNW88nnXe6dDAU"
    VERCEL_API_KEY = os.getenv('VERCEL_API_KEY', '')
    VERCEL_WEBHOOK = os.getenv('VERCEL_WEBHOOK', '')
    
    # GitHub
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')
    GITHUB_CLASSIC_TOKEN = os.getenv('GITHUB_CLASSIC_TOKEN', '')
    
    # Docker
    DOCKER_TOKEN = os.getenv('DOCKER_TOKEN', '')
    
    # Base de datos
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot.db')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    
    # URLs importantes
    MUNDIAL_URL = "https://vamos-al-mundial.karapanza.in/"
    DR_TAPIA_URL = "https://drtapiavargas.com"
    KUCHIUYAS_URL = "https://kuchiuyas.com"
    TOKEN_ACCESS_URL = "https://token.drtapiavargas.com/"
    
    # Contactos
    EMAIL_PRINCIPAL = "info@drtapiavargas.com"
    EMAIL_PANACEA = "repositorios.panacea@gmail.com"
    PHONE = "69674560"
    
    # Wallets y Blockchain
    ALGORAND_KEYS = [
        "WRX3S7MAMB7LGXCXBX5NHU2D55XCITEGYLSH3WH6HLA727K746HLS4SD64",
        "KNXUWV5UA6MU73UFZ3KGPDSYJ6D2BL5DGDJIANBOEQKTCEMUGVGK62SEUQ"
    ]
    
    ETHEREUM_ADDRESSES = [
        "0x21b227d8085b4522805b6a6dc838e1a8206baa91",
        "0x21b227d8085B4522805b6A6Dc838e1A8206bAa91"
    ]
    
    TON_WALLET = "UQDtP1eHpaelnNpljGZNBee2BlhMVXZDW_Zk5t1zxqsdsBSZ"
    
    # Telegram Wallet
    TELEGRAM_WALLET_ID = "104233824699580798071"
    CIVIL_AI_KEY = "6cff344b3d6a1257e11dede1133a32c4"
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    @classmethod
    def get_telegram_bot_by_username(cls, username: str) -> Optional[TelegramBot]:
        """Obtiene un bot de Telegram por username"""
        for bot in cls.TELEGRAM_BOTS:
            if bot.username == username:
                return bot
        return None
    
    @classmethod
    def get_active_telegram_bots(cls) -> List[TelegramBot]:
        """Obtiene todos los bots de Telegram activos"""
        return [bot for bot in cls.TELEGRAM_BOTS if bot.active]
    
    @classmethod
    def get_heroku_apps_by_account(cls, account: str) -> List[HerokuApp]:
        """Obtiene aplicaciones Heroku por cuenta"""
        return [app for app in cls.HEROKU_APPS if app.account == account]
    
    @classmethod
    def get_active_apis(cls) -> List[APIConfig]:
        """Obtiene todas las APIs activas"""
        return [api for api in cls.APIS if api.active and api.api_key]
