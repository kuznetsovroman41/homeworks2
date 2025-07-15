from datetime import timedelta
from django.utils import timezone
from django.db.models import Q, Count, F
from webapp.models import Issue, IssueStatus, IssueType

now = timezone.now()
month_ago = now - timedelta(days=30)
closed_status = IssueStatus.objects.get(name__iexact='Done')
status_1 = IssueStatus.objects.get(name='In Progress')
status_2 = IssueStatus.objects.get(name='Done')
type_1 = IssueType.objects.get(name='Task')
type_2 = IssueType.objects.get(name='Bug')

# 1.
Issue.objects.filter(status=closed_status, updated_at__gte=month_ago).values('id', 'summary', 'status__name', 'types__name').distinct()

# 2.
Issue.objects.filter(status__in=[status_1, status_2], types__in=[type_1, type_2]).values('id', 'summary', 'status__name', 'types__name').distinct()

# 3.
Issue.objects.filter(~Q(status=closed_status), Q(summary__icontains='bug') | Q(types__name__iexact='Bug')).values('id', 'summary', 'status__name', 'types__name').distinct()

# Бонус 2.
Issue.objects.filter(summary=F('description')).values('id', 'summary', 'status__name', 'types__name')

# Бонус 3.
Issue.objects.values('types__name').annotate(count=Count('id'))

