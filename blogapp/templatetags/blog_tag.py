from django import template

from django.db.models import Count
from blogapp.models import Blog

register=template.Library()


@register.inclusion_tag("most_commented_posts.html")
def get_most_commented_posts(count=5):
    most_commented=Blog.objects.annotate(total_comment=Count('comment')).order_by('-total_comment')[:count]

    return {'most_commented':most_commented}


@register.inclusion_tag("recent_post.html")
def get_recent_post(count=5):
    lastest_post=Blog.objects.order_by('date')[:count]
    return {'latest_post':lastest_post}