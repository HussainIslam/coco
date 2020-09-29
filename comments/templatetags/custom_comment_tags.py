from django import template

register = template.Library()

@register.inclusion_tag("Comments/_single_comment.html")
def stylized_comment(comment):
    return { 'comment': comment }