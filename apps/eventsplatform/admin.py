from django.contrib import admin
from .models import Event, Ticket, Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'organizer', 'category')
    list_filter = ('date', 'category')
    search_fields = ('title', 'description')
    autocomplete_fields = ['organizer', 'category']
    date_hierarchy = 'date'

class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'purchase_date', 'is_checked_in')
    list_filter = ('is_checked_in', 'purchase_date')
    search_fields = ('user__username', 'event__title')
    autocomplete_fields = ['user', 'event']
    readonly_fields = ('qr_code', 'purchase_date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
