from django.contrib import admin
from .views import mail_sender
from .models import Link, Sublink, About, Event, Announcement, Member, Blog, Team, Subscribe, Contact, Message, Sponsor, MemberYear

class LinkAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "position")

class SublinkAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "is_active", "position")

class AboutAdmin(admin.ModelAdmin):
    list_display = ("name", "text")

class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "is_active")

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "text")

class TeamAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

class MemberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "title", "team")

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('views_count', 'likes_count')
    list_display = ("title", "writer", "is_published")

class ContactAdmin(admin.ModelAdmin):
    list_display = ("user_name", "subject", "user_email")

@admin.action(description="Send email to all subscribers")
def send_email_to_subscribers(modeladmin, request, queryset):
    mail_sender()
    modeladmin.message_user(request, "Emails sent successfully!")

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("mail",)  
    actions = [send_email_to_subscribers] 


admin.site.register(Link, LinkAdmin)
admin.site.register(Sublink, SublinkAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Subscribe, SubscribeAdmin)  
admin.site.register(Contact, ContactAdmin)
admin.site.register(Message)
admin.site.register(Sponsor)
admin.site.register(MemberYear)
