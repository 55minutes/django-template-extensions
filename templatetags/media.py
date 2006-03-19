from django.core.template import Library
register = Library()

def media_prefix():
    try:
        from django.conf.settings import MEDIA_URL
    except ImportError:
        return ''
    return MEDIA_URL
media_prefix = register.simple_tag(media_prefix)
