from django.contrib import admin
from adv.models import Services, Guards, Contact, Users

class ServiceHeading(admin.ModelAdmin):
    list_display = ('iconImage','sTitle','sDesc')
    pass

class GuardsHeading(admin.ModelAdmin):
    list_display = ('gPhoto','gName','gPos')
    pass

class ContactHeading(admin.ModelAdmin):
    list_display = ('cName','cEmail','cPhone','cMsg')
    pass

class UsersHeading(admin.ModelAdmin):
    list_display = ('uName','uEmail','uPass')
    pass

# Register your models here.
admin.site.register(Services, ServiceHeading)
admin.site.register(Guards, GuardsHeading)
admin.site.register(Contact, ContactHeading)
admin.site.register(Users, UsersHeading)

