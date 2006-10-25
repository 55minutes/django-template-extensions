from django.template import Library
register = Library()

@register.simple_tag
def version_number():
    try:
        from django.conf import settings
    except ImportError:
        return ''
    return settings.VERSION
