"""
Serilizers for API View
https://www.django-rest-framework.org/tutorial/1-serialization/

"""

from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Json input -> validate it -> convert into python object
    https://www.django-rest-framework.org/api-guide/fields/
    """
    # user = serializers.SerializerMethodField()
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {
            'password' : {
                'write_only': True,
                'min_length': 5
            }
        }

        def create(self, validated_data):
            """
            Create and return user with encrypted pw.
            To be called after validation.
            """
            return get_user_model().objects.create_user(**validated_data)