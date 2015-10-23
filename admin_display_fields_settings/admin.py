from django.contrib import admin
from django.db.models import FieldDoesNotExist
from forms import DisplayFieldsSettings
from models import DisplaySettings
import json, types


class DisplayFieldsSettingsAdmin(admin.ModelAdmin):

    class Media:
        css = {
            "all": (
                "/admin_display_fields_settings/admin/css/admin_display_fields_settings.css",
                "admin/css/forms.css",
            )
        }
        js = (
            "admin/js/jquery.js",
            "/admin_display_fields_settings/admin/js/admin_display_fields_settings.js",
        )

    def get_field(self, field_name):

        try:
            field = self.opts.get_field(field_name)
            return field.name
        except FieldDoesNotExist:
            if callable(field_name):
                attr = field_name
            elif hasattr(self, field_name):
                attr = getattr(self, field_name)
            else:
                attr = getattr(self.model, field_name)
            print attr
            return getattr(attr, '__name__', None)

    def get_fields_names(self):
        response = []
        for field in self.list_display:

            name = None

            try:
                name = self.opts.get_field(field).verbose_name
            except FieldDoesNotExist:

                if hasattr(self.model, field):
                    if field == '__str__' or field == '__unicode__':
                        name = self.model.__name__
                    else:
                        mth = getattr(self.model, field)
                        if hasattr(mth, 'short_description'):
                            name = getattr(mth, 'short_description')

                elif isinstance(field, types.FunctionType):
                    if hasattr(field, 'short_description'):
                        name = getattr(field, 'short_description')
                    else:
                        field = field.__name__

            if name is None:
                name = field.replace('_', ' ')

            response.append([field, name.capitalize()])

        return response

    def get_list_display_settings(self, user):
        obj, created = DisplaySettings.objects\
            .get_or_create(user_id=user, app_label=self.opts.app_label,
                    model=self.model.__name__, view=self.__class__.__name__)

        settings = json.loads(obj.settings or '{}')
        return settings.get('list_display') or {}

    def get_list_display_settings_form(self, user, data=None):
        fields = self.get_fields_names()
        list_display = self.get_list_display_settings(user)
        return DisplayFieldsSettings(
            fields,
            initial={field[0]: list_display.get(field[0], True) for field in fields},
            data=data
        )

    def get_list_display(self, request):
        """
        Return a sequence containing the fields to be displayed on the
        changelist.
        """

        response = list(self.list_display)
        list_display = self.get_list_display_settings(request.user)
        if len(list_display) > 0:
            for field in self.list_display:
                if field in list_display and list_display[field] is False:
                    del response[response.index(field)]
        return response