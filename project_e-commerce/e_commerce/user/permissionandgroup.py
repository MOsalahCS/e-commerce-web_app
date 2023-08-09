from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'name', 'is_active', 'is_staff','is_superuser','display_groups', 'display_user_permissions']
    list_filter = ['is_superuser', 'is_active', 'is_staff']
    search_fields = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser',)}
        ),
    )
    filter_horizontal = ['groups', 'user_permissions']
    def display_groups(self, obj):
        return ', '.join(group.name for group in obj.groups.all())
    display_groups.short_description = 'Groups'

    def display_user_permissions(self, obj):
        return ', '.join(permission.codename for permission in obj.user_permissions.all())
    display_user_permissions.short_description = 'User Permissions'
