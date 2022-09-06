from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForms
from .models import Profile
import os


@login_required
def profile_page(request):
    if Profile.objects.filter(user__id=request.user.id).exists():
        context = {'already_created': True}
    else:
        context = {'already_created': False}
    return render(request, 'profile_page/index.html', context=context)


@login_required
def create_profile(request):
    if Profile.objects.filter(user__id=request.user.id):
        return redirect('update_profile')

    if request.method == 'POST':
        form = ProfileForms(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/profile')

        context = {'form': form, 'errors': 'Informations invalides'}
        return render(request, 'profile_page/create_profile.html', context=context)

    form = ProfileForms()
    context = {'form': form}
    return render(request, 'profile_page/create_profile.html', context=context)


@login_required
def update_profile(request):
    profile = Profile.objects.get(user__id=request.user.id)
    if request.method == 'POST':
        form = ProfileForms(request.POST, request.FILES, instance=profile)
        image_profile = profile.image_profile
        if form.is_valid():
            if 'image_profile' in form.changed_data and image_profile:
                os.remove(image_profile.path)
            form.save()
            return redirect('/profile')

        context = {'form': form,
                   'profile': profile,
                   'errors': 'Informations invalides'}

        return render(request, 'profile_page/update_profile.html', context=context)

    form = ProfileForms(instance=profile)
    context = {'form': form, 'profile': profile}
    return render(request, 'profile_page/update_profile.html', context=context)
