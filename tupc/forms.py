from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import OrganizationInfo, OfficersInfo, ActivitiesInfo, ReportsInfo


class SignUpUser(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name' ]
        # or 'modelFieldName','modelFieldName'


class OrgInfoForm(forms.ModelForm):
	class Meta:
		model = OrganizationInfo
		fields = "__all__"
        # or 'modelFieldName','modelFieldName'

class OfficersInfoForm(forms.ModelForm):
	class Meta:
		model = OfficersInfo
		fields = "__all__"
        # or 'modelFieldName','modelFieldName'

class ActivitiesInfoForm(forms.ModelForm):
	class Meta:
		model = ActivitiesInfo
		fields = ['OrganizationName', 'activity', 'budget', 'target', 'number', 'officers', 'faculty', 'description']
        # or 'modelFieldName','modelFieldName'


class ReportsInfoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ReportsInfoForm, self).__init__(*args, **kwargs)

		self.fields['date'].widget.attrs.update(
			{'placeholder': 'yyyy-mm-dd'}
		)
	class Meta:
		model = ReportsInfo
		fields = ['OrganizationName', 'date', 'statuE', 'file_link']
