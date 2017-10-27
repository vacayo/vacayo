from django.contrib.gis import admin
import vacayo.models as m

class VacayoAdminSite(admin.AdminSite):
    site_header = 'Vacayo Admin'
admin_site = VacayoAdminSite(name='vacayo')

@admin.register(m.Owner, site=admin_site)
class OwnerAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">face</i>'
    ordering = ('-id', )
admin.site.register(m.Owner, OwnerAdmin)

@admin.register(m.Location, site=admin_site)
class LocationAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">weekend</i>'
    ordering = ('-id', )
admin.site.register(m.Location, LocationAdmin)

@admin.register(m.Property, site=admin_site)
class PropertyAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">weekend</i>'
    ordering = ('-id', )
admin.site.register(m.Property, PropertyAdmin)

@admin.register(m.Zip, site=admin_site)
class ZipAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">weekend</i>'
    ordering = ('-id', )
admin.site.register(m.Zip, ZipAdmin)

@admin.register(m.Host, site=admin_site)
class HostAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">face</i>'
    ordering = ('-id', )
admin.site.register(m.Host, HostAdmin)
