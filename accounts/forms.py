from django.contrib.auth.forms import UserCreationForm
from tinymce import widgets


class TinyMCEWidget(widgets.TinyMCE):
    def use_required_attribute(self, *args):
        return False


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name']

    def save(self, commit=True):
        self.instance.is_active = False
        return super().save(commit)



