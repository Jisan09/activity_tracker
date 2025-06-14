import django_filters
from .models import UserActivityLog


class UserActivityLogFilter(django_filters.FilterSet):
    timestamp__gte = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    timestamp__lte = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')

    class Meta:
        model = UserActivityLog
        fields = ['action', 'timestamp__gte', 'timestamp__lte', 'user_id', 'status']
