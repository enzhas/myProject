from rest_framework import serializers

from .models import CostomUser

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length = 150, read_only=True)
    password = serializers.CharField(max_length = 128, read_only=True)
    first_name = serializers.CharField(max_length = 150)
    last_name = serializers.CharField(max_length = 150)
    date_joined = serializers.DateTimeField(read_only=True)
    email = serializers.CharField(max_length = 254)
    role = serializers.CharField(max_length = 255, default="", read_only=True)
    profile_pic = serializers.ImageField(read_only=True)
    bio = serializers.CharField(default="", read_only=True)
    user_qr = serializers.ImageField(read_only=True)
    is_active = serializers.BooleanField(read_only=True, default=1)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.role = validated_data.get("role", instance.role)
        instance.bio = validated_data.get("bio", instance.bio)

        instance.save()
        return instance

# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CostomUser
#         fields = ['email', 'username', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop("password")
#         user = User(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user 
        