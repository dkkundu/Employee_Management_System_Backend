"""API > views > profile.py"""
# PYTHON IMPORTS
import logging
from sys import _getframe
# DRF IMPORTS
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# CORE IMPORTS
from Core.models import Profile
from django.contrib.auth import get_user_model
# API IMPORTS
from API.serializers import (
    ImageSerializer,  ProfileListSerializer, ProfileSerializer,
    ProfileCreateSerializer, ProfileUpdateSerializer
)
logger = logging.getLogger(__name__)
USER_MODEL = get_user_model()


class ImageUploadAPI(generics.RetrieveUpdateAPIView):
    """Retrieves and/or Updates the Image field in the Profile Model"""
    queryset = Profile.objects.all()
    serializer_class = ImageSerializer
    # authentication_classes = ()  # check defaults in settings
    # permission_classes = ()  # check defaults in settings

    def retrieve(self, request, *args, **kwargs):
        """overriding to enable logging"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Retrieving profile: "
            f"{self.lookup_field}={kwargs[self.lookup_field]}"
        )
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """overriding to enable logging"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Updating profile: "
            f"{self.lookup_field}={kwargs[self.lookup_field]}"
        )
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """overriding to enable logging"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Partial update profile: "
            f"{self.lookup_field}={kwargs[self.lookup_field]}"
        )
        return super().partial_update(request, *args, **kwargs)


class EmployeeProfileView(APIView):
    model = Profile
    serializer_class = ProfileSerializer

    def get(self, request, pk, *args, **kwargs):
        profile = self.model.objects.get(pk=pk)
        serializer = self.serializer_class(profile)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EmployeeListView(APIView):
    model = Profile
    serializer_class = ProfileListSerializer

    def get(self, request, *args, **kwargs):
        profile = []
        for obj in self.model.objects.all():
            profile_dir = {
                "pk": obj.pk,
                "name": obj.pk,
                "image": obj.image if obj.image else None,
                "designation": obj.designation,
                "bio": obj.bio
            }
            profile.append(profile_dir)
        serializer_dir = {
            "data": profile
        }

        serializer = self.serializer_class(serializer_dir)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EmployeeProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    http_method_names = ['patch', ]

    def update(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class EmployeeCreateView(APIView):
    model = Profile
    serializer_class = ProfileCreateSerializer

    def post(self, request, format=None):
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        message = "Data not found"
        profile_dir = {}
        user_name = request.data.get('username')
        password = request.data.get('password')
        password2 = request.data.get('password2')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        nickname = request.data.get('nickname')
        designation = request.data.get('designation')
        id_number = request.data.get('id_number')
        phone = request.data.get('phone')
        image = request.data.get('image')
        bio = request.data.get('bio')
        birthday = request.data.get('birthday')
        gender = request.data.get('gender')
        if password2 == password:
            user = USER_MODEL.objects.create(
                username=user_name
            )
            user.set_password(password)
            user.email = email
            user.save()
        else:
            user = None

        if user:
            try:
                profile = Profile.objects.get(pk=user.pk)
                profile.first_name = first_name
                profile.last_name = last_name
                profile.nickname = nickname
                profile.designation = designation
                profile.id_number = id_number
                profile.phone = phone
                profile.image = image
                profile.bio = bio
                profile.birthday = birthday
                profile.gender = gender
            except Exception as e:
                profile = None
                logger.info(f"File update fail {e}")

            profile_dir = {
                'user': user,
                'name': profile.full_name() if profile else "",
                'designation': profile.designation if profile else "",
                'phone': profile.phone if profile else ""
            }
            status_code = status.HTTP_200_OK
            message = "Successfully Created"

        data = {
            "status": status_code,
            "message": message,
            "data": profile_dir
        }
        return Response(data=data, status=status_code)

