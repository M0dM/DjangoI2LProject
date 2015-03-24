from django.contrib import admin
from .models import Question, Reponse


class ReponseInline(admin.TabularInline):
    model = Reponse


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('date', )
    date_hierarchy = 'date'
    inlines = [ReponseInline]


class ReponseAdmin(admin.ModelAdmin):
    list_display = ('question', 'texte', 'score', 'deja_vote')
    list_display_links = ('texte',)

    def deja_vote(self, obj):
        return obj.score > 0

    deja_vote.boolean = True


admin.site.register(Question, QuestionAdmin)
admin.site.register(Reponse, ReponseAdmin)
