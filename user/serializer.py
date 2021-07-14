from rest_framework import serializers

from user.models import oldperson_info, employee_info, volunteer_info, event_info, sys_user


class Old_personSerializer(serializers.ModelSerializer):
    class Meta:
        model = oldperson_info
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_info
        fields = '__all__'


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = volunteer_info
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event_info
        fields = '__all__'


class SysSerializer(serializers.ModelSerializer):
    class Meta:
        model = sys_user
        fields = '__all__'