from django.db import models
from member_app.models import MemberProfile

# Create your models here.


class Membership(models.Model):
    MEM_NUM = models.IntegerField(primary_key=True,) 
    MEM_FNAME = models.CharField(max_length=300, null=True)  
    MEM_LNAME = models.CharField(max_length=300, null=True) 
    MEM_STREET = models.CharField(max_length=300, null=True)
    MEM_CITY = models.CharField(max_length=300, null=True)
    MEM_STATE = models.CharField(max_length=300, null=True)
    MEM_ZIP = models.CharField(max_length=300, null=True)
    MEM_BALANCE = models.CharField(max_length=300, null=True)


class DetailRental(models.Model):
    RENT_NUM = models.IntegerField(primary_key=True,) 
    VID_NUM = models.IntegerField(null=True)
    DETAIL_FEE = models.CharField(max_length=300, null=True) 
    DETAIL_DUEDATE = models.DateTimeField(null=True)
    DETAIL_RETURNDATE = models.DateTimeField(null=True)
    DETAIL_DAILYLATEFEE = models.CharField(max_length=300, null=True)



    
class Video(models.Model):
    VID_NUM = models.IntegerField(primary_key=True)
    VID_INDATE = models.DateField(null=True)
    MOVIE_NUM = models.IntegerField(null=True) 

class Movie(models.Model):
    VID_NUM = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)
    MOVIE_TITLE= models.CharField(max_length=300, null=True)
    MOVIE_YEAR = models.CharField(max_length=300, null=True)
    MOVIE_COST= models.CharField(max_length=300, null=True)
    MOVIE_GENRE = models.CharField(max_length=300, null=True)
    PRICE_CODE = models.CharField(max_length=300, null=True)

    def __str__(self):
        return str(self.MOVIE_TITLE)


class Rental(models.Model):
    MOVIE = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    RENT_NUM = models.IntegerField(primary_key=True)
    RENT_DATE = models.DateTimeField(null=True)
    MEM_NUM = models.ForeignKey(MemberProfile, on_delete=models.CASCADE, null=True)
   


class Price(models.Model):
    PRICE_CODE = models.IntegerField(primary_key=True)
    PRICE_DESCRIPTION = models.CharField(max_length=300, null=True)
    PRICE_RENTFEE = models.CharField(max_length=300, null=True)
    PRICE_DAILYLATEFEE = models.CharField(max_length=300, null=True)


    