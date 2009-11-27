from django.contrib.auth.models import User
from django.forms import ModelForm

from registration.forms import RegistrationFormUniqueEmail
from django.utils.translation import ugettext_lazy as _

attrs_dict = { 'class': 'required' }

class ProfileUpdateForm(ModelForm):
    """
    Some explanation for ProfileUpdateForm.

    >>> form = ProfileUpdateForm( )
    >>> form
    u"some output"
    >>> form.somemethod( )
    u"more output"
    """
    class Meta:
        """
        contains metadata about this class.
        """
        def __init__( self ):
            raise Exception( "Shouldn't be instanciated" )

        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class AurRegistrationForm( RegistrationFormUniqueEmail ):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
        render_value=False),  label=_( "Confirm password" )
