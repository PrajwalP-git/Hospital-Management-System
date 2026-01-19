from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            "id",
            "doctor",
            "patient",
            "appointment_date",
            "start_time",
            "end_time",
            "status"
        ]

    def validate(self, attrs):
        instance = self.instance or Appointment()

        for attr, value in attrs.items():
            setattr(instance,attr,value)

        instance.full_clean()
        return attrs