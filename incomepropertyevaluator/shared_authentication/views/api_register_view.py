import django_filters
import django_rq
from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from django_filters import rest_framework as filters
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework import mixins # See: http://www.django-rest-framework.org/api-guide/generic-views/#mixins
from rest_framework import authentication, viewsets, permissions, status, parsers, renderers
from rest_framework.decorators import detail_route, list_route # See: http://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
from rest_framework.response import Response
from shared_foundation import models
from shared_foundation import utils
from shared_authentication.serializers.register_serializers import RegisterUserSerializer
from shared_authentication.tasks import (
    send_user_activation_email_func,
    create_tenant_organization_func
)


class RegisterAPIView(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        # Perform validation.
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Attempt to create a user and return status.
        try:
            print("1")
            user = User.objects.create(
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                email=serializer.validated_data['email'],
                username=utils.get_unique_username_from_email(serializer.validated_data['email']),
                is_active=False
            )

            print("2")

            profile = models.SharedProfile.objects.create(
                user=user
            )

            print("3")

            # Generate and assign the password.
            user.set_password(serializer.validated_data['password'])
            user.save()

            print("4")

            # Generate the private access key.
            Token.objects.create(user=user)

            print("5")

            # Create our tenant organization.
            django_rq.enqueue(
                create_tenant_organization_func,
                {
                    'user_pk': user.id,
                    'schema_name': serializer.validated_data['company_schema_name'],
                    'name': serializer.validated_data['company_name'],
                    'alternate_name': serializer.validated_data['company_alternate_name']
                }
            )

            print("6")

            # Send an email.
            django_rq.enqueue(send_user_activation_email_func, user.email)

            print("7")

            # Implemented response.
            return Response({
                'status': 'Registered',
                'reason': ''
            })
        except Exception as e:
            return Response({
                'status': 'Failed',
                'reason': str(e)
            })
