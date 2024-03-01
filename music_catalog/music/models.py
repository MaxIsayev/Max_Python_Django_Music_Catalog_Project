from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.


class Album(models.Model):
    name = models.CharField(_("name"), max_length=100, db_index=True) 
    year_released = models.IntegerField(_("year released"), blank=True)
    number_of_songs = models.IntegerField(_("number of songs"), blank=True)
    album_rating = models.IntegerField(_("album rating"), blank=True)
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        verbose_name=_("owner"), 
        related_name='albums',
    )    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("album")
        verbose_name_plural = _("albums")
        ordering = ['name']

    def get_absolute_url(self):
        return reverse("album_detail", kwargs={"pk": self.pk})


class Track(models.Model):
    name = models.CharField(_("name"), max_length=100, db_index=True)
    length = models.TimeField(_("length"), blank=True)
    bitrate = models.IntegerField(_("bitrate"), blank=True)
    year_released = models.IntegerField(_("year released"), blank=True)
    genre = models.CharField(_("genre"), max_length=100, blank=True)
    track_rating = models.IntegerField(_("track rating"), blank=True)
    audio_file = models.FileField(_("audio"), upload_to='audio/', blank=True, null=True)
    audio_img = models.ImageField(_("audio picture"), upload_to='audio_img/', blank=True, null=True)  
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE, 
        verbose_name=_("album"), 
        related_name='tracks',
    )
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        verbose_name=_("owner"), 
        related_name='tracks',
    )
   
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("track")
        verbose_name_plural = _("tracks")
        ordering = ['name']

    def get_absolute_url(self):
        return reverse("track_detail", kwargs={"pk": self.pk})
