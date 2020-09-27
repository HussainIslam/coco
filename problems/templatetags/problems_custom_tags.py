from django import template

register = template.Library()

@register.inclusion_tag("Problems/_problem_info.html")
def problem_info_in_list(problem):
    return { 'problem': problem }