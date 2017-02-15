from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.

class CourseLevel(models.Model):
    user = models.ForeignKey(User, default=1)
    course_title = models.CharField(max_length=200)
    course_number = models.IntegerField()
    course_description = models.TextField()

    def __str__(self):
        return self.course_title


class Subject(models.Model):
    course_level= models.ForeignKey(CourseLevel, on_delete=models.CASCADE)
    subject_title = models.CharField(max_length=250)
    subject_medium = models.CharField(max_length=10)
    subject_description = models.TextField()

    def __str__(self):
        return self.course_level.course_title + ' - ' + self.subject_title + ' { ' + self.subject_medium + '-Medium }'

class Unit(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    unit_title = models.CharField(max_length=250)
    unit_number = models.IntegerField()
    unit_description = models.TextField()

    def __str__(self):
        return self.subject.course_level.course_title + ' - ' + self.subject.subject_title + ' - ' +  str(self.unit_number) + ' - ' + self.unit_title

class question_detail(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    question_statement = models.TextField()

    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)

    EASY = 'easy'
    DIFFICULT = 'Diff'
    IMPORTANCE_LEVEL_CHOICES = (
        (EASY, 'Easy'),
        (DIFFICULT, 'Difficult'),
    )
    importance_level = models.CharField(max_length=4,
                                        choices=IMPORTANCE_LEVEL_CHOICES,
                                        default=EASY,
                                        )

    answer_choice = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )
    answer = models.IntegerField(max_length=1,
                                 choices=answer_choice,
                                 default=1,
                                 )

    def __str__(self):
        return self.question_statement