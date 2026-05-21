from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Bug

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        if change and 'password' in form.changed_data:
            obj.save()  # This invalidates other sessions
        super().save_model(request, obj, form, change)


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at']  # columns you see
    list_filter = ['status']  # adds filter sidebar
    search_fields = ['title', 'description']  # adds search box