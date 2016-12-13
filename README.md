# django-bootstrap3-timepicker

Add 'b3timepicker' to installed apps.

# Static
```
{% load b3timepicker_tags %}
{% b3timepicker_css %}
{% b3timepicker_js %}
{{form.media}}
```

By default loads the following version css and js:
```
BOOTSTRAP_TIMEPICKER_VERSION = '0.5.2'
B3TIMEPICKER_JS = '//cdnjs.cloudflare.com/ajax/libs/bootstrap-timepicker/{}/js/bootstrap-timepicker.min.js'
B3TIMEPICKER_CSS = '//cdnjs.cloudflare.com/ajax/libs/bootstrap-timepicker/{}/css/bootstrap-timepicker.min.css'
```
If you just want to use a more recent version available on cdnjs just add BOOTSTRAP_TIMEPICKER_VERSION = '1.whatever'

# Available options

Pretty much all the options from:

https://jdewit.github.io/bootstrap-timepicker/

You can add options to the widget via:
```
widget=TimeWidget(
            options={
                'snapToStep': True,
            }
        )
```

If you dont want to show a clock icon:

```
widget=TimeWidget(
            options={
                'snapToStep': True,
            },
            component_view=False
        )
```