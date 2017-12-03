from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_tenants.models import TenantMixin, DomainMixin
from shared_foundation.models.abstract_thing import AbstractSharedThing
from shared_foundation import constants


class SharedOrganization(TenantMixin, AbstractSharedThing):
    class Meta:
        app_label = 'shared_foundation'
        db_table = 'mika_shared_organizations'
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')

    #
    #  SYSTEM FIELDS
    #

    created = models.DateTimeField(auto_now_add=True, db_index=True,)
    last_modified = models.DateTimeField(auto_now=True, db_index=True,)

    #
    # GENERIC FIELDS
    #

    administrators = models.ManyToManyField(
        User,
        help_text=_('The users who are office staff and administrators of this Organization.'),
        blank=True,
        related_name="%(app_label)s_%(class)s_administrators_related"
    )

    def get_tenant_url(self, url_id, url_args=None):
        """
        Function returns the full URL (with sub-domain included) of the
        resolved ID and parameters.
        """
        url = settings.INCOMEPROPERTYEVALUATOR_APP_HTTP_PROTOCOL
        url += settings.INCOMEPROPERTYEVALUATOR_APP_HTTP_DOMAIN
        url += reverse(url_id, args=url_args)
        url = url.replace("None","en")
        return url

class SharedOrganizationDomain(DomainMixin):
    class Meta:
        app_label = 'shared_foundation'
        db_table = 'at_shared_organization_domains'
        verbose_name = _('Organization Domain')
        verbose_name_plural = _('Organization Domains')

    pass
