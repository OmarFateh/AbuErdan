from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from .utils import round_avg


class BaseTimestamp(models.Model):
    """
    Timestamp abstract model to be inherited from.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class WeatherManager(models.Manager):
    """
    Weather Record model manager.
    """
    def get_avg_temp(self, n=10):
        """
        Take n, and return rounded avgerage temperature of last nth records.
        """
        avg = sum(self.get_queryset().values_list('temp', flat=True)[:n]) / n
        return round_avg(avg, 2)

    def get_avg_humidity(self, n=10):
        """
        Take n, and return rounded avgerage humidity of last nth records.
        """
        avg = sum(self.get_queryset().values_list('humidity', flat=True)[:n]) / n
        return round_avg(avg, 2)

    def get_last_n_dates(self, n=10):
        """
        Take n, and return dates of the last nth records.
        """
        return self.get_queryset().values_list('created_at', flat=True)[:n]

    def set_summary_id(self, summary_id, n=10):
        """
        Take summary's id & n, and set that id to last nth records.
        """
        ids_list = self.get_queryset().values_list('pk', flat=True)[:n]
        return self.get_queryset().filter(pk__in=ids_list).update(summary_id=summary_id)


class Weather(BaseTimestamp):
    """
    Weather Record model.
    """
    temp = models.FloatField("Temperature", validators=[MinValueValidator(19.0), MaxValueValidator(28.0)])
    humidity = models.FloatField(validators=[MinValueValidator(35.0), MaxValueValidator(65.0)])
    summary_id = models.PositiveIntegerField(null=True, blank=True)

    objects = WeatherManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Weather Records'

    def __str__ (self):
        """Return weather's timestamp & temperature & humidity."""
        return f"{self.id} | {self.date} | {self.time} | T:{self.temp} | H:{self.humidity}"

    @property  
    def date(self):
        """Return a nicely formatted date string, eg: Aug 06, 2020."""
        return self.created_at.strftime("%b %d, %Y")

    @property
    def time(self):
        """Return a nicely formatted time string, eg: 07:21 PM."""
        return self.created_at.strftime("%I:%M %p") 

    def is_temp_gt_25(self):
        """Return true if temp is greater than 25"""
        return self.temp > 25.0

    def is_temp_lte_25(self):
        """Return true if temp is less than or equal 25"""
        return self.temp <= 25.0

    def is_humidity_gt_55(self):
        """Return true if humidity is greater than 55"""
        return self.humidity > 55.0

    def is_humidity_lte_55(self):
        """Return true if humidity is less than or equal 55"""
        return self.humidity <= 55.0

    def get_prev(self):
        """Return previous value of the element."""
        return self.get_previous_by_created_at()

    def is_temp_lt_prev(self):
        """Return true if temp is less than the previous value."""
        return self.temp < self.get_prev().temp 

    def is_temp_gt_prev(self):
        """Return true if temp is greater than the previous value."""
        return self.temp > self.get_prev().temp 

    def is_humidity_lt_prev(self):
        """Return true if humidity is less than the previous value."""
        return self.humidity < self.get_prev().humidity 

    def is_humidity_gt_prev(self):
        """Return true if humidity is greater than the previous value."""
        return self.humidity > self.get_prev().humidity 
           

class Summary(BaseTimestamp):
    """
    Weather Record Summary model.
    """
    avg_temp = models.FloatField("Average Temperature")
    avg_humidity = models.FloatField("Average Humidity")
    start_date = models.DateField("Date of first record of the 10 records")
    end_date = models.DateField("Date of last record of the 10 records")

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Summaries'

    def __str__ (self):
        """Return summary's start_date & end_date & avg temperature & avg humidity."""
        return f"{self.start_date} | {self.end_date} | T:{self.avg_temp} | H:{self.avg_humidity}"    

    def get_delete_absolute_url(self):
        """Return absolute url of delete subject by its id.""" 
        return reverse('weather:delete-summary', kwargs={'summary_id': self.pk})