from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from profile_page.models import Post


@login_required
def home_page(request):
    user = request.user
    user_posts = Post.objects.filter(user__id=user.id)
    context = {'user_posts': user_posts}
    return render(request, 'home_page/index.html', context=context)
