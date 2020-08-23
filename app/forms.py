from django import forms


class RackForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(RackForm, self).__init__(*args, **kwargs)
        self.fields['rack'].widget.attrs['placeholder'] = 'Enter rack letters'

    rack = forms.CharField(label='', max_length=50)
