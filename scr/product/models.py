from django.db import models
from django.utils.text import slugify

from django.utils.translation import gettext as _
# Create your models here.

    

class Product(models.Model):
    PRDName = models.CharField(max_length=100,verbose_name= _ ("product name"))
    PRDCategory = models.ForeignKey("Category", verbose_name= _("product category"), on_delete=models.CASCADE,null=True,blank=True)
    PRDVariant = models.ForeignKey("settings.Variant", verbose_name= _("product Variant"), on_delete=models.CASCADE,null=True,blank=True)
    PRDDesc = models.TextField(verbose_name= _("product description"))
    PRDImage =models.ImageField(upload_to = 'product_image',verbose_name= _("product images"),null=True,blank=True)
    PRDPrice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name= _("price"))
    PRDDiscountprice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name= _("discountprice"),null=True,blank=True)
    PRDCost = models.DecimalField( max_digits=5, decimal_places=2,verbose_name= _("cost"),null=True,blank=True)
    PRDCreated = models.DateTimeField(verbose_name= _("created at"),null=True,blank=True)
    PRDBrand = models.ForeignKey("settings.Brand", verbose_name= _("product brand"), on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.PRDName
    
    PRDSlug = models.SlugField(unique=True,blank=True)
    def save(self, *args, **kwargs):
        if not self.PRDSlug:
            self.PRDSlug = slugify(self.PRDName)
        super(Product, self).save(*args, **kwargs)
        

    
class ProductImage (models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name= _("product"))
    PRDIImage = models.ImageField(upload_to = 'product_image',verbose_name= _("product images"))

    def __str__(self):
        return str(self.PRDIProduct)
    
    
class Category(models.Model):
    CATName = models.CharField(verbose_name= _("product category"), max_length=50)
    CATParent = models.ForeignKey('self', verbose_name= _("parent"),limit_choices_to={'CATParent__isnull':True}, on_delete=models.CASCADE,null=True,blank=True)
    CATDesc = models.TextField()
    CATImg = models.ImageField(verbose_name= _("image"), upload_to='category')

    def __str__(self):
        return str(self.CATName)



class Product_Alternative(models.Model):

    PALTProduct = models.ForeignKey(Product,verbose_name=("Product"),related_name='main_product',on_delete=models.CASCADE)
    PALTAlternative = models.ManyToManyField(Product, verbose_name=("Product Alternativ"),related_name='Prodzuct_Alternativ')



    def __str__(self):
        return str(self.PALTProduct)


class Product_Accessories(models.Model):
    
    PACSProduct = models.ForeignKey(Product,verbose_name=("Product"),related_name='main_accproduct',on_delete=models.CASCADE)
    PACSAccessories = models.ManyToManyField(Product, verbose_name=("Product Accessories"),related_name='Product_Accessories')

    


    def __str__(self):
        return str(self.PACSProduct)









