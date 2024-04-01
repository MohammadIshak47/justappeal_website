from django.db import models


type_choices = (
	('volentues', 'volentures'),
	('counsellor', 'counsellor'),
	('advisor', 'advisor'),
	)

donation_types = (
	('zakat', 'zakat'),
	('sadaqah', 'sadakah'),
	('donation', 'donation')
	)
class Appeal(models.Model):
	category = models.CharField(max_length=20, verbose_name="Apeal type")
	region = models.CharField(max_length=100, verbose_name="Region")
	title = models.CharField(max_length=20, verbose_name="Appeal Title")
	donation = models.PositiveIntegerField(verbose_name="Expected Donation")
	image = models.ImageField(upload_to='apeals/')
	author = models.CharField(max_length=30)
	description = models.TextField(max_length=1000000)
	created_date = models.DateTimeField()
	raised_fund = models.PositiveIntegerField(verbose_name="raised amount", blank=True, null=True, default=0)

	def __str__(self):
		return f"Apeal for {self.author} for {self.category}"

	class Meta:
		ordering = ['-created_date']

class GlobalAppeal(models.Model):
	category = models.CharField(max_length=20, verbose_name="Apeal type")
	region = models.CharField(max_length=100, verbose_name="Region")
	title = models.CharField(max_length=20, verbose_name="Appeal Title")
	donation = models.PositiveIntegerField(verbose_name="Expected Donation")
	image = models.ImageField(upload_to='apeals/')
	author = models.CharField(max_length=30)
	description = models.TextField(max_length=1000000)
	created_date = models.DateTimeField()
	raised_fund = models.PositiveIntegerField(verbose_name="raised amount", blank=True, null=True, default=0)

	def __str__(self):
		return f"Apeal for {self.author} for {self.category}"

	class Meta:
		ordering = ['-created_date']  
	

class Event(models.Model):
	created_date = models.DateTimeField()
	end_date = models.DateTimeField()
	title = models.CharField(max_length=30, verbose_name="Event name")
	description = models.TextField(max_length=1000)
	image = models.ImageField(upload_to='events/')
	ticket = models.BooleanField(default=False)
	price = models.PositiveIntegerField(blank=True, null=True, verbose_name="Price of ticket if true")

	def __str__(self):
		return f"Event name {self.title}"

class TicketSold(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	price = models.PositiveIntegerField()

	def __str__(self):
		return f"{self.event.title}"

class Volenture(models.Model):
	image = models.ImageField(upload_to='volenutes', verbose_name="Your Image")
	age = models.PositiveIntegerField()
	full_name = models.CharField(max_length=100)
	number = models.PositiveIntegerField()
	email = models.EmailField()
	address = models.CharField(max_length=100)
	country = models.CharField(max_length=20, verbose_name="Region")
	volenture_type = models.CharField(max_length=20, choices=type_choices)
	registration_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"volenutes name {self.full_name}"

class Donation(models.Model):
	donation_type = models.CharField(choices=donation_types, max_length=20)
	amount = models.PositiveIntegerField()
	donated_date = models.DateTimeField(auto_now_add=True)


