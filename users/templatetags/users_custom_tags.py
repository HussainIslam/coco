from django import template

register = template.Library()

from problems.models import Problem


@register.inclusion_tag("users/problems_table.html")
def tabularized_problems(problems):
    return { 'problems': problems }