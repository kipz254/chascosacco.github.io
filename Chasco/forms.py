from django import forms

from Chasco.models import Member, Management


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your gender'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'zone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your zone'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'images/*', 'title': 'Upload your image here'}),
        }


class ManagementForm(forms.ModelForm):
    class Meta:
        model = Management
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your role'}),
            'image': forms.FileInput(attrs={'class': 'form-control','accept': 'images/*', 'title': 'Upload your image here'}),

        }