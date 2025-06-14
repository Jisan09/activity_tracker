from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from apps.activity.models import UserActivityLog

User = get_user_model()


class UserActivityLogAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testcase', password='testcase123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.base_url = reverse('activity-log-list')

    def test_post_log(self):
        data = {
            'action': 'UPLOAD_FILE',
            'status': 'PENDING',
            'metadata': {'filename': 'file.txt'}
        }
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'PENDING')

    def test_get_logs(self):
        log = UserActivityLog.objects.create(
            user=self.user,
            action='LOGIN',
            status='DONE',
            metadata={}
        )
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_patch_log_status(self):
        log = UserActivityLog.objects.create(
            user=self.user,
            action='UPLOAD_FILE',
            status='PENDING',
            metadata={}
        )
        url = reverse('activity-log-update-status', kwargs={'pk': log.pk})
        response = self.client.patch(url, {'status': 'IN_PROGRESS'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'IN_PROGRESS')

    def test_put_log(self):
        log = UserActivityLog.objects.create(
            user=self.user,
            action='LOGIN',
            status='PENDING',
            metadata={}
        )
        url = reverse('activity-log-detail', kwargs={'pk': log.pk})
        new_data = {
            'action': 'LOGOUT',
            'status': 'DONE',
            'metadata': {'reason': 'user logged out'}
        }
        response = self.client.put(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['action'], 'LOGOUT')

    def test_delete_log(self):
        log = UserActivityLog.objects.create(
            user=self.user,
            action='LOGOUT',
            status='DONE',
            metadata={}
        )
        url = reverse('activity-log-detail', kwargs={'pk': log.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
