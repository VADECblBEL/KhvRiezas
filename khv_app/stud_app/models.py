from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from datetime import datetime

class Student(models.Model):
    """Студенты"""

    class Meta:
        db_table = "students"
        verbose_name = "Информация о студенте"
        verbose_name_plural = "Информация о студентах"
    
    student_name = models.TextField(verbose_name="Студент")
    student_course = models.TextField(verbose_name="Курс студента")
    student_group = models.TextField(verbose_name="Группа студента")

    def __str__(self):
        return f"{self.student_name} {self.student_group}"

class Teacher(models.Model):
    """Преподаватели"""

    class Meta:
        db_table = "teachers"
        verbose_name = "Информация о преподавателе"
        verbose_name_plural = "Информация о преподавателях"

    teacher_name = models.TextField(verbose_name="Преподаватель")
    teacher_kaf = models.TextField(verbose_name="Кафедра преподавателя")
    teacher_subject = models.TextField(verbose_name="Предмет преподавателя")

    def __str__(self):
        return f"{self.teacher_name} {self.teacher_subject}"

class Attendance(models.Model):
    """Посещаемость"""

    class Meta:
        db_table = "attendance"
        verbose_name = "Посещения студента"
        verbose_name_plural = "Посещения студентов"
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель")
    date = models.DateField(verbose_name="Дата занятия")
    indicator = models.BooleanField(verbose_name="Посещение")

    def __str__(self):
        return f"{self.student} {self.date} {self.indicator} {self.teacher}"

def mark_validator(mark):
    if mark not in [0, 2, 3, 4, 5]:
        raise ValidationError(
            gettext_lazy('%(mark)i is wrong mark'),
            params={'mark':mark}
        )

class Performance(models.Model):
    """Успеваемость"""

    class Meta:
        db_table = "performance"
        verbose_name = "Успеваемость студента"
        verbose_name_plural = "Успеваемость студентов"

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель")
    date = models.DateField(verbose_name="Дата занятия")
    mark = models.IntegerField(verbose_name="Оценка",validators=[mark_validator])

    def __str__(self):
        return f"{self.student} {self.date} {self.mark} {self.teacher}"
