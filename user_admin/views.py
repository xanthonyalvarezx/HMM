from django.shortcuts import render
from user_admin.models import Register
from user_admin.forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, Http404, reverse

# Create your views here.

# LOGIN VIEW
def login_view(request):
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(
                request, username=data["username"], password=data["password"])
            if user:

                login(request, user)

                return HttpResponseRedirect(request.GET.get("next", reverse("landingpage")))  # noqa

        form = LoginForm()

        return render(request, "generic_form.html", {"form": form})