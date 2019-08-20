from django.db import models

# Create your models here.
HOUSE_CATEGORY={
    ("Flats and Apartments":"flats and apartments"),
    ("STUDIO":"studio"),
}
class Housing(models.Model):
    name=models.CharField(max_length=20,null=False)
    image=models.ImageField(upload_to='media/',null=False)
    contact=models.IntegerField(null=True,blank=False)
    description=models.TextField(max_length=10000,null=False)
    category=