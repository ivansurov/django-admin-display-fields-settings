from django.http import HttpResponseNotFound, HttpResponseForbidden
from http import JsonResponse
from utils import getAdminViewByUrl, deserialize_form
from models import DisplaySettings
from django.template.loader import render_to_string
from settings import SELECTOR, INSERT_TYPE
import json


def changeFormHandler(request):

    if not request.user.is_authenticated():
        return HttpResponseForbidden()

    if not request.is_ajax() or request.method != "POST":
        return HttpResponseNotFound('<h1>Page not found</h1>')

    view = getAdminViewByUrl(request.META.get('HTTP_REFERER'))
    if view is False or view is None:
        return JsonResponse({}, errors=['Not found this view'], success=False)

    if not view.has_change_permission(request):
        return HttpResponseForbidden()

    if request.POST.get('operation') == 'get_form':

        form = view.get_list_display_settings_form(request.user)

        return JsonResponse({
            'insert_type': INSERT_TYPE,
            'selector': SELECTOR,
            'form': render_to_string(
                'admin_display_fields_settings/admin/admin_display_fields_settings.html', {'form': form})
        }, success=True)

    if request.POST.get('operation') == 'save_form' and request.POST.get('form'):

        form = view.get_list_display_settings_form(request.user, deserialize_form(request.POST.get('form')))
        if form.is_valid():

            obj, created = DisplaySettings.objects\
                .get_or_create(user_id=request.user, app_label=view.opts.app_label,
                               model=view.model.__name__, view=view.__class__.__name__)

            settings = json.loads(obj.settings or '{}')
            settings['list_display_sort'] = form.cleaned_data['sort_opts'].split(',')
            del form.cleaned_data['sort_opts']
            settings['list_display'] = form.cleaned_data

            obj.settings = json.dumps(settings)
            obj.save()

            return JsonResponse({}, errors=[], success=True)

    return JsonResponse({}, errors=[], success=False)