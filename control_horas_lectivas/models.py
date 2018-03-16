from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Regime(models.Model):
    name = models.CharField(max_length=100)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    address_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    regime = models.ForeignKey(Regime, on_delete=models.CASCADE)


class School(models.Model):
    name = models.CharField(max_length=100)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)


class StudyPlan(models.Model):
    year = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class HourType(models.Model):
    name = models.CharField(max_length=100)


class Course(models.Model):
    name = models.CharField(max_length=100)
    credit = models.IntegerField()
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)


class TeacherXCourse(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Hour(models.Model):
    quantity = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    hour_type = models.ForeignKey(HourType, on_delete=models.CASCADE)


class HourActivity(models.Model):
    quantity = models.IntegerField()
    hour_type = models.ForeignKey(HourType, on_delete=models.CASCADE)


class Day(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)


class SemesterNumber(models.Model):
    name = models.CharField(max_length=100)


class SemesterType(models.Model):
    name = models.CharField(max_length=100)
