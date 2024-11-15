from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Inline model for lessons in course view
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Inline model for choices in question view
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

# Inline model for questions in course view
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# Admin customization for Course model
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Admin customization for Question model
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']

# Admin customization for Lesson model
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Register models with the admin site
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
