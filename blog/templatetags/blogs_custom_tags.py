from django import template

register = template.Library()

@register.inclusion_tag("Blog/_blog_info.html")
def blog_info_in_list(blog):
    return { 'blog': blog }