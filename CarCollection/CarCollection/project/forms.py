from django import forms

from CarCollection.project.models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ["first_name", "last_name", 'profile_picture']
        widgets = {
            'password': forms.PasswordInput(),
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class DeleteCarForm(CreateCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'