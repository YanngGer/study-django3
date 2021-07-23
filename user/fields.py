from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat


class RestrictedFileField(FileField):

    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types", [])
        self.max_upload_size = kwargs.pop("max_upload_size", [])

        super().__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super().clean(*args, **kwargs)
        file = data.file

        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file.size > self.max_upload_size:
                    raise forms.ValidationError('Please keep filesize under {}. Current filesize {}'
                                                .format(filesizeformat(self.max_upload_size),
                                                        filesizeformat(file.size)))
            else:
                raise forms.ValidationError('This file type is not allowed.')
        except AttributeError:
            pass
        return data
