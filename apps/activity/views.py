from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import UserActivityLog
from .serializers import UserActivityLogSerializer
from .filters import UserActivityLogFilter
# Create your views here.


class UserActivityLogViewSet(viewsets.ModelViewSet):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = UserActivityLogFilter
    ordering_fields = ['timestamp']
    ordering = ['-timestamp']

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return UserActivityLog.objects.none()

        user = self.request.user
        if user.is_staff:
            return UserActivityLog.objects.all()
        return UserActivityLog.objects.filter(user=user)

    @action(detail=True, methods=["patch"], url_path="update-status")
    def update_status(self, request, pk=None):
        log = self.get_object()
        new_status = request.data.get("status")

        if new_status not in ['PENDING', 'IN_PROGRESS', 'DONE']:
            return Response(
                {"error": "Invalid status"},
                status=status.HTTP_400_BAD_REQUEST
            )

        log.status = new_status
        log.save()
        return Response(self.get_serializer(log).data)
