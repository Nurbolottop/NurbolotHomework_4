from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import generic

class RegisterView(generic.CreateView):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return render(request,"registration/register_done.html",{"user": new_user})
        else:
            return render(request, "registration/register.html", {"form": form})

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/register.html", {"form": form})