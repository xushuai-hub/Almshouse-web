# Create your views here.
import datetime
import json

from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, response
from rest_framework.views import APIView

from user.filter import *
from user.serializer import *


class Old_personViewSet(viewsets.ModelViewSet):
    queryset = oldperson_info.objects.all()
    serializer_class = Old_personSerializer
    filter_backends = [OldSearchFilter]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee_info.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [EmployeeSearchFilter]


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = volunteer_info.objects.all()
    serializer_class = VolunteerSerializer
    filter_backends = [VolunteerSearchFilter]


class EventViewSet(viewsets.ModelViewSet):
    queryset = event_info.objects.all()
    serializer_class = EventSerializer


class SysViewSet(viewsets.ModelViewSet):
    queryset = sys_user.objects.all()
    serializer_class = SysSerializer


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        name = request.data.get('username')
        pwd = request.data.get('password')
        user = sys_user.objects.filter(UserName=name, Password=pwd).first()
        if user:
            return HttpResponse('登录成功')
        else:
            return HttpResponse('登录失败')


class get_facenow(APIView):

    def get(self, request, *args, **kwargs):
        name = request.data.get('username')
        face_list = event_info.objects.filter(oldperson_name=name, event_type=0).last()
        print(face_list.face_list)
        # ret = EventSerializer(instance=face_list, many=False)
        ret = face_list.face_list
        return JsonResponse(ret, safe=False)


class get_face(APIView):

    def get(self, request, *args, **kwargs):
        name = request.data.get('username')
        start_time = datetime.datetime(2021, 7, 14, 0, 0, 0)
        end_time = datetime.datetime(2021, 7, 14, 7, 20, 0)
        face_list = event_info.objects.filter(oldperson_name=name, event_type=0,
                                              event_date__range=(start_time, end_time))

        ret = EventSerializer(instance=face_list, many=True)

        return JsonResponse(ret.data, safe=False)


class get_isfall(APIView):

    def get(self, request, *args, **kwargs):
        time = datetime.datetime.now().replace(microsecond=0)
        before = datetime.datetime.now() + datetime.timedelta(minutes=-1)
        face_list = event_info.objects.filter(event_type=3, event_date__range=(before, time)).last()

        if face_list:
            return HttpResponse(face_list.event_desc)
        else:
            return HttpResponse("正常")


class get_isunknow(APIView):

    def get(self, request, *args, **kwargs):
        time = datetime.datetime.now().replace(microsecond=0)
        print(time)
        before = datetime.datetime.now() + datetime.timedelta(minutes=-1)
        face_list = event_info.objects.filter(event_type=2, event_date__range=(before, time)).last()

        if face_list:
            return HttpResponse(face_list.event_desc)
        else:
            return HttpResponse("正常")
