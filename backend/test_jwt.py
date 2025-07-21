import os
import django

# Configurar settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

# Ahora puedes importar cosas de Django
from rest_framework_simplejwt.authentication import JWTAuthentication

print(JWTAuthentication)
