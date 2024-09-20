from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_code = models.CharField(max_length=250, blank=True, null=True)  
    
    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = 'Product'
        verbose_name = 'Product'
        verbose_name_plural = 'Product'
