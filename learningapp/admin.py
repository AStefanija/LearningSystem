from django.contrib import admin
from .models import Course, Enrollment, Message
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name",)
    list_filter = ("course_name", )
    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return True

    def has_add_permission(self, request):
        if not request.user.is_superuser:
            return False
        return True

admin.site.register(Course,CourseAdmin)


class EnrollmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enrollment, EnrollmentAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ("email",)
    list_filter = ("email",)
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Message,MessageAdmin)
