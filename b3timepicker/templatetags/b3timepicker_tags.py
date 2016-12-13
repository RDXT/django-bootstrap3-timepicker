# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

from b3timepicker.conf import settings

register = template.Library()


@register.simple_tag
def b3datepicker_css():
    css_template = u'<link rel="stylesheet" href="{}" type="text/css" charset="utf-8">'
    css = css_template.format(settings.B3DATEPICKER_CSS)
    return mark_safe(css)


@register.simple_tag()
def b3datepicker_js():
    js_template = u'<script src="{}" type="text/javascript" charset="utf-8"></script>'
    js = js_template.format(settings.B3DATEPICKER_JS)
    return mark_safe(js)
