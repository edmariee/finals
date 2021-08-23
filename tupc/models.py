from django.db import models

# Create your models here.
'''class SignUpInfo(models.Model):
    #SignUpInfo
	firstname = models.CharField(max_length=20, verbose_name = 'firstname' )
	lastname = models.CharField(max_length=20, verbose_name = 'lastname' )
	email = models.EmailField(max_length=20, verbose_name = 'email' )
	surname = models.CharField(max_length=20, unique= True)
	password = models.CharField(max_length=20, unique= True)


	def __str__(self):
		return self.lastname
'''

class OrganizationInfo(models.Model):
		
	adviser = models.CharField(max_length=20, verbose_name = 'Adviser' )
	contact = models.DecimalField(max_digits=11, decimal_places=0, verbose_name='Contact Number', default="")
	

	ORGANIZATION_CHOICES = (
		('', ''),
	    ('ASSOCIATION OF CIVIL ENGINEERING TECHNOLOGY STUDENTS', 'ASSOCIATION OF CIVIL ENGINEERING TECHNOLOGY STUDENTS'),
		('ASSOCIATION OF COMPUTER TECHNOLOGY STUDENTS', 'ASSOCIATION OF COMPUTER TECHNOLOGY STUDENTS'),
	    ('ASSOCIATION OF POWER PLANT ENGINEERING TECHNOLOGY STUDENTS', ' ASSOCIATION OF POWER PLANT ENGINEERING TECHNOLOGY STUDENTS'),
	    ('ARTISTS` CLUB', 'ARTISTS` CLUB'),
	    ('ENGINEERING HONOR SOCIETY', 'ENGINEERING HONOR SOCIETY'),
		('FUTURE EDUCATORS’ ORGANIZATION', 'FUTURE EDUCATORS’ ORGANIZATION'),
		('MECHANICAL ENGINEERING TECHNOLOGY STUDENTS', 'MECHANICAL ENGINEERING TECHNOLOGY STUDENTS'),
		('PHILIPPINE INSTITUTE OF CIVIL ENGINEERS STUDENTS', 'PHILIPPINE INSTITUTE OF CIVIL ENGINEERS'),
		('OTTO DE DION', 'OTTO DE DION'),
		('STUDENT AMBASSADOR FOR CHRIST', 'STUDENT AMBASSADOR FOR CHRIST'),
		('SOCIETY OF ELECTRONICS TECHNOLOGY STUDENT', 'SOCIETY OF ELECTRONICS TECHNOLOGY STUDENT'),
		('STUDENTS RIDERS CLUB', 'STUDENTS RIDERS CLUB'),
		)
	
	org = models.CharField(max_length=80, default="", choices=ORGANIZATION_CHOICES, null=True, verbose_name = 'Organization Name')
	def __str__(self):
		return self.org


class OfficersInfo(models.Model):
    #OfficerInfo
	OrganizationName = models.ForeignKey(OrganizationInfo, null=True, on_delete = models.SET_NULL, verbose_name = 'Organization Name')
	first = models.CharField(max_length=20, verbose_name = 'firstname')
	last = models.CharField(max_length=20, verbose_name = 'lastname')
	position = models.CharField(max_length=20, verbose_name = 'Position')
	academic = models.CharField(max_length=20, verbose_name = 'Academic Year' )
	student = models.CharField(max_length=20, verbose_name = 'Student ID Number', unique = True )

	gender =(('', ''), ('Male', 'Male'), ('Female', 'Female'))
	sex = models.CharField(max_length=20,default="", choices= gender)


	COURSES_CHOICES = (
		('', ''),
	    ('BACHELOR OF SCIENCE IN CIVIL ENGINEERING', 'BSCE'),
	    ('BACHELOR OF SCIENCE IN ELECTRICAL ENGINEERING', 'BSEE'),
	    ('BACHELOR OF SCIENCE IN MECHANICAL ENGINEERING', 'BSME'),
	    ('BET-ELECTRICAL TECHNOLOGY', 'BET-ET'),
		('BET-INDUSTRIAL AUTOMATION TECHNOLOGY', 'BET-ESET'),
		('BET-COMPUTER ENGINEERING TECHNOLOGY', 'BET-COET'),
		('BET-CIVIL TECHNOLOGY', 'BET-CT'),
		('BET-MECHANICAL ENGINEERING TECHNOLOGY', 'BET-MT'),
		('BET-AUTOMOTIVE TECHNOLOGY', 'BET-MT'),
		('BET-MECHANICALENGINEERING TECHNOLOGY', 'BET-MT'),
		('BET-POWER PLANT TECHNOLOGY', 'BET-PPT'),
		('BSIE-INFORMATION COMMUNICATION TECHNOLOGY', 'BSIE-ICT'),
		('BSIE-HOME ECONOMICS', 'BSIE-HE'),
		('BTTE-AUTOMOTIVE', 'BTTE-AU'),
		('BTTE-ELECTRICAL', 'BTTE-EI'),
		('BTTE-ELECTRONICS', 'BTTE-E'),
		('BTTE-AIR CONDITIONING', 'BTTE-HVACT'),
		('BTTE-COMPUTER PROGRAMMING', 'BTTE-CP'),
	)

	course = models.CharField(max_length=50, default="", choices=COURSES_CHOICES, null=True)

	def __str__(self):
		return self.student
		#return str(self.full)

class ActivitiesInfo(models.Model):
    #ActivitiesInfo
	OrganizationName = models.ForeignKey(OrganizationInfo, null=True, on_delete = models.SET_NULL, verbose_name = 'Organization Name')
	activity = models.CharField(max_length=20, verbose_name = 'Activity Name')
	budget = models.IntegerField(verbose_name = 'Est. Budget')
	target = models.CharField(max_length=20,verbose_name = 'Target Participants')
	number = models.IntegerField(verbose_name = 'No. of Participants')
	officers = models.IntegerField(verbose_name = 'No. of Officers Involved')
	faculty = models.CharField(max_length=20,verbose_name = 'Faculty In-charged')
	description = models.TextField(max_length=20, verbose_name = 'Activity Description')

	def __str__(self):
		return self.activity

class ReportsInfo(models.Model):
    #ReportsInfo
	OrganizationName = models.ForeignKey(OrganizationInfo, null=True, on_delete = models.SET_NULL, verbose_name = 'Organization Name')
	date = models.DateField(default='')
	statuE = models.CharField(max_length=20,default="", verbose_name = 'Accomplishment Report Status' )
	file_link = models.URLField(max_length=100,default="", verbose_name = 'Accomplishment Report (Link)' )


	def __str__(self):
		return self.statuE

