from django import forms

class DisplayFieldsSettings(forms.Form):
    
    def __init__(self, fields, *args, **kwargs):
        super(DisplayFieldsSettings, self).__init__(*args, **kwargs)

        for name in fields:
            field = fields[name]

            self.fields[name] = eval(field.get('class'))()
            self.fields[name].required = field.get('required') or False
            self.fields[name].label = field.get('label')

            if 'widget' in field:
                self.fields[name].widget = eval(field.get('widget'))()

    def clean(self):

        sort_opts = (self.cleaned_data.get('sort_opts') or '').strip()
        if len(sort_opts) > 0:
            for field in sort_opts.split(','):
                if field not in self.cleaned_data:
                    raise forms.ValidationError(u"Field %s does not exists" % field, code='invalid')

        return self.cleaned_data
