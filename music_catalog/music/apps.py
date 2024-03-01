from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class MusicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'music'

class Meta:
        verbose_name = _('music')