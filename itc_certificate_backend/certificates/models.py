from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True, db_column='StudentId')
    first_name = models.CharField(max_length=150, db_column='FirstName', blank=True, null=True)
    middle_name = models.CharField(max_length=150, db_column='MiddleName', blank=True, null=True)
    last_name = models.CharField(max_length=150, db_column='LastName', blank=True, null=True)
    mobile = models.CharField(max_length=25, db_column='StudentMobile', blank=True, null=True)

    @property
    def full_name(self):
        parts = [
            (self.first_name or '').strip(),
            (self.middle_name or '').strip(),
            (self.last_name or '').strip(),
        ]
        return ' '.join(p for p in parts if p)

    def __str__(self):
        return f"{str(self.student_id).strip()} - {self.full_name}"

    class Meta:
        managed = False
        db_table = 'a_StudentMaster'