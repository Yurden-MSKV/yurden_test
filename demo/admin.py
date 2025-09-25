from django.contrib import admin

from demo.models import Post, Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]