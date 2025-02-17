from django import template

register = template.Library()

@register.filter()
def censor(value,):
    redis = "редиска"
    if redis in value:
        value = value.replace("редиска", "р" + "+" * 6)
    return value
