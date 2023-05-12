from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.JlsSummary)


@admin.register(models.JlsSummary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ("s_id", "v_id", "v_date", "amount", "source", "source_id")
