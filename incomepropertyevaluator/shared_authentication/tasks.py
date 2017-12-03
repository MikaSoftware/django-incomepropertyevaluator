from rq import get_current_job
from django_rq import job
from django.core.management import call_command


@job
def send_user_activation_email_func(email):
    call_command('send_user_activation_email', email, verbosity=0, interactive=False)


@job
def create_tenant_organization_func(data_dict):
    call_command(
        'create_tenant_organization',
        data_dict['user_pk'],
        data_dict['schema_name'],
        data_dict['name'],
        data_dict['alternate_name'],
        verbosity=0,
        interactive=False)
