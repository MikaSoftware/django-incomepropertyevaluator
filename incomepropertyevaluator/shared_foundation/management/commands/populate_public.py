import os
import sys
from decimal import *
from django.db.models import Sum
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import ugettext_lazy as _
from django.core.management import call_command
from shared_foundation.models.organization import SharedOrganization
from shared_foundation.models.organization import SharedOrganizationDomain
from incomepropertyevaluator.settings import env


class Command(BaseCommand):
    help = _('Loads all the data necessary to operate this application.')

    def handle(self, *args, **options):
        #create your public tenant
        public_tenant = SharedOrganization(
            schema_name='public',
            name='incomepropertyevaluator.com',
        )
        try:
            # print("Creating Public")
            public_tenant.save()
        except Exception as e:
            print(e)

        # Add one or more domains for the tenant
        domain = SharedOrganizationDomain()
        domain.domain = env('INCOMEPROPERTYEVALUATOR_APP_HTTP_DOMAIN') # don't add your port or www here! on a local server you'll want to use localhost here
        domain.tenant = public_tenant
        domain.is_primary = True
        try:
            # print("Creating Public Domain")
            domain.save()
        except Exception as e:
            print(e)

        self.stdout.write(
            self.style.SUCCESS(_('Successfully setup public database.'))
        )

        # First call; current site fetched from database.
        from django.contrib.sites.models import Site # https://docs.djangoproject.com/en/dev/ref/contrib/sites/#caching-the-current-site-object
        current_site = Site.objects.get_current()
        current_site.domain = env('INCOMEPROPERTYEVALUATOR_APP_HTTP_DOMAIN')
        current_site.save()
