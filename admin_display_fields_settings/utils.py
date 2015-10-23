from urlparse import urlparse
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import QueryDict


def getAdminViewByUrl(url):
    """
    Get Admin View
    """

    if url is None:
        return False

    http_referer = urlparse(url).path
    for obj in admin.site._registry:
        view = admin.site._registry[obj]
        if http_referer == reverse("admin:%s_%s_changelist" % (
                view.model._meta.app_label, view.model._meta.model_name
        )):
            return view


def getDisplayFieldsSettingsForm(url, user, data=None):

    view = getAdminViewByUrl(url)
    if view is False:
        return False
    return view.get_list_display_settings_form(user, data)


def deserialize_form(data):
    """
    Create a new QueryDict from a serialized form.
    """
    return QueryDict(query_string=unicode(data).encode('utf-8'))
