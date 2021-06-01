from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


def image_preview(obj):
    return format_html(
        '<img src="{url}" style="max-height: 200px; max-width: 200px;" />'.format(
            url=obj.img.url
        )
    )


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = [image_preview]
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = [image_preview]
    autocomplete_fields = ['place']
