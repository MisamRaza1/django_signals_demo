from django.shortcuts import render

# Create your views here.
from django.db import transaction
from .models import DummyModel
import threading

def create_model_instance():
    print(f"Main thread: {threading.current_thread().name}")
    with transaction.atomic():
        DummyModel.objects.create(name="Test Signal")
