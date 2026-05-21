

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from.models import Bug
from.serializers import BugSerializer
from django_filters.rest_framework import DjangoFilterBackend

def bug_list(request):
  bugs=Bug.objects.all()
  return render(request, 'bugs/bug_list.html', {'bugs': bugs})


class BugViewSet(viewsets.ModelViewSet):
    queryset = Bug.objects.all().order_by('-created_at')
    serializer_class = BugSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
