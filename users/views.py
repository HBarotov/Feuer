from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Your account has been created! You can login now."
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    context = {
        "form": form,
    }
    return render(request, "users/register.html", context)


@login_required
def profile_view(request, id):
    user = User.objects.get(id=id)
    context = {
        "user": user,
    }

    return render(request, "users/profile.html", context)


@login_required
def profile_update_view(request, id):
    if not id == request.user.id:
        raise PermissionDenied()
    else:
        if request.method == "POST":
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(
                request.POST, request.FILES, instance=request.user.profile
            )
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f"Your account has been updated.")
                return redirect("users:profile", id)

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            "u_form": u_form,
            "p_form": p_form,
        }

    return render(request, "users/profile_update.html", context)
