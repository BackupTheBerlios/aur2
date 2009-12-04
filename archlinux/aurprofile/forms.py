from django.contrib.auth.models import User
from django.forms import ModelForm

from registration.forms import RegistrationFormUniqueEmail
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.contrib.auth.forms import AuthenticationForm

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

class AurRegistrationForm(RegistrationFormUniqueEmail):
    def __init__(self, *args, **kwargs):
        super(AurRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password2'].label = _("Confirm password")

class AuthenticationRememberMeForm (AuthenticationForm):

    """
    Subclass of Django ``AuthenticationForm`` which adds a remember me checkbox.

    """
    remember_me = forms.BooleanField (
        label = _( 'Remember Me' ),
        initial = False,
        required = False,
        )

