from django.urls import path

from app_pages.views import translation_example

urlpatterns = [
    path("", translation_example, name="example"),
]
