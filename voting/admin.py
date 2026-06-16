from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from .models import Candidate, Vote, ElectionResult, Voter


admin.site.unregister(Group)


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):

    list_display = ['user', 'usn']

    fields = (
        'user',
        'usn',
        'photo',
    )

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'contesting_for']
    
    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):

    list_display = ['voter', 'candidate', 'voted_at']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(ElectionResult)
class ElectionResultAdmin(admin.ModelAdmin):

    list_display = (
        'status_text',
        'view_results_button',
    )

    def status_text(self, obj):
        if obj.result_declared:
            return "Election Result Status"
        return "Result Not Declared"

    status_text.short_description = "Election Result"

    def view_results_button(self, obj):
        return format_html(
            '<a href="{}" '
            'style="background:#198754;'
            'color:white;'
            'padding:8px 14px;'
            'border-radius:8px;'
            'text-decoration:none;'
            'font-weight:bold;">'
            'View Results'
            '</a>',
            '/results/'
        )

    view_results_button.short_description = "Results"


admin.site.site_header = "VoteSphere"
admin.site.site_title = "Voting Admin"
admin.site.index_title = "Election Dashboard"