from django.db import models

class Bisnis(models.Model):
    nama = models.CharField(max_length=50,null=True)
    alamat = models.CharField(max_length=250, blank=True, null=True)
    kota = models.CharField(max_length=35, blank=True, null=True)
    telepon = models.CharField(max_length=35, blank=True, null=True)
    kodepos = models.CharField(max_length=7, null=True, blank=True)
    kode_cabang = models.IntegerField(null=True)
    kepala_cabang = models.CharField(max_length=25,null=True)
    adm_cabang = models.CharField(max_length=25,null=True)

    class Meta:
        abstract = True

class Cabang(Bisnis):
    singkatan = models.CharField(max_length=12,null=True)
    parent = models.ForeignKey('self', blank=True, null=True,on_delete=models.CASCADE)
    kode_produk = models.CharField(max_length=2,null=True)
    cdate = models.DateTimeField(auto_now_add=True)
    aktif = models.BooleanField(default=False)

    class Meta:
        db_table = 'cabang'
        verbose_name = 'Cabang'
        verbose_name_plural = verbose_name

    def __str__(self) :
        return self.singkatan