from django.contrib import admin
from user_metrics.models import Metric, MetricDay, MetricWeek, Cohort, CohortWeek

class MetricDayAdmin(admin.ModelAdmin):
    list_display = ('date_up', 'metric', 'user', 'count', )
    ordering = ('date_up',)
    search_fields = ('date_up',)

class MetricWeekAdmin(admin.ModelAdmin):
    list_display = ('date_up', 'metric', 'user', 'count', )
    ordering = ('date_up',)
    search_fields = ('date_up',)

admin.site.register(Metric)
admin.site.register(MetricDay, MetricDayAdmin)
admin.site.register(MetricWeek, MetricWeekAdmin)
admin.site.register(Cohort)
admin.site.register(CohortWeek)
