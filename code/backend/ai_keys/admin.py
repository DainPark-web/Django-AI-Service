from django.contrib import admin
from .models import AiKey
# Register your models here.
@admin.register(AiKey)
class AiKeyAdmin(admin.ModelAdmin):
    list_display = ('key_hash', 'user', 'is_active')
    # search_fields = ('key_hash', 'user__username')
    # list_filter = ('is_active',)
    # readonly_fields = ('key_hash', 'raw_key')
