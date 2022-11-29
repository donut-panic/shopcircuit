import django.forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.forms import ChoiceField, CharField, ModelForm,  EmailField, BooleanField, CheckboxInput
from tinymce import widgets
from tinymce.widgets import TinyMCE
from accounts.models import Profile


class TinyMCEWidget(widgets.TinyMCE):
    def use_required_attribute(self, *args):
        return False


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'first_name', 'last_name']
        field_classes = {'username': UsernameField, 'email': EmailField}

    def save(self, commit=True):
        self.instance.is_active = False
        return super().save(commit)



class UserProfileUpdateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    class Meta:
        model = Profile
        fields = '__all__'

    gender = ChoiceField(choices=GENDER_CHOICES, required=False)
    biography = CharField(label="Maybe something About yourself", widget=TinyMCE(),
                      required=False)





class LoginForm(AuthenticationForm):
    remember_me = BooleanField(label='Remember me', initial=False,
                                     required=False, widget=CheckboxInput(attrs={'class': 'form-check'}))
