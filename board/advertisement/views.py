from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View, generic
from django.views.generic import TemplateView

from .forms import AdvertisementForm
from .models import Advertisement


class Home(TemplateView):
    template_name = "advertisement/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = "http://127.0.0.1:8000/contacts"
        context["about"] = "http://127.0.0.1:8000/about"
        context["categories"] = "http://127.0.0.1:8000/categories"
        context["regions"] = "http://127.0.0.1:8000/regions"
        context["advertisements"] = "http://127.0.0.1:8000/advertisements"
        context["registration"] = "http://127.0.0.1:8000/users/another_register"
        context["login"] = "http://127.0.0.1:8000/users/another_login"
        context["logout"] = "http://127.0.0.1:8000/users/another_logout"
        context["create"] = "http://127.0.0.1:8000/advertisements/create"
        return context


class Advertisements(TemplateView):
    template_name = "advertisement/advertisements.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["advertisements"] = Advertisement.objects.all()
        return context


class Contacts(TemplateView):
    template_name = "advertisement/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Victor Bezai"
        context["phone"] = "+7 918 320 98 52"
        context["email"] = "viktorbezai@gmail.com"
        context["home"] = "http://127.0.0.1:8000/"
        return context


class About(TemplateView):
    template_name = "advertisement/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Бесплатные объявления в вашем городе"
        context["title"] = "Бесплатные объявления"
        context["description"] = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum neque nibh, faucibus ut elementum vel, 
        ultrices a ante. Sed mollis arcu in ex rutrum dignissim. Sed ut iaculis erat, nec ornare diam. Praesent 
        volutpat venenatis diam vel condimentum. Nulla finibus, leo eu rutrum imperdiet, eros eros interdum augue,
         at blandit dui quam at odio. Proin vestibulum, felis non semper mattis, nibh nisi accumsan lacus, a gravida 
         diam ex ac urna. Aliquam sodales ipsum urna, eget congue purus dignissim quis. Lorem ipsum dolor sit amet, 
         consectetur adipiscing elit. Fusce vel ultricies nisi. Aliquam ultrices dapibus pharetra. Proin nec libero nisl. 
         Curabitur at quam eget arcu tempus vestibulum. Suspendisse imperdiet sit amet diam ac blandit. Etiam non aliquam 
         tellus, sit amet tincidunt felis. Sed in metus ut enim ullamcorper vestibulum. Integer ac erat ut ex imperdiet 
         rutrum.
        """
        context["home"] = "http://127.0.0.1:8000/"
        return context


class Categories(TemplateView):
    template_name = "advertisement/categories.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ["Электроника", "Для дома", "Детские товары", "Автомобильные товары", "Одежда"]
        context["home"] = "http://127.0.0.1:8000/"
        return context




class Regions(View):
    def get(self, request):
        context = {
            "regions": ["Краснодар", "Ростов", "Ставрополь", "Грозный", "Волгоград", "Назрань", "Махачкала"],
            "home": "http://127.0.0.1:8000/",
        }
        return render(request, "advertisement/regions.html", context=context)
    def post(self, request):
        return HttpResponse("Регион успешно создан")


def fivth_page(request, *args, **kwargs):
    return HttpResponse("""
    <img src="https://i0.u-mama.ru/d44/469/5db/a276aa090936edf2188908976851edf9.jpg" height=300>
    <h3>Первая страница</h3>
    <a href="http://127.0.0.1:8000/">Назад</a>
    """)


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = "advertisement/advertisement_list.html"
    context_object_name = "advertisements"
    queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
    template_name = "advertisement/advertisement_detail.html"
    context_object_name = "advertisement"


class AdvertisementFormView(View):
    def get(self, request):
        userForm = AdvertisementForm()
        return render(request, "advertisement/create_advertisement.html", context={"user_form": userForm})

    def post(self, request):
        userForm = AdvertisementForm()
        if userForm.is_valid():
            Advertisement.objects.create(**userForm.cleaned_data)
            return HttpResponseRedirect("advertisements/")
        return render(request, "advertisement/create_advertisement.html", context={"user_form": userForm})
