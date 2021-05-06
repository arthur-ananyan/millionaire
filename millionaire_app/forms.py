from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.fields['username'].label = 'Անուն'
        self.fields['password1'].label = 'Գաղտնաբառ'
        self.fields['password2'].label = 'Կրկնել Գաղտնաբառը'
