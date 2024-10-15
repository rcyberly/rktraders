from django.db import models
class Home(models.Model):
    im = models.FileField(upload_to="Home/", max_length=250,null=True, default=None)
    pname = models.CharField(max_length=50)
    pdesc = models.TextField(max_length=500)
    pprice = models.IntegerField()
    pquantity = models.IntegerField()
    pgst = models.IntegerField()
    pdc = models.IntegerField()
    Displayfields = ['im','pname','pdesc','pprice','pquantity','pgst','pdc','Total']
    class Meta:
        db_table='Home_home'
    @property
    def Total(self):
       
            Total = self.pprice + self.pquantity + self.pgst + self.pdc 
            return Total
    


# Create your models here.
