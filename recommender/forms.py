from django import forms

from .models import User


class UserForm(forms.ModelForm):
    # userName = forms.CharField(max_length=20)
    # age = forms.CharField(max_length=3)
    # genre = forms.CharField(max_length=20)
    # keyword = forms.CharField(max_length=20)
    # theme = forms.CharField(max_length=20)
    # game_modes = forms.CharField(max_length=20)
    # tags = forms.CharField(max_length=20)
    # platforms = forms.CharField(max_length=20) ## can use these to override

    class Meta:
        model = User
        fields = [
            'userName',
            'age',
            'genre',
            'keyword',
            'theme',
            'game_modes',
            'tags',
            'platforms'
        ]

    def clean_userName(self):
        # validate the field - can make one for any field
        data = self.cleaned_data.get('userName')
        if len(data) < 4:
            raise forms.ValidationError("Username is not long enough")
        return data