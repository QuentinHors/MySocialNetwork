from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForms
from .models import Profile


@login_required
def profile_page(request):
    return render(request, 'profile_page/index.html')


@login_required
def create_or_update_profile(request):
    create = Profile.objects.filter(user__id=request.user.id).exists()

    if request.method == 'POST':

        if not create:
            form = ProfileForms(request.POST, request.FILES)
        else:
            profile = Profile.objects.get(user__id=request.user.id)
            form = ProfileForms(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            if not create:
                form = form.save(commit=False)
                form.user = request.user
            form.save()
            return redirect('/profile')
        else:
            context = {'form': form, 'errors': 'Informations invalides'}
            return render(request, 'profile_page/create_profile.html', context=context)

    if not create:
        form = ProfileForms()
        context = {'form': form}
    else:
        profile = Profile.objects.get(user__id=request.user.id)
        form = ProfileForms(instance=profile)
        context = {'form': form, 'profile': profile}

    return render(request, 'profile_page/create_profile.html', context=context)
