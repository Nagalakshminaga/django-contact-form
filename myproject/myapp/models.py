from django.db import models

# Create your models here.
class CommentModel(models.Model):
	name = models.CharField( max_length = 20, blank = False,null = False)
	college = models.CharField(max_length = 100, blank = False,null = False)
	roll_number = models.IntegerField( blank = False,null = False)
	comment = models.TextField(blank = False, null = False)
	files  = models.FileField(upload_to="Files", null=True, blank=True)
	

    
	
	def __str__(self):
         return self.name
