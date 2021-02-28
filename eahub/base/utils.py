import csv

from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse

from ..profiles import models


def user_display(user):
    try:
        profile = user.profile
    except models.Profile.DoesNotExist:
        return user.email
    return profile.name


def get_feedback_url(request):
    return f"https://feedback.{get_current_site(request).domain}"


class ExportCsvMixin:
    def export_csv(self, request, queryset, model, filename):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(filename)
        writer = csv.writer(response)

        field_names = model.get_exportable_field_names()
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow(obj.convert_to_row(field_names))

        return response

    export_csv.short_description = "Export as CSV"
