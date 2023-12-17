from django.contrib import admin
from .models import Student, Teacher, Attendance, Performance

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'student_course', 'student_group')
    search_fields = ('student_name', 'student_group')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher_name', 'teacher_kaf', 'teacher_subject')
    search_fields = ('teacher_name', 'teacher_kaf', 'teacher_subject')

class AttendanceAdmin(admin.ModelAdmin):
    def my_student_name(self, obj):
        return obj.student.student_name
    
    def my_student_group(self, obj):
        return obj.student.student_group
    
    def my_teacher_name(self, obj):
        return obj.teacher.teacher_name
    
    def my_teacher_subject(self, obj):
        return obj.teacher.teacher_subject
    
    my_student_name.short_description = 'Студент'
    my_student_group.short_description = 'Группа'
    my_teacher_name.short_description = 'Преподаватель'
    my_teacher_subject.short_description = 'Предмет'

    list_display = ('id', 'my_student_name', 'my_student_group', 'date', 'indicator', 'my_teacher_name', 'my_teacher_subject')
    search_fields = ('student__student_name', 'student__student_group', 'teacher__teacher_name', 'teacher__teacher_subject')

class PerformanceAdmin(admin.ModelAdmin):

    def my_student_name(self, obj):
        return obj.student.student_name
    
    def my_student_group(self, obj):
        return obj.student.student_group
    
    def my_teacher_name(self, obj):
        return obj.teacher.teacher_name
    
    def my_teacher_subject(self, obj):
        return obj.teacher.teacher_subject
    
    my_student_name.short_description = 'Студент'
    my_student_group.short_description = 'Группа'
    my_teacher_name.short_description = 'Преподаватель'
    my_teacher_subject.short_description = 'Предмет'

    list_display = ('id', 'my_student_name', 'my_student_group', 'date', 'mark', 'my_teacher_name', 'my_teacher_subject')
    search_fields = ('student__student_name', 'student__student_group', 'teacher__teacher_name', 'teacher__teacher_subject', 'mark')
    

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Performance, PerformanceAdmin)