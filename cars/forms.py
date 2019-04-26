from django import forms




class ContactForm(forms.Form):
    
    subject = forms.CharField()
    e_mail = forms.EmailField(widget=forms.EmailInput, required=False, label='E-mail')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):

        message = self.cleaned_data['message']
        token_count = len(message.split())
        if token_count < 3:
            raise forms.ValidationError('There are too few words!')
        return message
    