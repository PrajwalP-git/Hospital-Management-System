from rest_framework.viewsets import ModelViewSet
from .models import Appointment
from .serializers import AppointmentSerializer
from .permissions import IsStaffOrDoctor

# Create your views here.

class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsStaffOrDoctor]
