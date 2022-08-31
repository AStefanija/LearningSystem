from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.TextField()
    cover_image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
    lectures = models.FileField(upload_to="cover_images/")
    students = models.ManyToManyField(User, through='Enrollment', related_name="student_course")

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    course = models.ForeignKey(Course, related_name="enrollments", on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name="user_courses", on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username


class Message(models.Model):
    email = models.TextField()
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.email