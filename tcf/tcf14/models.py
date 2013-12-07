from django.db import models

# Create your models here.
class Booth(models.Model):
	number = models.IntegerField(verbose_name=u'Booth Number')
	row = models.IntegerField(verbose_name=u'Map Row')
	col = models.IntegerField(verbose_name=u'Map Column')
	filler = models.BooleanField(verbose_name=u'Filler?', default=False)

	def __str__(self):
		if self.filler:
			return "FILLER - Row " + str(self.row) + ", Col " + str(self.col);

		try:
			return "Booth " + str(self.number) + " (" + self.company.name + ")"
		except Company.DoesNotExist:
			return "Booth " + str(self.number)

	class Meta:
		verbose_name=u'Booth'
		verbose_name_plural=u'Booths'

class Company(models.Model):
	name = models.CharField(max_length=40, verbose_name=u'Name')
	description = models.TextField(verbose_name=u'Description', blank=True, null=True)
	website = models.CharField(max_length=100, verbose_name=u'Website URL', blank=True, null=True)
	facebook = models.CharField(max_length=100, verbose_name=u'Facebook URL', blank=True, null=True)
	twitter = models.CharField(max_length=100, verbose_name=u'Twitter URL', blank=True, null=True)
	linkedin = models.CharField(max_length=100, verbose_name=u'LinkedIn URL', blank=True, null=True)
	email = models.CharField(max_length=100, verbose_name=u'E-Mail Address', blank=True, null=True)
	logo = models.ImageField(upload_to='comapny_logos/' ,verbose_name='Logo File', blank=True, null=True)
	booth = models.OneToOneField(Booth, blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name=u'Company'
		verbose_name_plural=u'Companies'

class User(models.Model):
	fname = models.CharField(max_length=40, verbose_name=u'First Name', blank=True, null=True)
	lname = models.CharField(max_length=40, verbose_name=u'Last Name', blank=True, null=True)
	email = models.CharField(max_length=200, verbose_name=u'E-Mail Address', blank=True, null=True)
	phone = models.CharField(max_length=15, verbose_name=u'Phone Number', blank=True, null=True)

class Visit(models.Model):
	company = models.ForeignKey(Company)
	ip = models.CharField(max_length=20, verbose_name=u'IP Address')
	user = models.ForeignKey(User, blank=True, null=True)

class Checkin(models.Model):
	company = models.ForeignKey(Company)
	user = models.ForeignKey(User)