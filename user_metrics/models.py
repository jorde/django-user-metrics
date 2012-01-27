from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Metric(models.Model):
    """ holds the types of metrics
    """
    slug = models.SlugField(unique=True, max_length=100, db_index=True)
    name = models.CharField(max_length=90)

    def __unicode__(self): return self.name


class MetricItem(models.Model):
    """ more atomic representation of a metric by each user
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User, null=True, blank=True)

    count = models.IntegerField(default=1)
    date_up = models.DateField(default=date.today)

    def __unicode__(self):
        '%d %s by %s at %s' % (self.count, self.metric.name, self.user, self.date_up)


class MetricDay(models.Model):
    """ represent aggregation of metrics daily
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User, null=True, blank=True)

    count = models.IntegerField(default=0)
    date_up = models.DateField(default=date.today)
    
    def __unicode__(self):
        return '%s' % self.count


class MetricWeek(models.Model):
    """ represent aggregation of metric weekly
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User, null=True, blank=True)

    count = models.IntegerField(default=0)
    date_up = models.DateField(default=date.today)
    
    def __unicode__(self):
        return '%s' % self.count

class MetricMonth(models.Model):
    """ represent aggregation of metric weekly
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User, null=True, blank=True)

    count = models.IntegerField(default=0)
    date_up = models.DateField(default=date.today)
    
    def __unicode__(self):
        return '%s' % self.count


class MetricKey(models.Model):
    metric = models.ForeignKey(Metric)
    key = models.CharField(max_length=255)
    
    value = models.FloatField(null=True, blank=True)

# Cohorts

class Cohort(models.Model):
    metric = models.ForeignKey(Metric)
    cohort = models.CharField(max_length=255)

class CohortWeek(models.Model):
    metric = models.ForeignKey(Metric)
    cohort = models.ForeignKey(Cohort)
    value = models.FloatField(null=True, blank=True)
    
    date_up = models.DateField(default=date.today)

class CohortMonth(models.Model):
    metric = models.ForeignKey(Metric)
    cohort = models.ForeignKey(Cohort)
    value = models.FloatField(null=True, blank=True)
    
    date_up = models.DateField(default=date.today)