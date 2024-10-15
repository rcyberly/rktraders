from django.contrib import admin
from Home.models import Home
class HomeAdmin(admin.ModelAdmin):
    list_display = ('im','pname','pdesc','pprice','pquantity','pgst','pdc','Total')
admin.site.register(Home,HomeAdmin)
# Register your models here.
