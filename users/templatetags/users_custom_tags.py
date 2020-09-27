from django import template
from problems.models import Problem


register = template.Library()

@register.inclusion_tag("users/problems_table.html")
def tabularized_problems(problems):
    return { 'problems': problems }