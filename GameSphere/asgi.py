import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GameSphere.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "https": django_asgi_app,
})