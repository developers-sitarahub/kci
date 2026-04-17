from django.contrib import admin
from django.utils.html import format_html
from .models import Contact, CareerApplication, Property, Inquiry, InvestedProject, Newsletter

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'resume', 'display_notes', 'created_at')
    search_fields = ('name', 'email', 'phone', 'notes')
    list_filter = ('created_at',)

    def display_notes(self, obj):
        if not obj.notes:
            return "-"
        
        if len(obj.notes) <= 50:
            return obj.notes
            
        short_note = obj.notes[:50]
        return format_html(
            '<div style="max-width: 300px; word-wrap: break-word;">'
            '<span>{}</span>'
            '<span id="more-{}" style="display:none">{}</span>'
            ' <a href="javascript:void(0)" onclick="const more = document.getElementById(\'more-{}\'); if(more.style.display===\'none\') {{ more.style.display=\'inline\'; this.innerText=\' Show less\'; }} else {{ more.style.display=\'none\'; this.innerText=\' Show more\'; }}" style="color: #c2a990; font-weight: bold;"> Show more</a>'
            '</div>',
            short_note, obj.id, obj.notes[50:], obj.id
        )
    display_notes.short_description = 'Notes'

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'property_type', 'status', 'price', 'description', 'created_at')
    search_fields = ('title', 'address', 'description')
    list_filter = ('property_type', 'status', 'created_at')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'property_title', 'created_at')
    search_fields = ('name', 'email', 'phone', 'property_title', 'property_address')
    list_filter = ('created_at',)

@admin.register(InvestedProject)
class InvestedProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'description', 'created_at')
    search_fields = ('title', 'location', 'description')
    list_filter = ('created_at',)

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    list_filter = ('created_at',)
