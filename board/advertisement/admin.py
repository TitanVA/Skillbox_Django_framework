from django.contrib import admin

from advertisement.models import *


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.author = request.user
    #
    #     super(AdvertisementAdmin, self).save_model(
    #         request=request,
    #         obj=obj,
    #         form=form,
    #         change=change
    #     )
    list_display = ["id", "title", "category"]
    list_filter = ["category"]
    search_fields = ["title", "description", "category"]

@admin.register(AdvertisementStatus)
class AdvertisementStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(AdvertisementRegion)
class AdvertisementRegionAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementType)
class AdvertisementTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementCategory)
class AdvertisementCategoryAdmin(admin.ModelAdmin):
    pass