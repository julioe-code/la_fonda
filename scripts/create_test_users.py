import os
import sys
import django

# Añadir la ruta raíz del proyecto al path para que se encuentre el paquete `config`
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User, Group


def ensure_group(name):
    group, _ = Group.objects.get_or_create(name=name)
    return group


def create_user(username, email, password, role):
    if User.objects.filter(username=username).exists():
        print(f"Usuario {username} ya existe. Omitiendo.")
        return
    user = User.objects.create_user(username=username, email=email, password=password)
    group = ensure_group(role)
    user.groups.add(group)
    user.save()
    print(f"Creado usuario: {username} con rol {role}")


if __name__ == '__main__':
    # Credenciales de prueba
    users = [
        ("tester_mesero", "tester_mesero@example.com", "Test1234!", "Mesero"),
        ("tester_cajero", "tester_cajero@example.com", "Test1234!", "Cajero"),
    ]

    for u in users:
        create_user(*u)

    print("Proceso finalizado. Usa las credenciales mostradas para iniciar sesión.")
