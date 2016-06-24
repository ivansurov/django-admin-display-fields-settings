=====================================
django-admin-display-fields-settings
=====================================

Django application. It adds a column view control form into admin area. You can choose which fields to display and sort them in the correct order for you. Possible fields for display are taken from ``list_display``. To sort the fields just drag the field into place.

Motivation
-----------
Any user can choose to display the column for yourself!

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

          list_display = ('question', 'pub_date', 'was_published_recently', 'full_name', '__str__', '__unicode__')

      admin.site.register(MyModel, MyModelAdmin)
      
Example
-------
.. image:: https://cloud.githubusercontent.com/assets/15198843/10693762/912bfd86-799a-11e5-8b44-2bf3c6121930.png
