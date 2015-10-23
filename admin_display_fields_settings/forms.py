from django.forms import Form, BooleanField


class DisplayFieldsSettings(Form):
    
    def __init__(self, fields, *args, **kwargs):
        super(DisplayFieldsSettings, self).__init__(*args, **kwargs)

        for field in fields:
            self.fields[field[0]] = BooleanField(required=False, label=field[1])