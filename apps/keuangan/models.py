from django.db import models
from apps.core.models import AccountsUser as user
from apps.home.models import Cabang

ITEM_JURNAL = (
    ('parkir','PARKIR'),('bbm','BBM'),('materai','MATERAI'),('fotocopy','FOTO COPY'),
    ('lingkungan','LINGKUNGAN'),('sumbangan','SUMBANGAN'),('perlengkapan','PERLENGKAPAN'),
    ('konsumsi','KONSUMSI'),('majalah','MAJALAH'),('listrik','LISTRIK'),('lain_lain','LAIN_LAIN'),
    ('telepon','TELEPON'),('pdam','PDAM'),('sewa','SEWA'),('gaji','GAJI'),('transport','TRANSPORT'),
    ('peralkantor','PERALKANTOR'),('adm_bank','ADM BANK'),('pengiriman','PENGIRIMAN'),
    ('penjualan_materai','PENJUALAN MATERAI'),('pembelian_materai','Pembelian Materai'),('entertaint','ENTERTAINT'),
)

AKUN_PILIH = (
     ('519','Beban Transportasi & Perjalan Dinas'),('520','Beban Sewa'),('521','Beban Perlengkapan'),
     ('523','Beban Dokumentasi'),('525','Beban Pembinaan Lingkungan'),('526','Beban Konsumsi'),('527','Beban Sumbangan'),
     ('528','Beban Iuran & Ijin Lembaga Pemerintah'),('529','Beban Pemeliharaan & Perbaikan Peralatan Kantor'),
     ('530','Beban Pemeliharaan & Perbaikan Peralatan Gedung'),
     ('531','Transportasi'),('532','Beban Pemeliharaan & perbaikan Gedung'),('537','Beban Promosi'),('539','Beban Adm % Umum Lain-Lain')
)

REJECT_CHOICES =(
    ('1','Reject'),('3','Lanjut')
)

JS_TRANSAKSI =(('0','--PILIH--'),('1','KAS'),('2','BANK BSI'),)

JS_TRANSAKSI_BANK =(('1','BANK'),)

JNS_BIAYA = (
    ('',''),('1','KAS'),('2','UANG MUKA'),
)

STATUS_AKUN =(('0','Tidak Aktif'),('1','Aktif'),)

JENIS_AKUN =(('A','AKTIVA'),('P','PASSIVA'),('L','RUGI DAN LABA'))

LAPORAN_AKUN =(('A','AKTIVA'),('P','PASSIVA'),('E','EKUITAS'),('PO','PENDAPATAN OPS'),
    ('BO','BEBAN OPS'),('PNO','PENDAPATAN NON OPS'),('BNO','BEBAN NON OPS'),
    ('K','KONTIGEN'),('KS','KONTIGENSI'),)

J_STATUS = (
    ('0','NON BANK'),('1','BANK'),('2','J.Pendapatan'),
)

class Tbl_Akun(models.Model):
    no_urut = models.IntegerField(null=True, blank=True, editable=False)
    kode_guna = models.CharField(max_length=15)
    header_parent = models.ForeignKey('self', null=True, blank=True,on_delete=models.CASCADE)
    coa = models.CharField(max_length=15)
    deskripsi = models.CharField(max_length=5000)    
    saldo_awal = models.DecimalField(null=True, blank=True,max_digits =18,decimal_places = 2)
    status = models.CharField(max_length=10, choices=STATUS_AKUN)
    jenis = models.CharField(max_length=10, choices=JENIS_AKUN,blank=True,null=True)
    view_unit = models.CharField(max_length=10)
    kode_cabang=models.IntegerField(null=True)
    view_cabang = models.CharField(max_length=10)
    tanggal = models.DateField(null=True, blank=True)
    saldo_akhir = models.DecimalField(null=True, blank=True,max_digits =11,decimal_places = 2)
    layer = models.CharField(max_length=5,null=True,blank=True)
    jenis_laporan = models.CharField(max_length=30, choices=LAPORAN_AKUN)

    class Meta:
        db_table = "tbl_akun"

    def is_child(self):
        return self.tbl_akun_set.all().count() == 0

    def __str__(self):
        return '%s-%s' %(self.coa, self.deskripsi)


def number():
    kode = 1000000
    no = Jurnal.objects.all().count()
    if no == None:
      return 1
    else:
      return no + 1 + kode

class BiayaMapper(models.Model):
    item = models.CharField(max_length=50,null=True,blank=True,choices=ITEM_JURNAL)
    apcabang = models.ForeignKey(Cabang,on_delete=models.CASCADE)
    coa_debet = models.ForeignKey(Tbl_Akun,related_name="+",blank=True,null=True,on_delete=models.CASCADE)
    coa = models.ForeignKey(Tbl_Akun,related_name="+",blank=True,null=True,on_delete=models.CASCADE)
    coa_uk = models.ForeignKey(Tbl_Akun,related_name="+",blank=True,null=True,on_delete=models.CASCADE)
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)
    cu = models.ForeignKey(user, related_name='cu_mep', null=True,on_delete=models.CASCADE)
    mu = models.ForeignKey(user, related_name='mu_mep', null=True,on_delete=models.CASCADE)


    class Meta:
       db_table = 'biayamapper'

class BiayaPusat(models.Model):
    cabang = models.ForeignKey(Cabang,on_delete=models.CASCADE,null=True)
    tanggal = models.DateField(null=True)
    saldo_awal = models.FloatField(default=0)
    saldo_akhir =  models.FloatField(default=0)
    
    penerimaan_saldo = models.FloatField(default=0)

    listrik = models.FloatField(default=0)
    ket_listrik= models.CharField(max_length=50 , null=True, blank=True)
    jenis_transaksi_listrik= models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)

    pdam = models.FloatField(default=0)
    ket_pdam= models.CharField(max_length=50 , null=True, blank=True)
    jenis_transaksi_pdam =  models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)
    telpon = models.FloatField(default=0)
    ket_telpon= models.CharField(max_length=50 , null=True, blank=True)
    jenis_transaksi_telepon = models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)
    foto_copy = models.FloatField(null=True,blank=True,default=0)
    ket_foto_copy= models.CharField(max_length=50 , null=True, blank=True)
    jenis_transaksi_foto_copy =  models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)
    majalah = models.FloatField(default=0)
    ket_majalah= models.CharField(max_length=50 , null=True, blank=True)
    jenis_transaksi_majalah =  models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)
    palkir = models.FloatField(default=0)
    ket_palkir= models.CharField(max_length=50 , null=True, blank=True)
    jenis_transaksi_palkir =  models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)
    bbm = models.FloatField(default=0)
    ket_bbm= models.CharField(max_length=50 , null=True, blank=True)
    jenis_transaksi_bbm =  models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)
    
    
    pemb_lingkungan = models.FloatField(default=0)
    ket_pemb_lingkungan = models.CharField(max_length=50 , null=True, blank=True)
    jenis_transaksi_pemb_lingkungan =  models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)

    sumbangan= models.FloatField(default=0)
    ket_sumbangan = models.CharField(max_length=50 , null=True, blank=True)
    jenis_transaksi_sumbangan =  models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)

    perlengkapan = models.FloatField(default=0)
    ket_perlengkapan = models.CharField(max_length=50 , null=True, blank=True)
    jenis_transaksi_perlengkapan = models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)
    
    konsumsi = models.FloatField(default=0)
    ket_konsumsi = models.CharField(max_length=50 , null=True, blank=True)
    jenis_transaksi_konsumsi = models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)
    ket_penambahan_uk= models.CharField(max_length=50 , null=True, blank=True)
    ket_penambahan_saldo= models.CharField(max_length=50 , null=True, blank=True)

    pengembalian_uk = models.FloatField(default=0)
    ket_pengembalian_uk = models.CharField(max_length=50 , null=True, blank=True)
    penambahan_uk = models.FloatField(default=0)
    pengembalian_saldo = models.FloatField(default=0)
    penambahan_saldo = models.FloatField(default=0)
    ket_pengembalian_saldo= models.CharField(max_length=50 , null=True, blank=True)
    js_trans = models.CharField(max_length=2,choices=JS_TRANSAKSI,blank=True,null=True)
    js_trans_kembali = models.CharField(max_length=20 , null=True, blank=True,default=None)

    jenis_transaksi_biaya_bank = models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)
    biaya_bank = models.FloatField(default=0)
    ket_biaya_bank = models.CharField(max_length=50 , null=True, blank=True)

    jenis_transaksi_pengiriman = models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)
    pengiriman = models.FloatField(default=0)
    ket_pengiriman = models.CharField(max_length=50 , null=True, blank=True)

    jenis_transaksi_lain_lain = models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)
    lain_lain = models.FloatField(default=0)
    ket_lain_lain = models.CharField(max_length=50 , null=True, blank=True)
    
    kas_kecil = models.FloatField(default=0)
    ket_kas_kecil = models.CharField(max_length=50 , null=True, blank=True)
    jenis_transaksi_kas_kecil = models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)

    jenis_transaksi_entertaint = models.CharField(max_length=2,choices=JNS_BIAYA,blank=True,null=True)
    entertaint = models.FloatField(default=0)
    ket_entertaint = models.CharField(max_length=50 , null=True, blank=True)
    cu = models.ForeignKey(user, related_name='cu_biaya', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    mu = models.ForeignKey(user, related_name='mu_biaya', editable=False, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table="biayapusat"
        verbose_name="BiayaPusat"
        ordering = ['-tanggal']

class Jurnal(models.Model):
    nobukti= models.CharField(default=number,max_length=350,blank=True, null=True)
    kre_jurnal = models.IntegerField(blank=True, null=True)
    keterangan_transaksi = models.CharField(max_length=500 , null=True, blank=True)
    id_transaksi = models.CharField(max_length=500 , null=True, blank=True)
    object_id = models.IntegerField(blank =True,null=True)
    diskripsi = models.CharField(max_length=200, blank=True, null=True)
    kode_cabang = models.CharField(max_length=5,blank=True,null=True)
    tgl_trans = models.DateField()
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)
    cu = models.ForeignKey(user, related_name='jurnal_creator', null=True,on_delete=models.CASCADE)
    mu = models.ForeignKey(user, related_name='jurnal_modifier', null=True,on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.id,self.nobukti)

    class Meta:
        db_table = "jurnal"


class Tbl_Transaksi(models.Model):
    #id_coa = models.ForeignKey(Tbl_Akun,null =True,blank=True,on_delete=models.CASCADE)
    jurnal = models.ForeignKey(Jurnal,on_delete=models.CASCADE)
    no_trans = models.IntegerField(null=True, blank=True)
    jenis = models.CharField(max_length=100)
    debet = models.IntegerField()
    kredit = models.IntegerField()
    id_cabang = models.IntegerField()
    id_product  = models.IntegerField(null= True)
    
    status_jurnal = models.IntegerField()
    status_reject = models.CharField(max_length=2,choices=REJECT_CHOICES,blank=True,null=True)
    user = models.ForeignKey(user, related_name='c_tbl_transaksi', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    tgl_trans = models.DateField()
    status_posting = models.IntegerField(blank=True,null=True)
    deskripsi = models.CharField(max_length=500, blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True)
    posting = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        db_table = "tbl_transaksi"

    def __str__(self):
        return '%s' % (self.id)

class Jurnal_History(models.Model):
    diskripsi = models.CharField(max_length=200, blank=True, null=True)
    no_akad = models.IntegerField(default=number,blank=True, null=True)
    tgl_trans = models.DateField(blank=True, null=True)
    j_status = models.CharField(max_length=1, choices=J_STATUS,default= 0)
    object_id = models.IntegerField(blank =True,null=True)
    kode_cabang = models.CharField(max_length=5,blank=True,null=True)
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)
    cu = models.ForeignKey(user, related_name='+', null=True,on_delete=models.CASCADE)
    mu = models.ForeignKey(user, related_name='+', null=True,on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s' % (self.id)

    class Meta:
        db_table = "jurnal_history"


class Tbl_Transaksi_History(models.Model):
    deskripsi = models.CharField(max_length=500, blank=True, null=True)
    id_coa = models.ForeignKey(Tbl_Akun,null =True,blank=True,related_name='orders',on_delete=models.CASCADE)
    jurnal_h = models.ForeignKey(Jurnal_History, related_name='ordered_items',on_delete=models.CASCADE)
    no_trans = models.IntegerField(null=True, blank=True)
    jenis = models.CharField(max_length=500)
    debet = models.IntegerField()
    kredit = models.IntegerField()
    id_cabang = models.IntegerField()
    id_cabang_tuju = models.IntegerField(blank=True,null=True)
    id_unit = models.IntegerField()
    id_product  = models.IntegerField()
    status_jurnal = models.IntegerField()
    user = models.ForeignKey(user, related_name='c_tbl_transaksi_h', editable=False, null=True, blank=True,on_delete=models.CASCADE)
    tgl_trans = models.DateField()
    status_posting = models.IntegerField(blank=True,null=True)

    class Meta:
        db_table = "tbl_transaksi_history"