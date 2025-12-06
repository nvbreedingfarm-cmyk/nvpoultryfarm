from django.contrib.auth import get_user_model

def create_default_superuser():
    User = get_user_model()

    username = "admin"
    email = "admin@example.com"
    password = "Admin@123"   # change if you want

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superuser created successfully!")
    else:
        print("Superuser already exists.")
