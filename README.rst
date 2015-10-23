=====================================
django-admin-display-fields-settings
=====================================

Django application. It adds a column view control form into admin area.

Quick start
-----------

1. Download it from PyPi with ``pip install django-admin-display-fields-settings``

2. Add "admin_display_fields_settings" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'admin_display_fields_settings',
      )

3. Include the admin_display_fields_settings URLconf in your project urls.py like this::

      url(r'^admin_display_fields_settings/', include('admin_display_fields_settings.urls'))

4. Run ``python manage.py syncdb`` or ``python manage.py migrate`` to create the admin_display_fields_settings models.

5. In your admin.py::

      from django.contrib import admin
      from polls.models import MyModel
      from admin_display_fields_settings.admin import DisplayFieldsSettingsAdmin


      class MyModelAdmin(DisplayFieldsSettingsAdmin):
          pass

      admin.site.register(MyModel, MyModelAdmin)
      
Example
-------
.. image:: http://s12.postimg.org/mao49p13f/django_admin_display_fields_settings.png
