from django.contrib import admin

# Register your models here.
from apps.exams.models import Student, ExamLocation, Choice, Question, Exam, Grade


class StudentAdmin(admin.ModelAdmin):
    pass


class ExamLocationAdmin(admin.ModelAdmin):
    pass


class ChoiceAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


class ExamAdmin(admin.ModelAdmin):
    pass


class GradeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)
admin.site.register(ExamLocation, ExamLocationAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Grade, GradeAdmin)

