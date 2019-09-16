from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Housing, Business, Comments,Services
from django.contrib.auth.models import User
from django.contrib.gis import forms

# signup form adding custom field
class SignUpForm(UserCreationForm):
    """
    user creation form for sigup, adding custom field to signup form

    """
    email = forms.CharField(max_length=254, required=True)
    class Meta:
        model = User
        fields = ['username']


# Form for editing profile
class EditProfileForm(forms.ModelForm):
    """
    form for editing profile
    """
    class Meta:
        model = Profile
        fields = ['user', 'pic', 'bio']


class BusinessForm(forms.ModelForm):
    """
    form to create neighbourhood by users
    """
    location = forms.PointField(widget = 
        forms.OSMWidget(attrs = {'map_width': 1024, 'map_height': 600}))
    class Meta:
        model = Business
        fields = ['id','owner_name','name','location','address','image','image1','image2','image3','image4','image5','opening','closing','city','contact','description','category','verified']


class ServicesForm(forms.ModelForm):
    """
    for to create business
    """
    location = forms.PointField(widget = 
        forms.OSMWidget(attrs = {'map_width': 1024, 'map_height': 600}))
    class Meta:
        model = Services
        fields = ['id','owner_name','name','location','address','image','image1','image2','image3','image4','image5','city','opening','closing','category','price','description','contact','available','verified']


class HousingForm(forms.ModelForm):
    """
    Form to Create Posts
    """
    location = forms.PointField(widget = 
        forms.OSMWidget(attrs = {'map_width': 1024, 'map_height': 600}))
    class Meta:
        model = Housing
        fields = ['id','owner_name','name','image','image1','image2','image3','image4','image5','opening','closing','location','address','city','contact','description','verified']


class CommentForm(forms.ModelForm):
    """
    form t create comment
    """
    class Meta:
        model = Comments
        exclude = ['user', 'bsn','hsng','svc']
        fields = ['comment']