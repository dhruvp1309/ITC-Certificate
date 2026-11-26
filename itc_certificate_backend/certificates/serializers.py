from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='full_name', read_only=True)

    class Meta:
        model = Student
        fields = [
            'student_id',
            'name',
            'first_name',
            'middle_name',
            'last_name',
            'mobile',
        ]


class StudentLookupSerializer(serializers.Serializer):
    student_id = serializers.CharField(max_length=50)


class OTPRequestSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=25)


class OTPVerifySerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=25)
    otp_code = serializers.CharField(max_length=6)