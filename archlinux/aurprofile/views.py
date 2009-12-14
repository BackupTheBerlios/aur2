from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from aurprofile.forms import ProfileUpdateForm
from aur.models import Package

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.views.decorators.cache import never_cache
from aurprofile.forms import AuthenticationRememberMeForm

from django.views.generic.list_detail import object_detail


@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404

    packages = Package.objects.filter(maintainers=user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = ProfileUpdateForm(instance=user)
    count_packages_ood = packages.filter(outdated=True).count()
    context = RequestContext(request, {
        'packages': packages,
        'form': form,
        'packages_out_of_date': count_packages_ood,
    })
    return render_to_response('aurprofile/profile.html', context)

def remember_me_login(
    request,
    template_name = 'registration/login.html',
    redirect_field_name = REDIRECT_FIELD_NAME,
    form_class = AuthenticationRememberMeForm,
    ):

    """
    Based on code cribbed from django/trunk/django/contrib/auth/views.py

    Displays the login form with a remember me checkbox and handles the login
    action.

    """

    from django.conf import settings
    from django.contrib.sites.models import RequestSite, Site
    from django.http import HttpResponseRedirect
    from django.shortcuts import render_to_response
    from django.template import RequestContext
    from django.views.generic.simple import redirect_to
    from django.core.urlresolvers import reverse

    if request.user.is_authenticated( ):
        return redirect_to(request, reverse("aur-main"))

    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = AuthenticationRememberMeForm(data = request.POST,)
        if form.is_valid():
            # Light security check -- make sure redirect_to isn't garbage.
            if not redirect_to or '//' in redirect_to or ' ' in redirect_to:
                redirect_to = settings.LOGIN_REDIRECT_URL
            if not form.cleaned_data [ 'remember_me' ]:
                request.session.set_expiry(31536000)
            from django.contrib.auth import login
            login (request, form.get_user())
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return HttpResponseRedirect(redirect_to)
    else:
        form = form_class(request,)
    request.session.set_test_cookie()
    if Site._meta.installed:
        current_site = Site.objects.get_current()
    else:
        current_site = RequestSite(request)

    return render_to_response(
            template_name,
            {
                'form': form,
                redirect_field_name: redirect_to,
                'site': current_site,
                'site_name': current_site.name,
                },
            context_instance = RequestContext(request),
            )
remember_me_login = never_cache(remember_me_login)
