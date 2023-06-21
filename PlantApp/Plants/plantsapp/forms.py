from django import forms

from Plants.plantsapp.models import Profile, Plant


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreatePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'

class DeletePlantForm(CreatePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


