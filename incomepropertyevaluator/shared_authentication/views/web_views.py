# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from shared_foundation import models
from shared_foundation import utils


def register_master_page(request):
    return render(request, 'shared_authentication/register/master_view.html',{})


def register_detail_page(request):
    return render(request, 'shared_authentication/register/detail_view.html',{})


def user_activation_detail_page(request, pr_access_code):
    try:
        profile = models.SharedProfile.objects.get(pr_access_code=pr_access_code)

        if profile.has_pr_code_expired():
            raise PermissionDenied(_('Access code expired.'))
        else:
            # Activate our account.
            profile.user.is_active = True
            profile.user.save()

            # Load our view.
            return render(request, 'shared_authentication/activate_user/detail_view.html',{})

    except models.SharedProfile.DoesNotExist:
        raise PermissionDenied(_('Wrong access code.'))


def user_login_master_page(request):
    return render(request, 'shared_authentication/login_user/master_view.html',{})

@login_required(login_url='/sign-in')
def user_login_redirect(request):
    #TODO: IMPLEMENT LOGIN REDIRECTOR TO TENANT DASHBOARD.
    return render(request, 'shared_authentication/login_user/master_view.html',{})
    return HttpResponseRedirect(reverse('mika_tenant_dashboard_master'))
