from django.contrib import admin
import vacayo.models as m

class VacayoAdminSite(admin.AdminSite):
    site_header = 'Vacayo Admin'
admin_site = VacayoAdminSite(name='vacayo')

@admin.register(m.Owner, site=admin_site)
class OwnerAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">face</i>'
    ordering = ('-id', )
admin.site.register(m.Owner, OwnerAdmin)

@admin.register(m.Property, site=admin_site)
class PropertyAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">weekend</i>'
    ordering = ('-id', )
admin.site.register(m.Property, PropertyAdmin)