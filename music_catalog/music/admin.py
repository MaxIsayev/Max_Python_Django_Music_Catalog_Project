from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year_released', 'number_of_songs', 'album_rating', 'owner']
    list_display_links = ['name']
    fieldsets = (
        (None, {
            "fields": (
                'name', 'owner', 'year_released',
            ),
        }),
    )

    def total_tracks(self, obj: models.Track):
        return obj.tracks.count()
    total_tracks.short_description = _('total tracks')

class TrackAdmin(admin.ModelAdmin):
    list_display = ['name', 'length', 'bitrate', 'year_released', 'genre', 'track_rating', 'audio_file', 'audio_img', 'album', 'owner']
    list_filter = ['name', 'album', 'owner']
    search_fields = ['name', 'album__name', 'owner__last_name', 'owner__username']
    readonly_fields = ['id']
    fieldsets = (
        (_("general").title(), {
            "fields": (
                ('name', 'genre', 'year_released', 'length'),
                
            ),
        }),
        (_("ownership").title(), {
            "fields": (
                ('owner', 'album'),
            ),
        }),
        (_("temporal tracking").title(), {
            "fields": (
                ('audio_file', 'audio_img', 'id'),
            ),
        }),
    )


admin.site.register(models.Album, AlbumAdmin)
admin.site.register(models.Track, TrackAdmin)