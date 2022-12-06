from django.db import models
from apps.products import models as m_p

class GastiAsih(models.Model):
    name_vendor = models.ForeignKey(m_p.JasaPengiriman,on_delete=models.CASCADE)
    origin = models.ForeignKey(m_p.Negara,on_delete=models.CASCADE,null=True, related_name='or_gst',
        blank=True)
    destinations = models.ForeignKey(m_p.Negara,on_delete=models.CASCADE,null=True, related_name='des_gst',
        blank=True)
    jenis_angkutan = models.CharField(choices = m_p.JENISPRODUK,max_length=20,null= True,blank= True)
    rate = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)  # type: ignore

    class Meta:
        db_table = 'gastiasih'

    def __str__(self):
        return '%s %s %s %s %s'%(self.id, self.name_vendor,self.jenis_angkutan,self.origin, self.destinations)  # type: ignore


