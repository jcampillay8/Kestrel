import os
import django

# Establecer el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Configurar Django
django.setup()

from django.core.mail import EmailMultiAlternatives, get_connection
from django.conf import settings

# Configura una conexión personalizada con un tiempo límite
connection = get_connection(
    backend=settings.EMAIL_BACKEND,
    host=settings.EMAIL_HOST,
    port=settings.EMAIL_PORT,
    username=settings.EMAIL_HOST_USER,
    password=settings.EMAIL_HOST_PASSWORD,
    use_tls=settings.EMAIL_USE_TLS,
    use_ssl=settings.EMAIL_USE_SSL,
    timeout=10  # Tiempo límite en segundos
)

# Prepara el correo electrónico
email = EmailMultiAlternatives(
    subject='Test Email',  # Asunto
    body='This is a test email.',  # Cuerpo del mensaje
    from_email=settings.EMAIL_HOST_USER,  # Remitente
    to=['jcampillayworks@gmail.com'],  # Destinatario
    connection=connection  # Conexión personalizada
)

# Envía el correo
email.send()
