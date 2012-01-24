from datetime import date, timedelta
from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User

from user_metrics.models import Metric, MetricItem
from user_metrics.api import put_metric

class Command(NoArgsCommand):
    help = "Collect user signups until today"

    requires_model_validation = True

    def handle_noargs(self, **options):
        """ Collect new user signups """

        users = User.objects.filter()
        for user in users:
            put_metric(
                'user-signup',
                date_up=user.date_joined,
            )

