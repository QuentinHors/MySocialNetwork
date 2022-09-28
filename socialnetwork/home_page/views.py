from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from profile_page.models import Post, Comment


@login_required
def home_page(request):
    user = request.user
    user_posts = Post.objects.filter(user__id=user.id)
    user_posts_and_comments = []
    for post in user_posts:
        user_posts_and_comments.append((post, Comment.objects.filter(post_reference__id=post.id)))
    context = {'user_posts': user_posts_and_comments}
    return render(request, 'home_page/index.html', context=context)
