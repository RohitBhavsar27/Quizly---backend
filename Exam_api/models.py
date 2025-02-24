from django.db import models


# Create your models here.
class Users(models.Model):
    fname = models.CharField(max_length=40, default="")
    lname = models.CharField(max_length=40, default="")
    emailId = models.CharField(max_length=100)
    username = models.CharField(max_length=40, primary_key=True)
    password = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.username},{self.password},{self.mobNo},{self.emailId}"

    class Meta:
        db_table = "users"


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    qno = models.IntegerField()
    qtext = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)
    op1 = models.CharField(max_length=150)
    op2 = models.CharField(max_length=150)
    op3 = models.CharField(max_length=150)
    op4 = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.qno},{self.qtext},{self.answer},{self.op1},{self.op2},{self.op3},{self.op4},{self.subject}"

    class Meta:
        db_table = "questions"
        unique_together = (("qno", "subject"),)


class Admin(models.Model):
    username = models.CharField(max_length=40, primary_key=True)
    password = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.username},{self.password}"

    class Meta:
        db_table = "admin"


class Results(models.Model):
    username = models.CharField(max_length=40, primary_key=True)
    subject = models.CharField(max_length=40)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.username},{self.subject},{self.score}"

    class Meta:
        db_table = "results"
