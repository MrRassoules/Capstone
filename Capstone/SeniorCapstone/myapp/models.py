from django.db import models

# State Demographics model
class StateDemographic(models.Model):
	# Name of the state
	state = models.CharField(max_length=30)
	
	# Treated as a decimal so .88 = 88%
	white_highschool_grad_rate = models.DecimalField(max_digits = 2, decimal_places = 2, blank=True, null=True)
	black_highschool_grad_rate = models.DecimalField(max_digits = 2, decimal_places = 2, blank=True, null=True)
	
	# Treated as a decimal so .88 = 88%
	white_college_grad_rate = models.DecimalField(max_digits = 2, decimal_places = 2, blank=True, null=True)
	black_college_grad_rate = models.DecimalField(max_digits = 2, decimal_places = 2, blank=True, null=True)
	
	# By state and race
	white_median_income = models.PositiveIntegerField()
	black_median_income = models.PositiveIntegerField()
	black_population_percentage = models.DecimalField(max_digits = 2, decimal_places = 2, blank=True, null=True)
	black_population_raw_amount = models.PositiveIntegerField()
	white_population_percentage = models.DecimalField(max_digits = 2, decimal_places = 2, blank=True, null=True)
	white_population_raw_amount = models.PositiveIntegerField()
	

	
	
	