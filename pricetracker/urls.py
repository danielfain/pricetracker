from django.contrib import admin
from django.urls import path, include

from tracker.views import TrackerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TrackerView.as_view(), name="tracker"),
]
