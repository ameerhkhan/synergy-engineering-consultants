from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    from_email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    # we can also add captcha here. But not at the moment.
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
