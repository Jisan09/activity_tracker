from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.activity.models import UserActivityLog
# Create your tests here.


User = get_user_model()


class UserActivityLogTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        self.log_url = reverse('useractivitylog-list')

    def test_create_activity_log(self):
        data = {
            "action": "LOGIN",
            "status": "PENDING",
            "metadata": {"ip": "127.0.0.1"}
        }
        response = self.client.post(self.log_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserActivityLog.objects.count(), 1)

    def test_get_activity_logs(self):
        UserActivityLog.objects.create(user=self.user, action="LOGOUT", status="DONE")
        response = self.client.get(self.log_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_by_action(self):
        UserActivityLog.objects.create(user=self.user, action="UPLOAD_FILE", status="PENDING")
        response = self.client.get(self.log_url + '?action=UPLOAD_FILE')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_status_patch(self):
        log = UserActivityLog.objects.create(user=self.user, action="LOGIN", status="PENDING")
        patch_url = reverse('useractivitylog-update-status', args=[log.id])
        response = self.client.patch(patch_url, {"status": "IN_PROGRESS"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        log.refresh_from_db()
        self.assertEqual(log.status, "IN_PROGRESS")
