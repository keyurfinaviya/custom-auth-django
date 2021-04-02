
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from api.customauth import CustomAuthentication

from rest_framework.permissions import IsAuthenticated



class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	authentication_class=[CustomAuthentication]
	permission_classes=[IsAuthenticated]