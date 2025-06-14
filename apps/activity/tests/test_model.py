from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from apps.activity.models import UserActivityLog

User = get_user_model()


class UserActivityLogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testcase', email='test@example.com', password='testcase123')

    def test_create_log(self):
        log = UserActivityLog.objects.create(
            user=self.user,
            action='UPLOAD_FILE',
            status='PENDING',
            timestamp=timezone.now(),
            metadata={'filename': 'test.txt'}
        )
        self.assertEqual(log.user, self.user)
        self.assertEqual(log.status, 'PENDING')
        self.assertIn('filename', log.metadata)
