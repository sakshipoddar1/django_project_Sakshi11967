from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import *
from .SAKSHIPODDAR_serliazers import *

class SAKSHIPODDAR_lmsSignupUser(APIView):
    def post(self,request):
        userdata = SAKSHIPODDAR_lmsSignupSerliazer(data=request.data)
        if userdata.is_valid():
            SAKSHIPODDAR_lmsUser.objects.create(**userdata.data)
            message = {"message": "User created Successfully"}
            return JsonResponse(message,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(userdata.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class SAKSHIPODDAR_lmsGetUserDetails(APIView):
    def get(self,request):
        result = list(SAKSHIPODDAR_lmsUser.objects.filter().values())
        return JsonResponse(result,status=status.HTTP_200_OK,safe=False)

class SAKSHIPODDAR_lmsUpdateEmail(APIView):
    def put(self,request):
        userdata = SAKSHIPODDAR_lmsUpdateEmailSerliazer(data=request.data)
        if userdata.is_valid():
            email = userdata.data["email"]
            number = userdata.data["number"]
            SAKSHIPODDAR_lmsUser.objects.filter(number=number).update(email=email)
            message = {"message": "email updated successfully"}
            return JsonResponse(message,status=status.HTTP_200_OK)
        return JsonResponse(userdata.errors,status=status.HTTP_400_BAD_REQUEST)

class SAKSHIPODDAR_lmsDeleteUser(APIView):
    def delete(self,request,number):
        SAKSHIPODDAR_lmsUser.objects.filter(number=number).delete()
        message = {"message": "user deleted successfully"}
        return JsonResponse(message, status=status.HTTP_204_NO_CONTENT)