from django.conf import settings

SELECTOR = getattr(settings, 'ADMIN_DISPLAY_FIELDS_SETTINGS_SELECTOR', None)
INSERT_TYPE = getattr(settings, 'ADMIN_DISPLAY_FIELDS_SETTINGS_INSERT_TYPE', None)