from datetime import date, timedelta
from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User

from user_metrics.models import Metric, MetricItem

class Command(NoArgsCommand):
    help = "Collect user signups until today"

    requires_model_validation = True

    def handle_noargs(self, **options):
        """ Collect new user signups """

        # Get Metric for this type
        metric, created = Metric.objects.get_or_create(slug='user-signup', name="User Signup")
        
        # Save new user sign up data points
        users = User.objects.filter()
        for user in users:
            MetricItem(
                metric = metric,
                user = user,
            ).save()

