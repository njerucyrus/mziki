from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline

from music.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}
    class Meta:
        model = Category
admin.site.register(Category,CategoryAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display =['song_title','artist','category','song_type','song_url','download_point','date_released']
    prepopulated_fields = {'slug': ('song_title',)}
    class Meta:
        model=Song
admin.site.register(Song,SongAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','stage_name','phone_no','email','slug']
    prepopulated_fields = {'slug': ('stage_name', )}
    class Meta:
        model = Artist
admin.site.register(Artist,ArtistAdmin)

class AirtimeTopUpAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_no', 'amount','point_earned','transaction_date']
    class Meta:
        model = AirtimeTopUp
admin.site.register(AirtimeTopUp, AirtimeTopUpAdmin)

class Hits254AcAdmin(admin.ModelAdmin):
    list_display = ['phone_no', 'point_earned', 'date_update']
    class Meta:
        model = Hits254Ac
admin.site.register(Hits254Ac, Hits254AcAdmin)

class UserAccountAdmin(admin.ModelAdmin):
     list_display = ['FirstName', 'LastName', 'phone_no']
     class Meta:
         model = UserAccount
admin.site.register(UserAccount, UserAccountAdmin)

class RatesAdmin(admin.ModelAdmin):
    list_display = ['amount', 'points']
    class Meta:
        model = Rates
admin.site.register(Rates, RatesAdmin)
