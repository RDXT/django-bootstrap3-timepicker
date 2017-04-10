# -*- coding: utf-8 -*-
import re

from django.forms import TimeInput
from django.utils.html import format_html

COMPONENT_TEMPLATE = u"""
        <div class="input-group bootstrap-timepicker timepicker">
            {}
            <span class="input-group-addon"><i class="glyphicon {}"></i></span>
        </div>
       """

WITHOUT_COMPONENT_TEMPLATE = u"""
        <div class="input-group bootstrap-timepicker timepicker">
            {}
        </div>
        """


class B3timepickerMixin(object):
    format_name = None
    glyphicon = None

    def __init__(self, attrs=None, options=None, component_view=False):
        self.component_view = component_view
        self.options = options

        if self.options is None:
            self.options = {}

        if attrs is None:
            attrs = {}
        for k, v in self.options.items():
            if isinstance(v, bool):
                v = {True: 'true', False: 'false'}[v]
            # set properties
            pattern = re.sub('([A-Z]+)', r'-\1', k).lower()
            # we convert value to string (mainly for boolean values)
            attrs["data-%s" % pattern] = str(v)

        super(B3timepickerMixin, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        attrs["type"] = self.input_type
        attrs["name"] = name
        attrs["data-provide"] = "timepicker"
        final_attrs = self.build_attrs(attrs)
        rendered = super(B3timepickerMixin, self).render(name, value, final_attrs)
        if not self.component_view:
            return format_html(WITHOUT_COMPONENT_TEMPLATE, rendered)
        else:
            return format_html(COMPONENT_TEMPLATE, rendered, self.glyphicon)


class TimeWidget(B3timepickerMixin, TimeInput):
    glyphicon = 'glyphicon-time'

    def __init__(self, attrs=None, options=None, component_view=False):

        if options is None:
            options = {}

        component_view = True
        super(TimeWidget, self).__init__(attrs, options, component_view)
