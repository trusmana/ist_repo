from decimal import Decimal
from pyexpat import model
from random import choices
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import datetime
from apps.core.models import AccountsUser as user

STATUS =[('0','NonAktif'),('1','Aktif')]

STATUS_UPDATE =[('',''),('1','Done')]

JUMLAH_VENDOR=[('1','SATU'),('2','DUA'),('3','TIGA')]

JENISPRODUK =[('1','Airfreight'),('2','Seafreight')]

class Commodity(models.Model):
    nama = models.CharField(max_length=100)
    status = models.CharField(max_length= 10, choices=STATUS,null= True)
    cu = models.ForeignKey(user, related_name='cu_cd', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    mdate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'commodity'

    def __str__(self):
        return self.nama

class MataUang(models.Model):
    status =models.CharField(max_length=10,choices=STATUS,null=True,default=0)
    kode_matauang = models.CharField(max_length=5,null=True)
    nama_mata_uang = models.CharField(max_length=30,null=True,blank=True)
    negara = models.CharField(max_length=30,null=True,blank=True)
    cu = models.ForeignKey(user, related_name='cu_mt', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    mu = models.ForeignKey(user, related_name='mu_mt', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'MataUang'

    def __str__(self):
        return '%s-%s' %(self.negara,self.nama_mata_uang)


class Kurs(models.Model):
    mtu = models.ForeignKey(MataUang,on_delete=models.CASCADE,related_name='mtu_fk')
    status_kurs = models.CharField(max_length=10,choices=STATUS,default=0)
    nilai_kurs = models.FloatField(null=True,blank=True)
    tanggal_aktif = models.DateField(null=True,blank=True)
    cu = models.ForeignKey(user, related_name='cu_kurs', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    mu = models.ForeignKey(user, related_name='mu_kurs', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'kurs'

    def __str__(self):
        return self.mtu.kode_matauang

class Negara(models.Model):
    nama_negara = models.CharField(max_length=100,null=True)
    singkatan = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table ='negara'

    def __str__(self):
        return self.singkatan
    

#####Vendor
class JasaPengiriman(models.Model):
    nama_jasa_pengiriman = models.CharField(max_length=100,null=True)
    alamat = models.CharField(max_length=100,null=True)
    telepon = models.CharField(max_length=20,null=True)
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)
    cu = models.ForeignKey(user, related_name='cu_js', editable=False, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'jasapengiriman'
        verbose_name = 'JasaPengiriman'

    def __str__(self):
        return self.nama_jasa_pengiriman        
    

class Produk(models.Model):
    id_prod = models.IntegerField(null=True)
    nama_produk = models.CharField(max_length=100,null=True)
    jumlah_vendor = models.CharField(choices = JUMLAH_VENDOR,max_length=20,null= True)
    jenis_produk = models.CharField(choices = JENISPRODUK,max_length=20,null= True,blank= True)
    ####origin
    point_satu = models.ForeignKey(Negara,on_delete=models.CASCADE,null=True, related_name='point_satu',
        blank=True)
    origin_vendor = models.ForeignKey(JasaPengiriman,on_delete=models.CASCADE,null=True,related_name='origin_v1',
        blank=True)
    kurs_origin = models.ForeignKey(Kurs,on_delete=models.CASCADE,null=True,related_name='origin_kurs',
        blank=True)
    ####Through
    point_dua = models.ForeignKey(Negara,on_delete=models.CASCADE,null=True,related_name='point_dua',
        blank=True)
    through_vendor = models.ForeignKey(JasaPengiriman,on_delete=models.CASCADE,null=True,related_name='Through_v2',
        blank=True)
    kurs_through = models.ForeignKey(Kurs,on_delete=models.CASCADE,null=True,related_name='origin_trough',
        blank=True)
    ####Destinations
    point_tiga  = models.ForeignKey(Negara,on_delete=models.CASCADE,null=True,blank=True,related_name='point_tiga' )
    destinations_vendor = models.ForeignKey(JasaPengiriman,on_delete=models.CASCADE,null=True,related_name='destinatioin_v3')
    kurs_destinations = models.ForeignKey(Kurs,on_delete=models.CASCADE,null=True,related_name='origin_destinastions')


    tgl_aktif = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)
    cu = models.ForeignKey(user, related_name='cu_produk', editable=False, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'produk'
        verbose_name= 'Produk'
        verbose_name_plural =verbose_name
    
    def kode_produk(self):
        if self.jumlah_vendor == '1':
            return '%s %s' %(self.nama_produk,self.point_tiga)           
        elif self.jumlah_vendor == '2':
            return '%s %s %s' %(self.nama_produk, self.point_satu,self.point_tiga)
        else:
            return '%s %s %s Via %s' %(self.nama_produk, self.point_satu,self.point_tiga,self.point_dua)

    def __str__(self):
        return '%s-%s-%s' %(self.id,self.id_prod, self.kode_produk())

######Khusus Parameter Jual
class ParameterDataBl(models.Model):
    products = models.ForeignKey(Produk,on_delete=models.CASCADE)
    nilai_kurs = models.ForeignKey(Kurs,on_delete=models.CASCADE)
    vendor = models.ForeignKey(JasaPengiriman,on_delete=models.CASCADE,null=True,blank=True)    
    status_param = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)
    tgl_aktif_param = models.DateField(blank=True, null=True)
    ########## logistik Indah Sinergi Trading
    min_airfreight_import_handling = models.FloatField(null=True,blank=True)
    max_airfreight_import_handling = models.FloatField(null=True,blank=True)
    price_airfreight_import_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_cartage_and_warehouse_charge = models.FloatField(null=True,blank=True)
    max_cartage_and_warehouse_charge = models.FloatField(null=True,blank=True)
    price_cartage_and_warehouse_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_export_handling = models.FloatField(null=True,blank=True)
    max_export_handling = models.FloatField(null=True,blank=True)
    price_export_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    min_airfreight_sin_dps_dil = models.FloatField(null=True,blank=True)
    max_airfreight_sin_dps_dil = models.FloatField(null=True,blank=True)
    airfreight_sin_dps_dil = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_doc_and_clearance = models.FloatField(null=True,blank=True)
    max_doc_and_clearance = models.FloatField(null=True,blank=True)
    price_doc_and_clearance = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    min_ground_handling = models.FloatField(null=True,blank=True)
    max_ground_handling = models.FloatField(null=True,blank=True)
    price_ground_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_warehouse_charge = models.FloatField(null=True,blank=True)
    max_warehouse_charge = models.FloatField(null=True,blank=True)
    price_warehouse_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_handling_charge = models.FloatField(null=True,blank=True)
    max_handling_charge = models.FloatField(null=True,blank=True)
    price_handling_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_delivery = models.FloatField(null=True,blank=True)
    max_delivery = models.FloatField(null=True,blank=True)
    price_delivery = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_duty_tax = models.FloatField(null=True,blank=True)
    max_duty_tax = models.FloatField(null=True,blank=True)
    price_duty_tax = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_tax_handling_charge = models.FloatField(null=True,blank=True)
    max_tax_handling_charge = models.FloatField(null=True,blank=True)
    price_tax_handling_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    ########## logistik Indah Sinergi Trading
    cu = models.ForeignKey(user, related_name='cu_parambl', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'paramdatabl'
        verbose_name= 'ParameterDataBl'
        verbose_name_plural =verbose_name


    def __str__(self):
        return '%s' %(self.id)

    
    

##########Parameter untuk Job
class ParameterData(models.Model):
    products = models.ForeignKey(Produk,on_delete=models.CASCADE)
    nilai_kurs = models.ForeignKey(Kurs,on_delete=models.CASCADE)    
    status_param = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)
    tgl_aktif_param = models.DateField(blank=True, null=True)
    ########## Khusus Untuk Freight Solutions
    ####Pengiriman Udara
    max_airfreight = models.FloatField(null=True,blank=True,help_text="Freigh Solution")
    min_airfreight = models.FloatField(null=True,blank=True,help_text="Freigh Solution")
    
    price_min_airfreight = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution")
    price_max_airfreight = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution")
    price_high_airfreight = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution")
    
    ###### Biaya pengurusan / oprasional
    min_handling_charges = models.FloatField(null=True,blank=True,help_text="Freigh Solution",)
    price_max_handling_charges = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution",)
    price_min_handling_charges = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution",)
    
    ##### Biaya Asuransi
    min_insurance_security_surcharge = models.FloatField(null=True,blank=True,help_text="Freigh Solution")
    price_insurance_security_surcharge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution",)
    price_high_insurance_security_surcharge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution")

    ##biaya tambahan bahan bakar
    
    min_fuel_surcharge = models.FloatField(null=True,blank=True,help_text="Freigh Solution")
    price_fuel_surcharge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution")
    price_high_fuel_surcharge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution")
    ###Biaya Penanganan Impor
    
    min_import_handling_charges = models.FloatField(null=True,blank=True,help_text="Freigh Solution")
    price_import_handling_charges = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution")
    price_high_import_handling_charges = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution")

    
    min_gst_zero_rated = models.FloatField(null=True,blank=True,help_text="Freigh Solution")
    price_gst_zero_rated = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution")
    price_high_gst_zero_rated = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Freigh Solution")
    ##########Akhir Khusus Untuk Freight Solutions

    ##########Khusus Untuk Sholid Logistik
    ####### Biaya Storage
    min_storage_at_cost = models.FloatField(null=True,blank=True,help_text="Sholid Logistik")
    price_storage_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")
    price_high_storage_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")

    min_pjkp2u_sin_dps_at_cost = models.FloatField(null=True,blank=True,help_text="Sholid Logistik")
    price_pjkp2u_sin_dps_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")
    price_high_pjkp2u_sin_dps_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")

    min_storage_mcl_e_0389249_at_cost = models.FloatField(null=True,blank=True,help_text="Sholid Logistik")
    price_storage_mcl_e_0389249_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")
    price_high_storage_mcl_e_0389249_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")

    min_pjkp2u_dps_dil_at_cost = models.FloatField(null=True,blank=True,help_text="Sholid Logistik")    
    price_pjkp2u_dps_dil_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")
    price_high_pjkp2u_dps_dil_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")
    ######### Biaya Storege

    min_airfreight_charges = models.FloatField(null=True,blank=True,help_text="Sholid Logistik")
    price_airfreight_charges = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")
    price_high_airfreight_charges = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")

    min_overweight_charges_surcharge = models.FloatField(null=True,blank=True,help_text="Sholid Logistik")   
    price_overweight_charges_surcharge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")
    price_high_overweight_charges_surcharge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")

    min_awb_fee = models.FloatField(null=True,blank=True,help_text="Sholid Logistik")
    price_awb_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")
    price_high_awb_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")

    min_handling_charges_sl = models.FloatField(null=True,blank=True,help_text="Sholid Logistik")
    price_handling_charges_sl = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")
    price_high_handling_charges_sl = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Sholid Logistik")
    ########## Akhir Khusus Untuk Sholid Logistik

    ############ khusus logistik dili
    min_ground_handling_dl = models.FloatField(null=True,blank=True,help_text="LOGISTIK DILI")
    price_ground_handling_dl = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    price_high_ground_handling_dl = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    
    min_forklift_for_heavy_cargo = models.FloatField(null=True,blank=True,help_text="LOGISTIK DILI")
    price_forklift_for_heavy_cargo = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    price_high_forklift_for_heavy_cargo = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    
    min_custom_clearance = models.FloatField(null=True,blank=True,help_text="LOGISTIK DILI")
    price_custom_clearance = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    price_high_custom_clearance = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    
    min_delivey_to_hera = models.FloatField(null=True,blank=True,help_text="LOGISTIK DILI")
    price_delivey_to_hera = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    price_high_delivey_to_hera = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    
    min_akses_bandara_inspeksi = models.FloatField(null=True,blank=True,help_text="LOGISTIK DILI")
    price_akses_bandara_inspeksi = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    price_high_akses_bandara_inspeksi = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    
    min_handling_fee = models.FloatField(null=True,blank=True,help_text="LOGISTIK DILI")
    price_handling_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    price_high_handling_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    
    min_admin_fee = models.FloatField(null=True,blank=True,help_text="LOGISTIK DILI")
    admin_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI") 
    admin_high_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI") 
    
    min_fee_collection = models.FloatField(null=True,blank=True,help_text="LOGISTIK DILI")
    fee_collection = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    fee_high_collection = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="LOGISTIK DILI")
    ############ Akhir khusus logistik dili

    cu = models.ForeignKey(user, related_name='cu_paramdata', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'parameterdata'
        verbose_name = 'ParameterData'

    def __str__(self):
        return '%s' %(self.id)


class Transaksi(models.Model):
    tanggal = models.DateTimeField(auto_now_add=True)
    no_pekerjaan = models.IntegerField(blank=True,null=True)
    qty = models.IntegerField(blank=True,null=True)
    weight = models.FloatField(null=True,blank=True)
    products = models.ForeignKey(Produk,on_delete=models.CASCADE,null=True,blank=True)
    commodity =models.ForeignKey(Commodity,blank=True,null=True,on_delete= models.CASCADE)
    re_export_shipment_one = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_one_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    re_export_shipment_one_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    re_export_shipment_two = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_two_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    re_export_shipment_two_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    cu = models.ForeignKey(user, related_name='cu_transaksi', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transaksi'
        verbose_name = 'Transaksi'

    def __str__(self):
        return '%s' %(self.no_pekerjaan)

   
        

    def counter_nope(self):
        tot = 0
        try:
            skr = datetime.date.today()
            count = Transaksi.objects.filter(cdate__year=skr.year).count()
            cekkr = Transaksi.objects.filter(cdate__year=skr.year).latest('no_pekerjaan')
            if count >= 1:
                tot = cekkr.no_pekerjaan + 1
            else:
                tot = 1
        except ObjectDoesNotExist:
            tot = 1
        return tot

    def _no_pk_(self):
        skr = datetime.date.today()
        thn = int(skr.strftime("%Y"))
        bl = int(skr.strftime("%m"))
        return "%s" %(int(self.counter_nope()))

class Sale(models.Model):
    trans = models.ForeignKey(Transaksi,on_delete=models.CASCADE,null=True)
    prod = models.ForeignKey(ParameterDataBl,on_delete=models.CASCADE,null=True,blank=True)
    cartage_warehouse_charge_one =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    cartage_warehouse_charge_two =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    airfreight_one = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    airfreight_two = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    export_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    freight = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    doc_clearance = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    ground_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    warehouse_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    handling_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    delivery = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    duty_tax = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) 
    tax_handling_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    cu = models.ForeignKey(user, related_name='cu_sale', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='sale'

    def __str__(self):
        return '%s' %(self.id)

    def total_sale(self):
        return self.cartage_warehouse_charge_one + self.cartage_warehouse_charge_two + \
            self.airfreight_one + self.airfreight_two + self.export_handling + \
            self.freight + self.doc_clearance + self.ground_handling + \
            self.warehouse_charge + self.handling_charge + \
            self.delivery + self.duty_tax + self.tax_handling_charge 

class Job(models.Model):
    tanggal_invoice = models.DateField()
    no_invoice = models.IntegerField(blank=True,null=True)
    transaksi = models.ForeignKey(Transaksi,on_delete=models.CASCADE)
    status_job = models.CharField(choices=STATUS_UPDATE,null=True,blank=True,max_length=50)
    tanggal_status = models.DateField(null=True,blank=True) 
    
    vendor = models.ForeignKey(JasaPengiriman,on_delete=models.CASCADE)
    nilai_kurs = models.ForeignKey(Kurs,on_delete=models.CASCADE)
    ########## Khusus Untuk Freight Solutions
    ####Pengiriman Udara
    
    ###### Biaya pengurusan / oprasional dan Udara Untuk Freight Solution dan Shlid
    airfreight = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    handling_charges = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    ##### Biaya Asuransi
    insurance_security_surcharge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    ##biaya tambahan bahan bakar
    fuel_surcharge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    ###Biaya Penanganan Impor
    import_handling_charges = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    gst_zero_rated = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    

    ##########Akhir Khusus Untuk Freight Solutions

   
    ##########Khusus Untuk Sholid Logistik
    ####### Biaya Storage
    storage_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    pjkp2u_sin_dps_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    storage_mcl_e_0389249_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    pjkp2u_dps_dil_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    ######### Biaya Storege
    overweight_charges_surcharge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    awb_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)    
    ########## Akhir Khusus Untuk Sholid Logistik
    ##########Khusus Untuk Sholid Logistik
        
    ############ khusus logistik dili
    ground_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    forklift_for_heavy_cargo = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    custom_clearance = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    delivey_to_hera = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    akses_bandara_inspeksi = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    handling_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    admin_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) 
    fee_collection = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    ############ Akhir khusus logistik dili
    cu = models.ForeignKey(user, related_name='cu_job', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    cu_update = models.ForeignKey(user, related_name='cu_jobup', null=True, blank=True,on_delete=models.CASCADE)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'job'
        verbose_name = 'job'

    def total_job(self):
        return self.airfreight + self.handling_charges + self.insurance_security_surcharge + self.fuel_surcharge + \
            self.import_handling_charges + self.gst_zero_rated + self.storage_at_cost + self.pjkp2u_sin_dps_at_cost +\
            self.storage_mcl_e_0389249_at_cost + self.pjkp2u_dps_dil_at_cost + self.overweight_charges_surcharge +\
            self.awb_fee + self.ground_handling + self.forklift_for_heavy_cargo + self.custom_clearance + \
            self.delivey_to_hera + self.akses_bandara_inspeksi + self.handling_fee + self.admin_fee + self.fee_collection 
    
    ####Untuk Vendor Solid Logistik
    def total_sl_one(self):
        return self.storage_at_cost + self.pjkp2u_sin_dps_at_cost + self.storage_mcl_e_0389249_at_cost + self.pjkp2u_dps_dil_at_cost 
    
    def total_sl_two(self):
        return self.airfreight + self.overweight_charges_surcharge + self.awb_fee 

    def total_sl_kali_vat(self):
        return (Decimal(self.total_sl_two()) * Decimal(1.1/100))

    def sum_sub_val_sl(self):
        return self.total_sl_two() + self.total_sl_kali_vat()

    def handeling_sl_kali_vat(self):
        return (Decimal(self.handling_charges) * Decimal(1.1/100))

    def total_sl_tree(self):
        return self.handling_charges + self.handeling_sl_kali_vat() 

    ####Untuk Vendor Solid Logistik