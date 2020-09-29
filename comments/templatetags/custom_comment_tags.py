from django import template

register = template.Library()

@register.inclusion_tag("Comments/_single_blog_comment.html")
def stylized_blog_comment(comment):
    return { 'comment': comment }

@register.inclusion_tag("Comments/_single_problem_comment.html")
def stylized_problem_comment(comment, request):
    return { 'comment': comment, 'request': request }