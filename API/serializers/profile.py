"""API > serializers > profile.py"""
from django.contrib.auth import get_user_model
# DRF IMPORTS
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# CORE IMPORTS
from Core.models import Profile
USER_MODEL = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for One-to-One Profile model"""
    class Meta:
        """Meta class"""
        model = Profile
        fields = '__all__'
        read_only_fields = ('user', 'is_active', )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    """Serializer for One-to-One Profile model"""
    class Meta:
        """Meta class"""
        model = Profile
        fields = [
            'first_name', 'last_name', 'nickname', 'id_number',
            'father_name', 'mother_name', 'nid', 'passport',
            'phone', 'image', 'signature', 'bio', 'birthday', 'gender',
            'blood_group', 'joining_date', 'website', 'spouse_name',
            'designation', 'present_division', 'present_district',
            'present_upazila', 'present_post_code', 'present_address',
            'same_as_present_address', 'permanent_division',
            'permanent_district', 'permanent_upazila', 'permanent_post_code',
            'permanent_address'
        ]


class ProfileCreateSerializer(serializers.Serializer):
   username = serializers.CharField(
       max_length=55,
       validators=[UniqueValidator(queryset=USER_MODEL.objects.all())],
       required=True
   )
   password = serializers.CharField(
       max_length=55, write_only=True, required=True
   )
   password2 = serializers.CharField(
       max_length=55, write_only=True, required=True
   )
   email = serializers.EmailField()
   first_name = serializers.CharField(max_length=255)
   last_name = serializers.CharField(max_length=255)
   nickname = serializers.CharField(max_length=255)
   designation = serializers.CharField(max_length=255)
   id_number = serializers.CharField(max_length=30)
   phone = serializers.CharField(max_length=12)
   image = serializers.ImageField()
   bio = serializers.CharField(max_length=900)
   birthday = serializers.DateField()
   gender = serializers.CharField(max_length=1)


class ProfileListSerializer(serializers.Serializer):
    """Serializer for One-to-One Profile model"""
    data = serializers.ListField()


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for the Image field in the Profile model"""
    class Meta:
        """Meta class"""
        model = Profile
        fields = ('image', )
