import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Реквизиты для работы с google-таблицей
CREDENTIALS = {
    'type': 'service_account',
    'project_id': 'dankadimkafilms',
    'private_key_id': os.environ.get('PRIVATE_KEY_ID'),
    'private_key': os.environ.get('PRIVATE_KEY').replace('\\n', '\n'),
    'client_email': 'filmbot-551@dankadimkafilms.iam.gserviceaccount.com',
    'client_id': '114018269873706955026',
    'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
    'token_uri': 'https://oauth2.googleapis.com/token',
    'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
    'client_x509_cert_url': 'https://www.googleapis.com/robot/v1/metadata/x509/filmbot-551%40dankadimkafilms.iam.gserviceaccount.com'
}

INSULTS = ['Пидр', 'Хуй', 'Гандон', 'Сука', 'Блядь', 'Казёл', 'Мразь']