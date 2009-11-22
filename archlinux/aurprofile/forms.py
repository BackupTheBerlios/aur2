from django.contrib.auth.models import User
from django.forms import ModelForm

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

