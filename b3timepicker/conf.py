# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.conf import settings as base_settings


class B3timepickerConfig(AppConfig):
    name = 'b3timepicker'


class Settings(object):
    BOOTSTRAP_TIMEPICKER_VERSION = '0.5.2'
    B3TIMEPICKER_JS = '//cdnjs.cloudflare.com/ajax/libs/bootstrap-timepicker/{}/js/bootstrap-timepicker.min.js'.format(
        BOOTSTRAP_TIMEPICKER_VERSION)
    B3TIMEPICKER_CSS = '//cdnjs.cloudflare.com/ajax/libs/bootstrap-timepicker/{}/css/bootstrap-timepicker.min.css'.format(
        BOOTSTRAP_TIMEPICKER_VERSION)

    def __getattribute__(self, name):
        if hasattr(base_settings, name):
            return getattr(base_settings, name)
        return object.__getattribute__(self, name)


settings = Settings()
