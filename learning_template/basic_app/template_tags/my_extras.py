from django import template
register = template.Library()


@register.filter(name='cuta')
def cut(value,arg):
    return value.replace(arg,'')

#register.filter('cuttt', cut)
