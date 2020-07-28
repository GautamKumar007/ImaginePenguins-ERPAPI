from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):

    # password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs ={
            'password': {'write_only':True}
        }

    def save(self):
        register = User(username=self.validated_data['username'],
                        email=self.validated_data['email'],
                    )
        password = self.validated_data['password']
        register.set_password(password)
        register.save()
        return register
