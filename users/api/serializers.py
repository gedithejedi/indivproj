from rest_framework import serializers
from users.models import Account

class RegistrationSerializer(serializers.ModelSerializer):
    passwordrep = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields =     ['email','username', 'password', 'passwordrep']
        extra_kwargs = {
                'password': {'write_only': True}
        }

    def save(self):
        account = Account(
                    email=self.validated_data['email'],
                    username=self.validated_data['username'],
            )
        password = self.validated_data['password']
        passwordrep = self.validated_data['passwordrep']

        if password != passwordrep:
            raise serializers.ValidationError({'password': 'Passwords must match!!!!!!!'})
        account.set_password(password)
        account.save()
        return account