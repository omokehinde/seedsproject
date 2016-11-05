from django import forms
from info.models import NameNEmail


class EmailNameForm(forms.ModelForm):

	class Meta:
		model=NameNEmail
		fields=('name','email')