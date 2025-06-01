import threading
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import DummyModel

@receiver(post_save, sender=DummyModel)
def signal_handler(sender, instance, **kwargs):
    print(f"Signal handler: running in thread: {threading.current_thread().name}")
    print(f"Signal handler: in transaction? {transaction.get_connection().in_atomic_block}")
    print("Signal handler: starting...")
    time.sleep(3)
    print("Signal handler: completed.")
