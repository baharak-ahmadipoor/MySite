from unicodedata import category
from django import template
from blog.models import Post,Category

register = template.Library()

@register.simple_tag (name= 'posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value, arg=50):
#    return value[:len]
    term = ''
    if len(value) > arg:
        term = ' ...'
    return value[:arg]+ term

@register.inclusion_tag('blog/popular-posts.html')
def latestposts (arg=3):
    tagposts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'tagposts': tagposts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    categories = Category.objects.all()
    posts = Post.objects.filter(status=1)
    cat_dict = {}
    for cat in categories:
        cat_dict[cat] = posts.filter(category=cat).count()
    return {'categories':cat_dict}
