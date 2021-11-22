from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_profile.forms import UserForm
from django.views import View
from app_profile.models import User


class UserFormView(View):
    def get(self, request):
        userForm = UserForm()
        return render(request, "app_profile/register.html", context={"user_form": userForm})

    def post(self, request):
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            User.objects.create(**userForm.cleaned_data)
            return HttpResponseRedirect("/")
        return render(request, "app_profile/register.html", context={"user_form": userForm})


class UserEditFormView(View):
    def get(self, request, profile_id):
        user = User.objects.get(id=profile_id)
        user_form = UserForm(instance=user)
        return render(request, "app_profile/edit.html", context={"user_form": user_form, "profile_id": profile_id})

    def post(self, request, profile_id):
        user = User.objects.get(id=profile_id)
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user.save()
        return render(request, "app_profile/edit.html", context={"user_form": user_form, "profile_id": profile_id})
