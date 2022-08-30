# -*- coding: utf-8 -*-
"""
Implement 'create_superuser' Django management command.
"""
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from requests import HTTPError

User = get_user_model()


class Command(BaseCommand):
    """
    A management command which creates default superuser.
    """
    help = 'Create default superuser'

    def handle(self, *args, **kwargs):
        auth = settings.FIREBASE.auth()

        email = 'admin@example.com'
        password = 'admin123'
        firstname = 'John'
        lastname = 'Doe'

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(
                first_name=firstname,
                last_name=lastname,
                username=f'{firstname.lower()}-{lastname.lower()}',
                email=email,
                password=password,
            )

        try:
            auth.create_user_with_email_and_password(email, password)
        except HTTPError:
            pass

        print('-' * 20)
        print(f'\nUsername: {firstname.lower()}-{lastname.lower()}\nEmail: {email}\nPassword: {password}\n')
        print('-' * 20)
