from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from services.jobs import sync_jobs_with_db
from services.models import ServiceConfig
    
@receiver(post_save, sender=ServiceConfig)
def add_jobs(sender, instance, update_fields=None, **kwargs):
    if update_fields and all([field in ["last_run"] for field in list(update_fields)]):
        print(f"Changes ignored for {instance}, no relevant field changed.")
        return
    sync_jobs_with_db()
    print(f'Updated job for service: {instance.name}')
    
@receiver(post_delete, sender=ServiceConfig)
def delete_jobs(sender, instance, **kwargs):
    sync_jobs_with_db()
    print(f'Updated job for service: {instance.name}')