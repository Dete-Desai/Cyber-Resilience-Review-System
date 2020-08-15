from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.

# CSE FORM
CSE_FORM_RESPONSE_CHOICES = (
    ('am1', 'Asset Management'),
    ('cm2', 'Controls Management'), 
    ('ccm3', 'Control Change Management'), 
    ('vm4', 'Vulnerability Management'), 
    ('im5', 'Incident Management'), 
    ('scm6', 'Service Continuity Management'), 
    ('rm7', 'Risk Management'), 
    ('edm8', 'External Dependancies Management'), 
    ('ta9', 'Training Awareness'),
    ('sa10', 'Situational Awareness')
)
class cseformdb(models.Model):
    expertid = models.CharField(primary_key=True, max_length=50)
    formdomainlevel = models.CharField(max_length=100, choices=CSE_FORM_RESPONSE_CHOICES, default='am1')

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formdomainlevel)
        #return self.expertid




AMG2_FORM_ID_CHOICES = (
    ('amg2', 'AMG 2'),
)

AMG3_FORM_ID_CHOICES = (
    ('amg3', 'AMG 3'),
)

AMG4_FORM_ID_CHOICES = (
    ('amg4', 'AMG 4'),
)

AMG5_FORM_ID_CHOICES = (
    ('amg5', 'AMG 5'),
)

AMG6_FORM_ID_CHOICES = (
    ('amg6', 'AMG 6'),
)

AMG7_FORM_ID_CHOICES = (
    ('amg7', 'AMG 7'),
)

CCMG1_FORM_ID_CHOICES = (
    ('ccmg1', 'CCMG 1'),
)

CCMG2_FORM_ID_CHOICES = (
    ('ccmg2', 'CCMG 2'),
)

CCMG3_FORM_ID_CHOICES = (
    ('ccmg3', 'CCMG 3'),
)

CMG1_FORM_ID_CHOICES = (
    ('cmg1', 'CMG 1'),
)

CMG2_FORM_ID_CHOICES = (
    ('cmg2', 'CMG 2'),
)
 
CMG3_FORM_ID_CHOICES = (
    ('cmg3', 'CMG 3'),
)
 
CMG4_FORM_ID_CHOICES = (
    ('cmg4', 'CMG 4'),
)
 
CMG5_FORM_ID_CHOICES = (
    ('cmg5', 'CMG 5'),
)
 
CMG6_FORM_ID_CHOICES = (
    ('cmg6', 'CMG 6'),
)
 
CMG7_FORM_ID_CHOICES = (
    ('cmg7', 'CMG 7'),
)

EDMG1_FORM_ID_CHOICES = (
    ('edmg1', 'EDMG 1'),
)

EDMG2_FORM_ID_CHOICES = (
    ('edmg2', 'EDMG 2'),
)

EDMG3_FORM_ID_CHOICES = (
    ('edmg3', 'EDMG 3'),
)

EDMG4_FORM_ID_CHOICES = (
    ('edmg4', 'EDMG 4'),
)

EDMG5_FORM_ID_CHOICES = (
    ('edmg5', 'EDMG 5'),
)

IMG1_FORM_ID_CHOICES = (
    ('img1', 'IMG 1'),
)

IMG2_FORM_ID_CHOICES = (
    ('img2', 'IMG 2'),
)

IMG3_FORM_ID_CHOICES = (
    ('img3', 'IMG 3'),
)

IMG4_FORM_ID_CHOICES = (
    ('img4', 'IMG 4'),
)

IMG5_FORM_ID_CHOICES = (
    ('img5', 'IMG 5'),
)

RMG1_FORM_ID_CHOICES = (
    ('rmg1', 'RMG 1'),
)

RMG2_FORM_ID_CHOICES = (
    ('rmg2', 'RMG 2'),
)

RMG3_FORM_ID_CHOICES = (
    ('rmg3', 'RMG 3'),
)

RMG4_FORM_ID_CHOICES = (
    ('rmg4', 'RMG 4'),
)

RMG5_FORM_ID_CHOICES = (
    ('rmg5', 'RMG 5'),
)

SCMG1_FORM_ID_CHOICES = (
    ('scmg1', 'SCMG 1'),
)

SCMG2_FORM_ID_CHOICES = (
    ('scmg2', 'SCMG 2'),
)

SCMG3_FORM_ID_CHOICES = (
    ('scmg3', 'SCMG 3'),
)

SCMG4_FORM_ID_CHOICES = (
    ('scmg4', 'SCMG 4'),
)

SAG1_FORM_ID_CHOICES = (
    ('sag1', 'SAG 1'),
)

SAG2_FORM_ID_CHOICES = (
    ('sag2', 'SAG 2'),
)

SAG3_FORM_ID_CHOICES = (
    ('sag3', 'SAG 3'),
)

TAG1_FORM_ID_CHOICES = (
    ('tag1', 'TAG 1'),
)

TAG2_FORM_ID_CHOICES = (
    ('tag2', 'TAG 2'),
)

VMG1_FORM_ID_CHOICES = (
    ('vmg1', 'VMG 1'),
)

VMG2_FORM_ID_CHOICES = (
    ('vmg2', 'VMG 2'),
)

VMG3_FORM_ID_CHOICES = (
    ('vmg3', 'VMG 3'),
)

VMG4_FORM_ID_CHOICES = (
    ('vmg4', 'VMG 4'),
)

AMMIL2_FORM_ID_CHOICES = (   
    ('ammil2', 'AMMIL 2'),
)

AMMIL3_FORM_ID_CHOICES = ( 
    ('ammil3', 'AMMIL 3'),
)

AMMIL4_FORM_ID_CHOICES = ( 
    ('ammil4', 'AMMIL 4'),
)

AMMIL5_FORM_ID_CHOICES = ( 
    ('ammil5', 'AMMIL 5'),
)

CCMMIL2_FORM_ID_CHOICES = (
    ('ccmmil2', 'CCMMIL 2'),
)

CCMMIL3_FORM_ID_CHOICES = (
    ('ccmmil3', 'CCMMIL 3'),
)

CCMMIL4_FORM_ID_CHOICES = (
    ('ccmmil4', 'CCMMIL 4'),
)

CCMMIL5_FORM_ID_CHOICES = (
    ('ccmmil5', 'CCMMIL 5'),
)

CMMIL2_FORM_ID_CHOICES = (
    ('cmmil2', 'CMMIL 2'),
)

CMMIL3_FORM_ID_CHOICES = (
    ('cmmil3', 'CMMIL 3'),
)

CMMIL4_FORM_ID_CHOICES = (
    ('cmmil4', 'CMMIL 4'),
)

CMMIL5_FORM_ID_CHOICES = (
    ('cmmil5', 'CMMIL 5'),
)

EDMMIL2_FORM_ID_CHOICES = (
    ('edmmil2', 'EDMMIL 2'),
)

EDMMIL3_FORM_ID_CHOICES = (
    ('edmmil3', 'EDMMIL 3'),
)

EDMMIL4_FORM_ID_CHOICES = (
    ('edmmil4', 'EDMMIL 4'),
)

EDMMIL5_FORM_ID_CHOICES = (
    ('edmmil5', 'EDMMIL 5'),
)

IMMIL2_FORM_ID_CHOICES = (
    ('immil2', 'IMMIL 2'),
)

IMMIL3_FORM_ID_CHOICES = (
    ('immil3', 'IMMIL 3'),
)

IMMIL4_FORM_ID_CHOICES = (
    ('immil4', 'IMMIL 4'),
)

IMMIL5_FORM_ID_CHOICES = (
    ('immil5', 'IMMIL 5'),
)

RMMIL2_FORM_ID_CHOICES = (
    ('rmmil2', 'RMMIL 2'),
)

RMMIL3_FORM_ID_CHOICES = (
    ('rmmil3', 'RMMIL 3'),
)

RMMIL4_FORM_ID_CHOICES = (
    ('rmmil4', 'RMMIL 4'),
)

RMMIL5_FORM_ID_CHOICES = (
    ('rmmil5', 'RMMIL 5'),
)

SCMMIL2_FORM_ID_CHOICES = (
    ('scmmil2', 'SCMMIL 2'),
)

SCMMIL3_FORM_ID_CHOICES = (
    ('scmmil3', 'SCMMIL 3'),
)

SCMMIL4_FORM_ID_CHOICES = (
    ('scmmil4', 'SCMMIL 4'),
)

SCMMIL5_FORM_ID_CHOICES = (
    ('scmmil5', 'SCMMIL 5'),
)

SAMIL2_FORM_ID_CHOICES = (
    ('samil2', 'SAMIL 2'),
)

SAMIL3_FORM_ID_CHOICES = (
    ('samil3', 'SAMIL 3'),
)

SAMIL4_FORM_ID_CHOICES = (
    ('samil4', 'SAMIL 4'),
)

SAMIL5_FORM_ID_CHOICES = (
    ('samil5', 'SAMIL 5'),
)

TAMIL2_FORM_ID_CHOICES = (
    ('tamil2', 'TAMIL 2'),
)

TAMIL3_FORM_ID_CHOICES = (
    ('tamil3', 'TAMIL 3'),
)

TAMIL4_FORM_ID_CHOICES = (
    ('tamil4', 'TAMIL 4'),
)

TAMIL5_FORM_ID_CHOICES = (
    ('tamil5', 'TAMIL 5'),
)

VMMIL2_FORM_ID_CHOICES = (
    ('vmmil2', 'VMMIL 2'),
)

VMMIL3_FORM_ID_CHOICES = (
    ('vmmil3', 'VMMIL 3'),
)

VMMIL4_FORM_ID_CHOICES = (
    ('vmmil4', 'VMMIL 4'),
)

VMMIL5_FORM_ID_CHOICES = (
    ('vmmil5', 'VMMIL 5'),
)

FORM_RESPONSE_CHOICES = (
    ('', '--Select a Response'),
    ('yes', 'YES'),
    ('no', 'NO'),
)

#GOAL DATABASE TABLES
#ASSET MANAGEMENT GOALS (AMG)
#AMG1
AMG1_FORM_ID_CHOICES = (
    ('amg1', 'AMG 1'),
)
class amg1formdb(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    AMG1_RESPONSES_NUMBER = (
    (ONE,'One'),
    (TWO,'Two'),
    (THREE,'Three'),
    (FOUR,'Four')
    )
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=AMG1_FORM_ID_CHOICES, default='amg1')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    amg1_complete = models.IntegerField(
        choices=AMG1_RESPONSES_NUMBER, default=ONE)
    amg1_incomplete = models.IntegerField(blank=True, null=True)
    #amg1_incomplete = 4 - amg1_complete
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

    def __int__(self):
        return "{}-{}".format(self.amg1_complete, self.amg1_incomplete)

#AMG2
class amg2formdb(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    AMG2_RESPONSES_NUMBER = (
    (ONE,'One'),
    (TWO,'Two'),
    (THREE,'Three'),
    (FOUR,'Four'),
    (FIVE,'Five')
    )
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=AMG2_FORM_ID_CHOICES, default='amg2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    amg2_complete = models.IntegerField(
        choices=AMG2_RESPONSES_NUMBER, default=ONE)
    amg2_incomplete = models.IntegerField(blank=True, null=True)
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five)
    def __int__(self):
        return "{}-{}".format(self.amg2_complete, self.amg2_incomplete)

#AMG3
class amg3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=AMG3_FORM_ID_CHOICES, default='amg3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#AMG4
class amg4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=AMG4_FORM_ID_CHOICES, default='amg4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#AMG5
class amg5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=AMG5_FORM_ID_CHOICES, default='amg5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_six = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_seven = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five, self.response_six, self.response_seven)

#AMG6
class amg6formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=AMG6_FORM_ID_CHOICES, default='amg6')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_six = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_seven = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five, self.response_six, self.response_seven)

#AMG7
class amg7formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=AMG7_FORM_ID_CHOICES, default='amg7')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#CONFIGRATION CHANGE MANAGEMENT GOALS (CCMG)
#CCMG1
class ccmg1formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CCMG1_FORM_ID_CHOICES, default='ccmg1')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_six = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five, self.response_six)

#CCMG2
class ccmg2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CCMG2_FORM_ID_CHOICES, default='ccmg2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_six = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_seven = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_eight = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_nine = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_ten = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five, self.response_six, self.response_seven, self.response_eight, self.response_nine, self.response_ten)

#CCMG3
class ccmg3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CCMG3_FORM_ID_CHOICES, default='ccmg3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_six = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five, self.response_six)

#CONTROLS MANAGEMENT GOALS (CMG)
#CMG1
class cmg1formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CMG1_FORM_ID_CHOICES, default='cmg1')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#CMG2
class cmg2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CMG2_FORM_ID_CHOICES, default='cmg2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_six = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_seven = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_eight = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_nine = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_ten = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five, self.response_six, self.response_seven, self.response_eight, self.response_nine, self.response_ten)

#CMG3
class cmg3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CMG3_FORM_ID_CHOICES, default='cmg3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#CMG4
class cmg4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CMG4_FORM_ID_CHOICES, default='cmg4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)


#EXTERNAL DEPENDENCIES MANAGEMENT (EDMG)
#EDMG1
class edmg1formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=EDMG1_FORM_ID_CHOICES, default='edmg1')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#EDMG2
class edmg2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=EDMG2_FORM_ID_CHOICES, default='edmg2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one)

#EDMG3
class edmg3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=EDMG3_FORM_ID_CHOICES, default='edmg3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#EDMG4
class edmg4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=EDMG4_FORM_ID_CHOICES, default='edmg4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#EDMG5
class edmg5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=EDMG5_FORM_ID_CHOICES, default='edmg5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#INCIDENT MANAGEMENT
#IMG1
class img1formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=IMG1_FORM_ID_CHOICES, default='img1')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#IMG2
class img2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=IMG2_FORM_ID_CHOICES, default='img2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_six = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_seven = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_eight = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_nine = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five, self.response_six, self.response_seven, self.response_eight, self.response_nine)

#IMG3
class img3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=IMG3_FORM_ID_CHOICES, default='img3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#IMG4
class img4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=IMG4_FORM_ID_CHOICES, default='img4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#IMG5
class img5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=IMG5_FORM_ID_CHOICES, default='img5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#RISK MANAGEMENT
#RMG1
class rmg1formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=RMG1_FORM_ID_CHOICES, default='rmg1')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#RMG2
class rmg2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=RMG2_FORM_ID_CHOICES, default='rmg2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#RMG3
class rmg3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=RMG3_FORM_ID_CHOICES, default='rmg3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one)

#RMG4
class rmg4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=RMG4_FORM_ID_CHOICES, default='rmg4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#RMG5
class rmg5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=RMG5_FORM_ID_CHOICES, default='rmg5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#SERVICE CONTINUITY MANAGEMENT
#SCMG1
class scmg1formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SCMG1_FORM_ID_CHOICES, default='scmg1')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_six = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_seven = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five, self.response_six, self.response_seven)

#SCMG2
class scmg2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SCMG2_FORM_ID_CHOICES, default='scmg2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one)

#SCMG3
class scmg3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SCMG3_FORM_ID_CHOICES, default='scmg3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five)

#SCMG4
class scmg4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SCMG4_FORM_ID_CHOICES, default='scmg4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#SITUATIONAL AWARENESS
#SAG1
class sag1formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SAG1_FORM_ID_CHOICES, default='sag1')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#SAG2
class sag2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SAG2_FORM_ID_CHOICES, default='sag2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#SAG3
class sag3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SAG3_FORM_ID_CHOICES, default='sag3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#TRAINING AWARENESS
#TAG1
class tag1formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=TAG1_FORM_ID_CHOICES, default='tag1')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#TAG2
class tag2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=TAG2_FORM_ID_CHOICES, default='tag2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_six = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_seven = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five, self.response_six, self.response_seven)

#VULNERABILITY AWARENESS
#VMG1
class vmg1formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=VMG1_FORM_ID_CHOICES, default='vmg1')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five)

#VMG2
class vmg2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=VMG2_FORM_ID_CHOICES, default='vmg2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_six = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five, self.response_six)

#VMG3
class vmg3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=VMG3_FORM_ID_CHOICES, default='vmg3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
   
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#VMG4
class vmg4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=VMG4_FORM_ID_CHOICES, default='vmg4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one)

#MATURITY INDICATOR LEVELS DATABASE TABLES
#ASSET MANAGEMENT MATURITY INDICATOR LEVELS
#AMMIL2
class ammil2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=AMMIL2_FORM_ID_CHOICES, default='ammil2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#AMMIL3
class ammil3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=AMMIL3_FORM_ID_CHOICES, default='ammil3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#AMMIL4
class ammil4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=AMMIL4_FORM_ID_CHOICES, default='ammil4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')

    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#AMMIL5
class ammil5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=AMMIL5_FORM_ID_CHOICES, default='ammil5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#CONTROLS CHANGE MANAGEMENT MATURITY INDICATOR LEVELS
#CCMMIL2
class ccmmil2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CCMMIL2_FORM_ID_CHOICES, default='ccmmil2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#CCMMIL3
class ccmmil3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CCMMIL3_FORM_ID_CHOICES, default='ccmmil3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#CCMMIL4
class ccmmil4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CCMMIL4_FORM_ID_CHOICES, default='ccmmil4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#CCMMIL5
class ccmmil5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CCMMIL5_FORM_ID_CHOICES, default='ccmmil5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#CONTROLS MANAGEMENT MATURITY INDICATOR LEVELS
#CMMIL2
class cmmil2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CMMIL2_FORM_ID_CHOICES, default='cmmil2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#CMMIL3
class cmmil3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CMMIL3_FORM_ID_CHOICES, default='cmmil3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#CMMIL4
class cmmil4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CMMIL4_FORM_ID_CHOICES, default='cmmil4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#CMMIL5
class cmmil5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=CMMIL5_FORM_ID_CHOICES, default='cmmil5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#EXTERNAL DEPENDANCIES MANAGEMENT MATURITY INDICATOR LEVELS
#EDMMIL2
class edmmil2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=EDMMIL2_FORM_ID_CHOICES, default='edmmil2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#EDMMIL3
class edmmil3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=EDMMIL3_FORM_ID_CHOICES, default='edmmil3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#EDMMIL4
class edmmil4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=EDMMIL4_FORM_ID_CHOICES, default='edmmil4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#EDMMIL5
class edmmil5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=EDMMIL5_FORM_ID_CHOICES, default='edmmil5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#INCIDENT MANAGEMENT MATURITY INDICATOR LEVELS
#IMMIL2
class immil2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=IMMIL2_FORM_ID_CHOICES, default='immil2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five)

#IMMIL3
class immil3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=IMMIL3_FORM_ID_CHOICES, default='immil3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_five = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_six = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_seven = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four, self.response_five, self.response_six, self.response_seven)

#IMMIL4
class immil4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=IMMIL4_FORM_ID_CHOICES, default='immil4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#IMMIL5
class immil5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=IMMIL5_FORM_ID_CHOICES, default='immil5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#RISK MANAGEMENT MATURITY INDICATOR LEVELS
#RMMIL2
class rmmil2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=RMMIL2_FORM_ID_CHOICES, default='rmmil2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#RMMIL3
class rmmil3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=RMMIL3_FORM_ID_CHOICES, default='rmmil3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#RMMIL4
class rmmil4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=RMMIL4_FORM_ID_CHOICES, default='rmmil4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#RMMIL5
class rmmil5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=RMMIL5_FORM_ID_CHOICES, default='rmmil5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#ASSET MANAGEMENT MATURITY INDICATOR LEVELS
#SCMMIL2
class scmmil2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SCMMIL2_FORM_ID_CHOICES, default='scmmil2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#SCMMIL3
class scmmil3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SCMMIL3_FORM_ID_CHOICES, default='scmmil3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#SCMMIL4
class scmmil4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SCMMIL4_FORM_ID_CHOICES, default='scmmil4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#SCMMIL5
class scmmil5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SCMMIL5_FORM_ID_CHOICES, default='scmmil5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)



#SITUATIONAL AWARENESS MATURITY INDICATOR LEVELS
#SAMIL2
class samil2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SAMIL2_FORM_ID_CHOICES, default='samil2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#SAMIL3
class samil3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SAMIL3_FORM_ID_CHOICES, default='samil3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#SAMIL4
class samil4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SAMIL4_FORM_ID_CHOICES, default='samil4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#SAMIL5
class samil5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=SAMIL5_FORM_ID_CHOICES, default='samil5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#TRAINING AWARENESS MATURITY INDICATOR LEVELS
#TAMIL2
class tamil2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=TAMIL2_FORM_ID_CHOICES, default='tamil2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#TAMIL3
class tamil3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=TAMIL3_FORM_ID_CHOICES, default='tamil3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#TAMIL4
class tamil4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=TAMIL4_FORM_ID_CHOICES, default='tamil4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#TAMIL5
class tamil5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=TAMIL5_FORM_ID_CHOICES, default='tamil5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)

#VULNERABILITY MANAGEMENT MATURITY INDICATOR LEVELS
#VMMIL2
class vmmil2formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=VMMIL2_FORM_ID_CHOICES, default='vmmil2')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#VMMIL3
class vmmil3formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=VMMIL3_FORM_ID_CHOICES, default='vmmil3')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_four = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three, self.response_four)

#VMMIL4
class vmmil4formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=VMMIL4_FORM_ID_CHOICES, default='vmmil4')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_three = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two, self.response_three)

#VMMIL5
class vmmil5formdb(models.Model):
    expertid = models.ForeignKey(
        cseformdb, on_delete=models.CASCADE, verbose_name="expert id",)
    formid = models.CharField(
        max_length=8, choices=VMMIL5_FORM_ID_CHOICES, default='vmmil5')
    response_one = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    response_two = models.CharField(
        max_length=6, choices=FORM_RESPONSE_CHOICES, default='')
    
    feedback = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return "{}-{}".format(self.expertid, self.formid, self.response_one, self.response_two)