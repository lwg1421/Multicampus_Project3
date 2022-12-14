from django.contrib import admin

from mysite.models import Question, Post, resultall, choice


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Post)
admin.site.register(resultall)
admin.site.register(choice)