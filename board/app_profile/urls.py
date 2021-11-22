from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserFormView.as_view()),
    path('<int:profile_id>/edit/', UserEditFormView.as_view()),
]
