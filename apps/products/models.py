from decimal import Decimal
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import datetime
from apps.core.models import AccountsUser as user

KURS_DUTY =[('1','€'),('2','$'),('3','Rp')]

STATUS_SHIPMENT =[('','--SELECT--'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),
    ('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'), 
    ('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'), ]

DELIVERY_TIMOR_LESTE =[('','--SELECT--'),('3','Hera'),('4','Okusi'),('5','Betano')]

REPORT_DATA =[('','-- Select --'),("1",'View'),("2",'Xls')]

STATUS_DUTY =[('','--Piih--'),("1",'Tidak'),("2",'Ada')]

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
    status =models.CharField(max_length=10,choices=STATUS,null=True,default=0)  # type: ignore
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
    status_kurs = models.CharField(max_length=10,choices=STATUS,default=0)  # type: ignore
    nilai_kurs = models.FloatField(null=True,blank=True)
    simbol = models.CharField(max_length=10,null=True,blank=True)
    tanggal_aktif = models.DateField(null=True,blank=True)
    simbol = models.CharField(max_length=10,null=True,blank=True)
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
    nama_kota = models.CharField(max_length=100,null=True)
    singkatan = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)  # type: ignore
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
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)  # type: ignore
    nilai_kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE,null=True,blank=True)
    singkatan = models.CharField(null=True, max_length=50)
    cu = models.ForeignKey(user, related_name='cu_js', editable=False, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'jasapengiriman'
        verbose_name = 'JasaPengiriman'

    def __str__(self):
        return '%s-%s' %(self.singkatan,self.nama_jasa_pengiriman)        
    

class Produk(models.Model):
    id_prod = models.IntegerField(null=True)
    nama_produk = models.CharField(max_length=100,null=True)
    jumlah_vendor = models.CharField(choices = JUMLAH_VENDOR,max_length=20,null= True,blank=True)
    jenis_produk = models.CharField(choices = JENISPRODUK,max_length=20,null= True,blank= True)
    ####origin
    point_satu = models.ForeignKey(Negara,on_delete=models.CASCADE,null=True, related_name='point_satu' )
    origin_vendor = models.ForeignKey(JasaPengiriman,on_delete=models.CASCADE,null=True,related_name='origin_v1')
    kurs_origin = models.ForeignKey(Kurs,on_delete=models.CASCADE,null=True,related_name='origin_kurs')
    ####Through
    point_dua = models.ForeignKey(Negara,on_delete=models.CASCADE,null=True,related_name='point_dua' )
    through_vendor = models.ForeignKey(JasaPengiriman,on_delete=models.CASCADE,null=True,related_name='Through_v2')
    kurs_through = models.ForeignKey(Kurs,on_delete=models.CASCADE,null=True,related_name='origin_trough')
    ####Destinations
    point_tiga  = models.ForeignKey(Negara,on_delete=models.CASCADE,null=True,blank=True,related_name='point_tiga' )
    destinations_vendor = models.ForeignKey(JasaPengiriman,on_delete=models.CASCADE,null=True,related_name='destinatioin_v3')
    kurs_destinations = models.ForeignKey(Kurs,on_delete=models.CASCADE,null=True,related_name='origin_destinastions')

    tgl_aktif = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)  # type: ignore
    cu = models.ForeignKey(user, related_name='cu_produk', editable=False, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'produk'
        verbose_name= 'Produk'
        verbose_name_plural =verbose_name
    
    def counter_produk(self):
        tot = 0 # type: ignore
        try:
            skr = datetime.date.today()
            count = Produk.objects.filter(tgl_aktif__year=skr.year).count()
            cekkr = Produk.objects.filter(tgl_aktif__year=skr.year).latest('id_prod')
            if count >= 1:
                tot = cekkr.id_prod + 1 # type: ignore
            else:
                tot = 1
        except ObjectDoesNotExist:
            tot = 1
        return tot
    
    def kode_produk(self):
        if self.jumlah_vendor == '1':  # type: ignore
            return '%s %s' %(self.nama_produk,self.point_tiga)# type: ignore
        elif self.jumlah_vendor == '2':# type: ignore
            return '%s %s %s | ( %s %s )' %(self.nama_produk, self.point_satu,self.point_tiga,self.origin_vendor.singkatan,self.destinations_vendor.singkatan)# type: ignore
        else:
            return '%s %s %s Via %s | ( %s %s %s )' %(self.nama_produk, self.point_satu,self.point_tiga,self.point_dua,self.origin_vendor.singkatan,self.through_vendor.singkatan,self.destinations_vendor.singkatan)# type: ignore

    def __str__(self):
        return '%s-%s-%s' %(self.id,self.id_prod, self.kode_produk())# type: ignore

######Khusus Parameter Jual
class ParameterDataBl(models.Model):
    products = models.ForeignKey(('Produk'),on_delete=models.CASCADE)
    vendor = models.ForeignKey(JasaPengiriman,on_delete=models.CASCADE,null=True,blank=True)    
    status_param = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)  # type: ignore
    tgl_aktif_param = models.DateField(blank=True, null=True)
    ########## logistik Indah Sinergi Trading
    min_airfreight_import_handling = models.FloatField(null=True,blank=True)
    max_airfreight_import_handling = models.FloatField(null=True,blank=True)
    price_airfreight_import_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)  # type: ignore

    min_cartage_and_warehouse_charge = models.FloatField(null=True,blank=True)
    max_cartage_and_warehouse_charge = models.FloatField(null=True,blank=True)
    price_cartage_and_warehouse_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)  # type: ignore

    min_export_handling = models.FloatField(null=True,blank=True)
    max_export_handling = models.FloatField(null=True,blank=True)
    price_export_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)  # type: ignore
    
    min_airfreight_sin_dps_dil = models.FloatField(null=True,blank=True)
    max_airfreight_sin_dps_dil = models.FloatField(null=True,blank=True)
    airfreight_sin_dps_dil = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)  # type: ignore

    min_doc_and_clearance = models.FloatField(null=True,blank=True)
    max_doc_and_clearance = models.FloatField(null=True,blank=True)
    price_doc_and_clearance = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    
    min_ground_handling = models.FloatField(null=True,blank=True)
    max_ground_handling = models.FloatField(null=True,blank=True)
    price_ground_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    min_warehouse_charge = models.FloatField(null=True,blank=True)
    max_warehouse_charge = models.FloatField(null=True,blank=True)
    price_warehouse_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    min_handling_charge = models.FloatField(null=True,blank=True)
    max_handling_charge = models.FloatField(null=True,blank=True)
    price_handling_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    min_delivery = models.FloatField(null=True,blank=True)
    max_delivery = models.FloatField(null=True,blank=True)
    price_delivery = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    min_duty_tax = models.FloatField(null=True,blank=True)
    max_duty_tax = models.FloatField(null=True,blank=True)
    price_duty_tax = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    min_tax_handling_charge = models.FloatField(null=True,blank=True)
    max_tax_handling_charge = models.FloatField(null=True,blank=True)
    price_tax_handling_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    ########## logistik Indah Sinergi Trading
    cu = models.ForeignKey(user, related_name='cu_parambl', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'paramdatabl'
        verbose_name= 'ParameterDataBl'
        verbose_name_plural =verbose_name


    def __str__(self):
        return '%s' %(self.id) # type: ignore

    
    

##########Parameter untuk Job
class ParameterData(models.Model):
    products = models.ForeignKey(('Produk'),on_delete=models.CASCADE)
    nilai_kurs = models.ForeignKey(Kurs,on_delete=models.CASCADE,null=True,blank=True)    
    status_param = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0) # type: ignore
    tgl_aktif_param = models.DateField(blank=True, null=True)
    j_vendor = models.CharField(choices = JUMLAH_VENDOR,max_length=20,null= True,blank=True)
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
    ###########Gasti asih Caraka
    min_pcs = models.FloatField(null=True,blank=True,help_text="Gasti asih caraka")
    price_pcs= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Gasti Asih caraka")
    price_high_pcs= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Gasti Asih caraka")
    
    min_weight = models.FloatField(null=True,blank=True,help_text="Gasti asih caraka")
    price_weight = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Gasti Asih caraka")
    price_high_weight = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Gasti Asih caraka")                                       
    
    min_handling = models.FloatField(null=True,blank=True,help_text="Gasti asih caraka",default =0)
    price_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Gasti Asih caraka",default = 0)  # type: ignore
    price_high_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Gasti Asih caraka",default =0)  # type: ignore

    min_transportation_charge = models.FloatField(null=True,blank=True,help_text="Gasti asih caraka",default =0)
    price_transportation_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Gasti Asih caraka",default =0)  # type: ignore
    price_high_transportation_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Gasti Asih caraka",default =0)  # type: ignore
    
    ########Warstila nedherlan
    min_custom_learance_fee_handling= models.FloatField(null=True,blank=True,help_text="Wastila Belanda")
    price_custom_learance_fee_handling= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Wastila Belanda")
    price_high_custom_learance_fee_handling= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Wastila Belanda")
    
    min_heavy_weight_surcharge= models.FloatField(null=True,blank=True,help_text="Wastila Belanda")
    price_heavy_weight_surcharge= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Wastila Belanda")
    price_high_heavy_weight_surcharge= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Wastila Belanda")
    
    min_agent_fee= models.FloatField(null=True,blank=True,help_text="Wastila Belanda")
    price_agent_fee= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Wastila Belanda")
    price_high_agent_fee= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Wastila Belanda")
    
    min_delivery= models.FloatField(null=True,blank=True,help_text="Wastila Belanda")
    price_delivery= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Wastila Belanda")
    price_high_delivery= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="Wastila Belanda")
        
    ########DHL
    min_express_wordwide_nondoc= models.FloatField(null=True,blank=True,help_text="DHl")
    price_express_wordwide_nondoc= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="DHl")
    price_high_express_wordwide_nondoc= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="DHl")
    
    min_fuel_surcharge_dhl= models.FloatField(null=True,blank=True,help_text="DHl")
    price_fuel_surcharge_dhl= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="DHl")
    price_high_fuel_surcharge_dhl= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="DHl")
    
    min_emergency_situation= models.FloatField(null=True,blank=True,help_text="DHl")
    price_emergency_situation= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="DHl")
    price_high_emergency_situation= models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,help_text="DHl")
    
    cu = models.ForeignKey(user, related_name='cu_paramdata', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    cdate = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'parameterdata'
        verbose_name = 'ParameterData'

    def __str__(self):
        return '%s' %(self.id) # type: ignore


class Transaksi(models.Model):
    tanggal = models.DateTimeField(auto_now_add=True)
    no_pekerjaan = models.IntegerField(blank=True,null=True)
    qty = models.IntegerField(blank=True,null=True)
    weight = models.FloatField(null=True,blank=True)
    products = models.ForeignKey(Produk,on_delete=models.CASCADE,null=True,blank=True)
    commodity =models.ForeignKey(Commodity,blank=True,null=True,on_delete= models.CASCADE)
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
                tot = cekkr.no_pekerjaan + 1 # type: ignore
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
    
class AddresInvoice(models.Model):
    nama = models.CharField(max_length=100,null=True)
    alamat = models.CharField(max_length=100,null=True)
    telepon = models.CharField(max_length=20,null=True)
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)  # type: ignore
    cu = models.ForeignKey(user, related_name='cu_addI', editable=False, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'addresinvoice'
        verbose_name = 'AddresInvoice'

    def __str__(self):
        return '%s' %(self.nama)    

class ShipperInvoice(models.Model):
    nama = models.CharField(max_length=100,null=True)
    alamat = models.CharField(max_length=100,null=True,blank=True)
    kota = models.CharField(max_length=100,null=True,blank=True)
    telepon = models.CharField(max_length=20,null=True,blank=True)
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)  # type: ignore
    cu = models.ForeignKey(user, related_name='cu_ssp', editable=False, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'shipersinvoice'
        verbose_name = 'ShipperInvoice'
    
    def __str__(self):
        return '%s %s' %(self.nama, self.kota)    

class ConsigneInvoice(models.Model):
    nama = models.CharField(max_length=100,null=True)
    alamat = models.CharField(max_length=100,null=True,blank=True)
    kota = models.CharField(max_length=100,null=True,blank=True)
    telepon = models.CharField(max_length=20,null=True,blank=True)
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)  # type: ignore
    cu = models.ForeignKey(user, related_name='cu_csg', editable=False, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Consigneinvoice'
        verbose_name = 'ConsigneInvoice' 

    def __str__(self):
        return '%s %s' %(self.nama, self.kota)

class TermInvoice(models.Model):
    nama_term = models.CharField(max_length=100,null=True)                      
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)  # type: ignore
    cu = models.ForeignKey(user, related_name='cu_term', editable=False, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'TermInvoice'
        verbose_name = 'TermInvoice'

    def __str__(self):
        return '%s ' %(self.nama_term)

class DdpInvoice(models.Model):
    nama_ddp = models.CharField(max_length=100,null=True)                      
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)  # type: ignore
    cu = models.ForeignKey(user, related_name='cu_ddp', editable=False, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'DdpInvoice'
        verbose_name = 'DdpInvoice'

    def __str__(self):
        return '%s ' %(self.nama_ddp)

class PicInvoice(models.Model):
    nama_pic = models.CharField(max_length=100,null=True)                      
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)  # type: ignore
    cu = models.ForeignKey(user, related_name='cu_pic', editable=False, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'PicInvoice'
        verbose_name = 'PicInvoice'

    def __str__(self):
        return '%s ' %(self.nama_pic)


class Invoice(models.Model):
    address_header = models.ForeignKey(AddresInvoice,on_delete=models.CASCADE,null=True,related_name='inv_01')
    shipper = models.ForeignKey(ShipperInvoice, verbose_name='Shipper', on_delete=models.CASCADE)
    consignee = models.ForeignKey(ConsigneInvoice, verbose_name='Consigne', on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS,null=True,blank=True,default=0)  # type: ignore

    class Meta:
        db_table = 'Invoice'    
        verbose_name = 'Invoice' 

    def __str__(self):
        return '%s-%s-%s' %(self.address_header,self.shipper,self.consignee)

JFORM =[('','--Select--'),('100','Form1'),('200','Fom2')]    

class MenuInputSale(models.Model):
    jenis_form = models.CharField(("Jenis Form"), max_length=50,choices=JFORM)
    total_shipment = models.CharField(choices=STATUS_SHIPMENT,null=True,blank=True,max_length=50)
    ######## Shifment dua 200 form1
    nb_of_parcels = models.DecimalField(("NB OF PARCE"), max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    gross_weight = models.DecimalField(("Gross Weight"), max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    repecking = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    repecking_price = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    repecking_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    pickup = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    pickup_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    freight_cost = models.DecimalField(("Freight Cost"), max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    freight_cost_price = models.DecimalField(("Freight Cost Price"),max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    freight_cost_qty = models.DecimalField(("Freight Cost QTY"),max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    overweight_charge = models.DecimalField(("Overweight Charge"), max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    overweight_charge_price = models.DecimalField(("Overweight Charge Price"), max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    overweight_charge_qty = models.DecimalField(("Overweight Charge QTY"), max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    insuranse_forms = models.DecimalField(("Insurence"), max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    insuranse_nilai = models.DecimalField(("Insurence Price "), max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    insuranse_pers = models.DecimalField(("Insurence Persen"), max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    ######## Shifment dua 100 form1
    cartage_warehouse_charge_satu =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_dua =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_tiga =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_empat =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_lima =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_enam =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_tujuh =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_delapan =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_sembilan =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_sepuluh =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_sebelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_duabelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_tigabelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_empatbelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_limabelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_enambelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_tujuhbelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_delapanbelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_sembilanbelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    cartage_warehouse_charge_duapuluh =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    price_cartage_warehouse_charge_satu =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_dua =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_tiga =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_empat =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_lima =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_enam =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_tujuh =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_delapan =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_sembilan =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_sepuluh =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_sebelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_duabelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_tigabelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_empatbelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_limabelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_enambelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_tujuhbelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_delapanbelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_sembilanbelas =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_cartage_warehouse_charge_daupuluh =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    airfreight_satu = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_dua = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_tiga = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_empat = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_lima = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_enam = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_tujuh = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_delapan = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_sembilan = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_sepuluh = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_sebelas = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_duabelas = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_tigabelas = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_empatbelas = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_limabelas = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_enambelas = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_tujuhbelas = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_delapanbelas = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_sembilanbelas = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    airfreight_duapuluh = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    
    re_export_shipment_satu = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_satu_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_satu_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    
    re_export_shipment_dua = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_dua_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_dua_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_tiga = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_tiga_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_tiga_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_empat = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_empat_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_empat_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_lima = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_lima_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_lima_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_enam = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_enam_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_enam_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_tujuh = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_tujuh_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_tujuh_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_delapan = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_delapan_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_delapan_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_sembilan = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_sembilan_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_sembilan_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_sepuluh = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_sepuluh_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_sepuluh_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_sebelas = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_sebelas_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_sebelas_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_duabelas = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_duabelas_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_duabelas_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_tigabelas = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_tigabelas_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_tigabelas_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_empatbelas = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_empatbelas_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_empatbelas_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_limabelas = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_limabelas_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_limabelas_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_enambelas = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_enambelas_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_enambelas_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_tujuhbelas = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_tujuhbelas_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_tujuhbelas_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_delapanbelas = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_delapanbelas_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_delapanbelas_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_sembilanbelas = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_sembilanbelas_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_sembilanbelas_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore

    re_export_shipment_duapuluh = models.CharField(max_length=30,null=True,blank=True)
    re_export_shipment_duapuluh_pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    re_export_shipment_duapuluh_qty = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    #########end shiftment

    class Meta:
        db_table='MenuInputSale'

    def __str__(self):
        return '%s' %(self.id) # type: ignore
    

class Sale(models.Model):
    trans = models.ForeignKey(Transaksi,on_delete=models.CASCADE,null=True)
    head_address = models.ForeignKey(AddresInvoice,on_delete=models.CASCADE,null=True,blank=True)
    consigne = models.ForeignKey(ConsigneInvoice,on_delete=models.CASCADE,null=True,blank=True)
    shipper = models.ForeignKey(ShipperInvoice,on_delete=models.CASCADE,null=True,blank=True)

    term = models.ForeignKey(TermInvoice, verbose_name='Term', on_delete=models.CASCADE,null=True,blank=True)
    ddp = models.ForeignKey(DdpInvoice, verbose_name='DDP', on_delete=models.CASCADE,null=True,blank=True)
    pic = models.ForeignKey(PicInvoice, verbose_name='PIC', on_delete=models.CASCADE,null=True,blank=True)
    
    status_sale = models.CharField(choices=STATUS_UPDATE,null=True,blank=True,max_length=50)
    awb = models.CharField(max_length=50,null=True,blank=True)
    warehouse_charge_days = models.CharField(max_length=50,null=True,blank=True)
    tgl_done = models.DateField(null=True,blank=True)
    prod = models.ForeignKey(ParameterDataBl,on_delete=models.CASCADE,null=True,blank=True)
    formsale = models.ForeignKey(MenuInputSale,on_delete=models.CASCADE,null=True,blank=True)
    
    export_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    freight = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_freight = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    doc_clearance = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_doc_clearance = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    ground_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_ground_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    warehouse_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_warehouse_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    handling_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_handling_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    status_duty = models.CharField(choices=STATUS_DUTY,max_length=10,null=True,blank=True)
    delivery = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    price_delivery = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    duty_tax = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore 
    tax_handling_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore 
    shipment_value = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore 
    insurance = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore 
    kurs_duty = models.CharField(choices=KURS_DUTY,max_length=10,null=True,blank=True,default=1) # type: ignore
    etd = models.DateField(null=True,blank=True)
    eta = models.DateField(null=True,blank=True)
    cu = models.ForeignKey(user, related_name='cu_sale', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='sale'

    def __str__(self):
        return '%s' %(self.id) # type: ignore

    def total_sale(self):
        return  self.export_handling + self.freight + self.doc_clearance + self.ground_handling + \
            self.warehouse_charge + self.handling_charge + self.delivery 
    
    def total_duty(self):
        return self.duty_tax + self.tax_handling_charge + self.insurance


JUMLAHREFF=[('','--SELECT--'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),
    ('8','8'),('9','9'),('10','10')]

JUMLAHREFFCS=[('','--SELECT--'),('11','1'),('12','2'),('13','3'),('14','4'),('15','5'),('16','6'),('17','7'),
    ('18','8'),('19','9'),('20','10')]  
    
class RefCustomer(models.Model):
    fkref = models.ForeignKey(Sale, verbose_name=("fkreff"), on_delete=models.CASCADE)
    jumlahreff = models.CharField(choices=JUMLAHREFF,blank=True,null=True,max_length=20)
    jumlahreffcs = models.CharField(choices=JUMLAHREFFCS,blank=True,null=True,max_length=20)
    ref1 = models.CharField(blank=True,null=True,max_length=20 )
    ref2 = models.CharField(blank=True,null=True,max_length=20 )
    ref3 = models.CharField(blank=True,null=True,max_length=20 )
    ref4 = models.CharField(blank=True,null=True,max_length=20 )
    ref5 = models.CharField(blank=True,null=True,max_length=20 )
    ref6 = models.CharField(blank=True,null=True,max_length=20 )
    ref7 = models.CharField(blank=True,null=True,max_length=20 )
    ref8 = models.CharField(blank=True,null=True,max_length=20 )
    ref9 = models.CharField(blank=True,null=True,max_length=20 )
    ref10 = models.CharField(blank=True,null=True,max_length=20)
    ref11 = models.CharField(blank=True,null=True,max_length=20 )
    ref12 = models.CharField(blank=True,null=True,max_length=20 )
    ref13 = models.CharField(blank=True,null=True,max_length=20 )
    ref14 = models.CharField(blank=True,null=True,max_length=20 )
    ref15 = models.CharField(blank=True,null=True,max_length=20 )
    ref16 = models.CharField(blank=True,null=True,max_length=20 )
    ref17 = models.CharField(blank=True,null=True,max_length=20 )
    ref18 = models.CharField(blank=True,null=True,max_length=20 )
    ref19 = models.CharField(blank=True,null=True,max_length=20 )
    ref20 = models.CharField(blank=True,null=True,max_length=20)
    ref21 = models.CharField(blank=True,null=True,max_length=20 )
    ref22 = models.CharField(blank=True,null=True,max_length=20 )
    ref23 = models.CharField(blank=True,null=True,max_length=20 )
    ref24 = models.CharField(blank=True,null=True,max_length=20 )
    ref25 = models.CharField(blank=True,null=True,max_length=20 )
    ref26 = models.CharField(blank=True,null=True,max_length=20 )
    ref27 = models.CharField(blank=True,null=True,max_length=20 )
    ref28 = models.CharField(blank=True,null=True,max_length=20 )
    ref29 = models.CharField(blank=True,null=True,max_length=20 )
    ref30 = models.CharField(blank=True,null=True,max_length=20)
    

    csref1 = models.CharField(blank=True,null=True,max_length=20 )
    csref2 = models.CharField(blank=True,null=True,max_length=20 )
    csref3 = models.CharField(blank=True,null=True,max_length=20 )
    csref4 = models.CharField(blank=True,null=True,max_length=20 )
    csref5 = models.CharField(blank=True,null=True,max_length=20 )
    csref6 = models.CharField(blank=True,null=True,max_length=20 )
    csref7 = models.CharField(blank=True,null=True,max_length=20 )
    csref8 = models.CharField(blank=True,null=True,max_length=20 )
    csref9 = models.CharField(blank=True,null=True,max_length=20 )
    csref10 = models.CharField(blank=True,null=True,max_length=20 )
    csref11 = models.CharField(blank=True,null=True,max_length=20 )
    csref12 = models.CharField(blank=True,null=True,max_length=20 )
    csref13 = models.CharField(blank=True,null=True,max_length=20 )
    csref14 = models.CharField(blank=True,null=True,max_length=20 )
    csref15 = models.CharField(blank=True,null=True,max_length=20 )
    csref16 = models.CharField(blank=True,null=True,max_length=20 )
    csref17 = models.CharField(blank=True,null=True,max_length=20 )
    csref18 = models.CharField(blank=True,null=True,max_length=20 )
    csref19 = models.CharField(blank=True,null=True,max_length=20 )
    csref20 = models.CharField(blank=True,null=True,max_length=20 )
    csref21 = models.CharField(blank=True,null=True,max_length=20 )
    csref22 = models.CharField(blank=True,null=True,max_length=20 )
    csref23 = models.CharField(blank=True,null=True,max_length=20 )
    csref24 = models.CharField(blank=True,null=True,max_length=20 )
    csref25 = models.CharField(blank=True,null=True,max_length=20 )
    csref26 = models.CharField(blank=True,null=True,max_length=20 )
    csref27 = models.CharField(blank=True,null=True,max_length=20 )
    csref28 = models.CharField(blank=True,null=True,max_length=20 )
    csref29 = models.CharField(blank=True,null=True,max_length=20 )
    csref30 = models.CharField(blank=True,null=True,max_length=20 )
    
    class Meta:
        db_table = 'refcustomer'
        verbose_name = 'RefCustomer'


class Job(models.Model):
    tanggal_invoice = models.DateField()# Dipakai Semua vendor
    no_invoice = models.CharField(null=True,blank=True,max_length=50)# Dipakai Semua vendor
    no_invoice_sl_2 = models.CharField(null=True,blank=True,max_length=50)# Dipakai Semua vendor
    no_invoice_sl_3 = models.CharField(null=True,blank=True,max_length=50)# Dipakai Semua vendor
    transaksi = models.ForeignKey(Transaksi,on_delete=models.CASCADE)
    status_job = models.CharField(choices=STATUS_UPDATE,null=True,blank=True,max_length=50)
    tanggal_status = models.DateField(null=True,blank=True) 
    
    vendor = models.ForeignKey(JasaPengiriman,on_delete=models.CASCADE)
    nilai_kurs = models.ForeignKey(Kurs,on_delete=models.CASCADE)
    ########## Khusus Untuk Freight Solutions
    ####Pengiriman Udara
    
    ###### Biaya pengurusan / oprasional dan Udara Untuk Freight Solution dan Shlid
    airfreight = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    handling_charges = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    ##### Biaya Asuransi 
    insurance_security_surcharge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    ##biaya tambahan bahan bakar
    fuel_surcharge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    ###Biaya Penanganan Impor
    import_handling_charges = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    gst_zero_rated = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    ##########Akhir Khusus Untuk Freight Solutions

    ##########Khusus Untuk Sholid Logistik
    ####### Biaya Storage
    storage_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    pjkp2u_sin_dps_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    storage_mcl_e_0389249_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    pjkp2u_dps_dil_at_cost = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    ######### Biaya Storege
    overweight_charges_surcharge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    awb_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)   # type: ignore 
    ########## Akhir Khusus Untuk Sholid Logistik
    ##########Khusus Untuk Sholid Logistik
        
    ############ khusus logistik dili
    ground_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    forklift_for_heavy_cargo = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    custom_clearance = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    delivey_to = models.CharField(choices=DELIVERY_TIMOR_LESTE,max_length=10,null=True,blank=True)
    delivey_to_hera = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    delivey_to_okusi = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    delivey_to_betano = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    akses_bandara_inspeksi = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    handling_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    admin_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore 
    fee_collection = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) # type: ignore
    ############ Akhir khusus logistik dili

    ###########Gasti asih Caraka
    jenis = models.CharField(choices = JENISPRODUK,max_length=20,null= True,blank= True)
    amount = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="Gasti asih caraka")  # type: ignore
    pcs = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="Gasti asih caraka")  # type: ignore
    weight = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="Gasti asih caraka")  # type: ignore
    paking = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="Gasti asih caraka") # type: ignore
    transportation_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="Gasti asih caraka") # type: ignore
    
    ###########LintasNegara
    transit_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="Lintas Negara") # type: ignore
    transportations_charge = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="Lintas Negara") # type: ignore

    ###########AntarLapan
    cbm = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="ANTAR LAPAN") # type: ignore
    twentyft = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="ANTAR LAPAN") # type: ignore
    blfee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="ANTAR LAPAN") # type: ignore
    biaya_peb = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="ANTAR LAPAN") # type: ignore

    ########Warstila nedherlan
    custom_learance_fee_handling = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="Wastila belanda") # type: ignore
    heavy_weight_surcharge =  models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="Wastila belanda") # type: ignore
    agent_fee = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="Wastila belanda") # type: ignore
    delivery = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="Wastila belanda") # type: ignore
    
    ########DHL
    express_wordwide_nondoc =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="DHL") # type: ignore
    fuel_surcharge_dhl =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="DHL") # type: ignore
    emergency_situation  =models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0,help_text="DHL") # type: ignore
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
            self.delivey_to_hera + self.akses_bandara_inspeksi + self.handling_fee + self.admin_fee + self.fee_collection + \
            self.delivey_to_okusi + self.delivey_to_betano
    
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

    def total_lintas_negara(self):
        return self.transit_charge + self.transportations_charge  # type: ignore  

    def total_antarlapan(self):
        return self.cbm + self.twentyft + self.blfee + self.biaya_peb  # type: ignore

    ####Untuk Vendor Solid Logistik