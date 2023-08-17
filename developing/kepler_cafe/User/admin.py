from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import UserProfile, Charge

@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    @admin.display(description="Usuario", ordering="user__identification")
    def charge_name(self, obj):
        if obj.charge:
            return f"{obj.charge.name}"
        else:
            return "-"
    @admin.display(description="Fecha de creación", ordering="creation_date")
    def formated_creation_date(self, obj):
        return obj.creation_date.strftime("%d/%m/%Y %H:%M:%S")
    @admin.display(description="Fecha de inactivo", ordering="inactive_date")
    def formated_inactive_date(self, obj):
        return obj.inactive_date.strftime("%d/%m/%Y %H:%M:%S")

    list_display = (
		"pk",
		"identification",
		"first_name",
		"last_name",
		"email",
		"is_active",
		"is_staff",
		"is_superuser",
		"charge_name",
		"formated_creation_date",
		"formated_inactive_date",
		)
    search_fields = (
		'pk',
        "identification",
        'first_name',
        'last_name',
        'email'
        'charge__name'
        )
    list_filter = (
		'is_active',
		'is_staff',
		'is_superuser',
		'charge__name',
    	)

@admin.register(Charge)
class ChargeAdmin(ImportExportModelAdmin):
    list_display = (
		"pk",
		"name",
		)
    search_fields = (
		'pk',
        'name',
        )
