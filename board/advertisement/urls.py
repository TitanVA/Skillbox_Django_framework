from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('contacts/', Contacts.as_view(), name="contacts"),
    path('about/', About.as_view(), name="about"),
    path('categories/', Categories.as_view(), name="categories"),
    path('regions/', Regions.as_view(), name="regions"),
    path('advertisements/', AdvertisementListView.as_view(), name="advertisements"),
    path('advertisements/create/', AdvertisementFormView.as_view(), name="create_advertisement"),
    path('advertisements/<int:pk>/', AdvertisementDetailView.as_view(), name="advertisements-detail"),
]
