# This just ChatGOT code to populate sample data
# python manage.py seed_activity


from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.activity.models import UserActivityLog
from django.utils import timezone
import random

User = get_user_model()


class Command(BaseCommand):
    help = 'Seed the database with test user activity logs.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding test data...'))

        users_info = [
            {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpass123'},
            {'username': 'sampleuser', 'email': 'sample@example.com', 'password': 'samplepass123'}
        ]

        actions = ['LOGIN', 'LOGOUT', 'UPLOAD_FILE']
        statuses = ['PENDING', 'IN_PROGRESS', 'DONE']

        # Clear previous logs
        UserActivityLog.objects.all().delete()

        for user_info in users_info:
            user, created = User.objects.get_or_create(
                username=user_info['username'],
                defaults={'email': user_info['email']}
            )
            if created:
                user.set_password(user_info['password'])
                user.save()

            for i in range(10):
                UserActivityLog.objects.create(
                    user=user,
                    action=random.choice(actions),
                    status=random.choice(statuses),
                    timestamp=timezone.now(),
                    metadata={'info': f'Test log {i} for {user.username}'}
                )

        self.stdout.write(self.style.SUCCESS('✅ Seeded test data for testuser & sampleuser!'))
