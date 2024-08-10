from django import forms
from .models import UserProfile, ThreeDModel

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name', 'last_name', 'shop_name', 'role_at_shop',
            'owner_of_shop', 'phone_number', 'email_address',
            'shop_description', 'subscription_detail','bio', 'location', 
            'birth_date'
        ]
        widgets = {
            'shop_description': forms.Textarea(attrs={'rows': 3}),
            'subscription_detail': forms.Textarea(attrs={'rows': 3}),
            'bio': forms.Textarea(attrs={'rows': 3}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'required': True})
        self.fields['last_name'].widget.attrs.update({'required': True})
        self.fields['role_at_shop'].widget.attrs.update({'required': True})
        self.fields['phone_number'].widget.attrs.update({'required': True})
        self.fields['email_address'].widget.attrs.update({'required': True})
        # date_of_joining is automatically set and immutable, so no need to include it in the form

class ThreeDModelForm(forms.ModelForm):
    """Form for managing 3D models."""
    
    class Meta:
        model = ThreeDModel
        fields = ['model_id', 'category', 'description', 'obj_file']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'obj_file': forms.ClearableFileInput(attrs={'accept': '.obj'}),
        }
        
