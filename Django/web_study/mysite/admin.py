from django.contrib import admin

from mysite.models import Question, Post, resultall


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Post)
admin.site.register(resultall)