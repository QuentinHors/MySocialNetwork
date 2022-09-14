from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForms, PostForm
from .models import Profile, Post
import os


@login_required
def profile_page(request):
    user = request.user
    user_posts = Post.objects.filter(user__id=user.id)
    context = {'user_posts': user_posts}
    if Profile.objects.filter(user__id=user.id).exists():
        context['already_created'] = True
    else:
        context['already_created'] = False
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


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            redirection_page = request.POST.get('next')
            return redirect(redirection_page)

        context = {'form': form, 'errors': 'Informations invalides'}
        return render(request, 'profile_page/create_profile.html', context=context)

    form = PostForm()
    context = {'form': form}
    return render(request, 'profile_page/create_post.html', context=context)


@login_required
def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        image_post = post.image
        if form.is_valid():
            if 'image' in form.changed_data and image_post:
                os.remove(image_post.path)
            form.save()
            redirection_page = request.POST.get('next')
            return redirect(redirection_page)

        context = {'form': form,
                   'profile': post,
                   'errors': 'Informations invalides'}
        return render(request, 'profile_page/update_post.html', context=context)

    form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'profile_page/update_post.html', context=context)


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    image_post = post.image
    if image_post:
        os.remove(path=image_post.path)
    post.delete()
    redirection_page = request.GET.get('next')
    return redirect(redirection_page)