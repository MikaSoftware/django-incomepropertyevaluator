# -*- coding: utf-8 -*-
import datetime
from django import template
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
from shared_foundation import constants


register = template.Library()


@register.simple_tag
def get_app_domain():
    """
    Returns the full URL to the domain. The output from this function gets
    generally appended with a path string.
    """
    url = settings.INCOMEPROPERTYEVALUATOR_APP_HTTP_PROTOCOL
    url += settings.INCOMEPROPERTYEVALUATOR_APP_HTTP_DOMAIN
    return url


@register.simple_tag
def tenant_url(schema_name, view_name):
    if schema_name:
        return settings.INCOMEPROPERTYEVALUATOR_APP_HTTP_PROTOCOL + schema_name + '.%s' % settings.INCOMEPROPERTYEVALUATOR_APP_HTTP_DOMAIN + reverse(view_name)
    else:
        return settings.INCOMEPROPERTYEVALUATOR_APP_HTTP_PROTOCOL + '%s' % settings.INCOMEPROPERTYEVALUATOR_APP_HTTP_DOMAIN + reverse(view_name)
