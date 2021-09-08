from django.dispatch import receiver
from django.db.models import Avg
from django.db.models.signals import post_save, pre_delete

from .models import Weather, Summary


@receiver(post_save, sender=Weather)     
def create_summary_record(sender, instance, created, **kwargs):
    """
    Create summary record of weather data once the 10th weather record is created.
    """
    if created:
        if Weather.objects.count() % 10 == 0:
            avg_temp = Weather.objects.get_avg_temp(n=10)
            avg_humidity = Weather.objects.get_avg_humidity(n=10)
            dates = Weather.objects.get_last_n_dates(n=10)
            summary_obj = Summary.objects.create(avg_temp=avg_temp, avg_humidity=avg_humidity,
                                            start_date=dates[9].date(), end_date=dates[0].date())
            Weather.objects.set_summary_id(summary_id=summary_obj.id, n=10)


@receiver(pre_delete, sender=Summary)
def delete_related_weather_records(sender, instance, using, **kwargs):
    """
    Delete all related weather records to the summary instance. 
    """
    weather_qs = Weather.objects.filter(summary_id=instance.id)
    for obj in weather_qs:
        obj.delete()