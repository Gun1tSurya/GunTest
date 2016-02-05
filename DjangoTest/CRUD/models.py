from django.db import models

# Create your models here.

class Invoice(models.Model):
    customer = models.CharField(max_length=100,blank=False)
    date = models.DateTimeField(blank=True,auto_now_add=True)
    total_quantity = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=5,decimal_places=2)

    def __unicode__(self):
        return self.customer

class Transaction(models.Model):
    product = models.CharField(max_length=100,blank=False)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    line_total  = models.DecimalField(max_digits=10,decimal_places=2)
    invoice_id = models.ForeignKey(Invoice,related_name='transactions')

    def __unicode__(self):
        return self.product

