from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save


class PatientProfile(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=30, default="")
    patient_surname = models.CharField(max_length=20, default="")
    patient_birthday = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.patient_name + " " + self.patient_surname


class ResultsModel(models.Model):
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    result_id = models.AutoField(primary_key=True)
    pregnancy = models.IntegerField(default=0, validators=[MaxValueValidator(17), MinValueValidator(0)])
    glucose = models.IntegerField(default=0, validators=[MaxValueValidator(199), MinValueValidator(0)])
    blood_p = models.IntegerField(default=0, validators=[MaxValueValidator(122), MinValueValidator(0)])
    skin = models.IntegerField(default=0, validators=[MaxValueValidator(99), MinValueValidator(0)])
    insulin = models.IntegerField(default=0, validators=[MaxValueValidator(846), MinValueValidator(0)])
    bmi = models.FloatField(default=0, validators=[MaxValueValidator(67.0), MinValueValidator(0)])
    diabetes = models.FloatField(default=0, validators=[MaxValueValidator(2.5), MinValueValidator(0)])
    age = models.IntegerField(default=0, validators=[MaxValueValidator(120), MinValueValidator(0)])

    def __str__(self):
        return self.result_id


def create_profile(sender, **kwargs):
    if kwargs['created']:
        PatientProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=PatientProfile)