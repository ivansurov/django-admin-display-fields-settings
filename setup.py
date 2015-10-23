import os
from setuptools import setup

def read(fname):
	try:
	    return open(os.path.join(os.path.dirname(__file__), fname)).read()
	except IOError:
	    return ''

setup(
    name='django-admin-display-fields-settings',
    version=__import__('admin_display_fields_settings').__version__,
    description=read('DESCRIPTION'),
    license='GPL',
    keywords="django admin fields column setting"
    author='Ivan Surov',
    author_email='ivansurovv@gmail.com',
    packages=['admin_display_fields_settings'],
    include_package_data=True,
    long_description=long_description=read('README'),
    url='https://github.com/ivansurov/django-admin-display-fields-settings',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: GPL',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
