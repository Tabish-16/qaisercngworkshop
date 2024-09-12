
from django.db import models


from django.db import models

class Oil_Companies(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True) 
    purchase_price  = models.CharField(max_length=200, null=True, blank=True)
    sale_price = models.CharField(max_length=200, null=True,blank=True) 
    rack_no = models.CharField(max_length=100,blank=True,null=True,default=0)
    total_products = models.PositiveIntegerField(null=True, blank=True, default=0)

    def calculate_profit(self):
        try:
            profit = int(self.sale_price) - int(self.purchase_price)
        except (ValueError, TypeError):
            profit = None  # Handle the case where the prices aren't valid integers
        return profit
    
    def save(self, *args, **kwargs):
        # Before saving, calculate the profit
        self.profit = self.calculate_profit()
        super(Oil_Companies, self).save(*args, **kwargs)

    profit = models.IntegerField(null=True, blank=True)  # To store profit in the database

    def __str__(self):
        return self.name
    
    
class Spare_Parts(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    purchase_price  = models.CharField(max_length=200,null=True,blank=True)
    sale_price = models.CharField(max_length=200,null=True,blank=True)
    rack_no = models.CharField(max_length=100,blank=True,null=True,default=0)
    total_products = models.PositiveIntegerField(null=True, blank=True, default=0)

    def calculate_profit(self):
        try:
            profit = int(self.sale_price) - int(self.purchase_price)
        except (ValueError, TypeError):
            profit = None  # Handle the case where the prices aren't valid integers
        return profit
    
    def save(self, *args, **kwargs):
        # Before saving, calculate the profit
        self.profit = self.calculate_profit()
        super(Spare_Parts, self).save(*args, **kwargs)

    profit = models.IntegerField(null=True, blank=True)  # To store profit in the database
    
    def __str__(self):
        return self.name
    
    
class Body_Parts(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    purchase_price  = models.CharField(max_length=200,null=True,blank=True)
    sale_price = models.CharField(max_length=200,null=True,blank=True)
    rack_no = models.CharField(max_length=100,blank=True,null=True,default=0)
    total_products = models.PositiveIntegerField(null=True, blank=True, default=0)

    def calculate_profit(self):
        try:
            profit = int(self.sale_price) - int(self.purchase_price)
        except (ValueError, TypeError):
            profit = None  # Handle the case where the prices aren't valid integers
        return profit
    
    def save(self, *args, **kwargs):
        # Before saving, calculate the profit
        self.profit = self.calculate_profit()
        super(Body_Parts, self).save(*args, **kwargs)

    profit = models.IntegerField(null=True, blank=True)  # To store profit in the database
    
    def __str__(self):
        return self.name
    
    
class CNG_Parts(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    purchase_price  = models.CharField(max_length=200,null=True,blank=True)
    sale_price = models.CharField(max_length=200,null=True,blank=True)
    rack_no = models.CharField(max_length=100,blank=True,null=True,default=0)
    total_products = models.PositiveIntegerField(null=True, blank=True, default=0)

    
    def calculate_profit(self):
        try:
            profit = int(self.sale_price) - int(self.purchase_price)
        except (ValueError, TypeError):
            profit = None  # Handle the case where the prices aren't valid integers
        return profit
    
    def save(self, *args, **kwargs):
        # Before saving, calculate the profit
        self.profit = self.calculate_profit()
        super(CNG_Parts, self).save(*args, **kwargs)

    profit = models.IntegerField(null=True, blank=True)  # To store profit in the database
    
    
    def __str__(self):
        return self.name
    
    
class Kabli_Parts(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    purchase_price  = models.CharField(max_length=200,null=True,blank=True)
    sale_price = models.CharField(max_length=200,null=True,blank=True)
    rack_no = models.CharField(max_length=100,blank=True,null=True,default=0)
    total_products = models.PositiveIntegerField(null=True, blank=True, default=0)

    def calculate_profit(self):
        try:
            profit = int(self.sale_price) - int(self.purchase_price)
        except (ValueError, TypeError):
            profit = None  # Handle the case where the prices aren't valid integers
        return profit
    
    def save(self, *args, **kwargs):
        # Before saving, calculate the profit
        self.profit = self.calculate_profit()
        super(Kabli_Parts, self).save(*args, **kwargs)

    profit = models.IntegerField(null=True, blank=True)  # To store profit in the database
    
    def __str__(self):
        return self.name
    
    
class Silencer(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    purchase_price  = models.CharField(max_length=200,null=True,blank=True)
    sale_price = models.CharField(max_length=200,null=True,blank=True)
    rack_no = models.CharField(max_length=100,blank=True,null=True,default=0)
    total_products = models.PositiveIntegerField(null=True, blank=True, default=0)

    def calculate_profit(self):
        try:
            profit = int(self.sale_price) - int(self.purchase_price)
        except (ValueError, TypeError):
            profit = None  # Handle the case where the prices aren't valid integers
        return profit
    
    def save(self, *args, **kwargs):
        # Before saving, calculate the profit
        self.profit = self.calculate_profit()
        super(Silencer, self).save(*args, **kwargs)

    profit = models.IntegerField(null=True, blank=True)  # To store profit in the database
    
    def __str__(self):
        return self.name
    
    
class Decoration(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    purchase_price  = models.CharField(max_length=200,null=True,blank=True)
    sale_price = models.CharField(max_length=200,null=True,blank=True)
    rack_no = models.CharField(max_length=100,blank=True,null=True,default=0)
    total_products = models.PositiveIntegerField(null=True, blank=True, default=0)

    def calculate_profit(self):
        try:
            profit = int(self.sale_price) - int(self.purchase_price)
        except (ValueError, TypeError):
            profit = None  # Handle the case where the prices aren't valid integers
        return profit
    
    def save(self, *args, **kwargs):
        # Before saving, calculate the profit
        self.profit = self.calculate_profit()
        super(Decoration, self).save(*args, **kwargs)

    profit = models.IntegerField(null=True, blank=True)  # To store profit in the database
    
    def __str__(self):
        return self.name


class Oil_Filter(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    purchase_price  = models.CharField(max_length=200,null=True,blank=True)
    sale_price = models.CharField(max_length=200,null=True,blank=True)
    rack_no = models.CharField(max_length=100,blank=True,null=True,default=0)
    total_products = models.PositiveIntegerField(null=True, blank=True, default=0)

    def calculate_profit(self):
        try:
            profit = int(self.sale_price) - int(self.purchase_price)
        except (ValueError, TypeError):
            profit = None  # Handle the case where the prices aren't valid integers
        return profit
    
    def save(self, *args, **kwargs):
        # Before saving, calculate the profit
        self.profit = self.calculate_profit()
        super(Oil_Filter, self).save(*args, **kwargs)

    profit = models.IntegerField(null=True, blank=True)  # To store profit in the database
    
    def __str__(self):
        return self.name

class Air_Filter(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    purchase_price  = models.CharField(max_length=200,null=True,blank=True)
    sale_price = models.CharField(max_length=200,null=True,blank=True)
    rack_no = models.CharField(max_length=100,blank=True,null=True,default=0)
    total_products = models.PositiveIntegerField(null=True, blank=True, default=0)

    def calculate_profit(self):
        try:
            profit = int(self.sale_price) - int(self.purchase_price)
        except (ValueError, TypeError):
            profit = None  # Handle the case where the prices aren't valid integers
        return profit
    
    def save(self, *args, **kwargs):
        # Before saving, calculate the profit
        self.profit = self.calculate_profit()
        super(Air_Filter, self).save(*args, **kwargs)

    profit = models.IntegerField(null=True, blank=True)  # To store profit in the database
    
    def __str__(self):
        return self.name


class AC_Filter(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    purchase_price  = models.CharField(max_length=200,null=True,blank=True)
    sale_price = models.CharField(max_length=200,null=True,blank=True)
    rack_no = models.CharField(max_length=100,blank=True,null=True,default=0)
    total_products = models.PositiveIntegerField(null=True, blank=True, default=0)

    def calculate_profit(self):
        try:
            profit = int(self.sale_price) - int(self.purchase_price)
        except (ValueError, TypeError):
            profit = None  # Handle the case where the prices aren't valid integers
        return profit
    
    def save(self, *args, **kwargs):
        # Before saving, calculate the profit
        self.profit = self.calculate_profit()
        super(AC_Filter, self).save(*args, **kwargs)

    profit = models.IntegerField(null=True, blank=True)  # To store profit in the database
    
    def __str__(self):
        return self.name        
    

class Whole_Sale(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    purchase_price  = models.CharField(max_length=200,null=True,blank=True)
    sale_price = models.CharField(max_length=200,null=True,blank=True)
    rack_no = models.CharField(max_length=100,blank=True,null=True,default=0)
    total_products = models.PositiveIntegerField(null=True, blank=True, default=0)

    def calculate_profit(self):
        try:
            profit = int(self.sale_price) - int(self.purchase_price)
        except (ValueError, TypeError):
            profit = None  # Handle the case where the prices aren't valid integers
        return profit
    
    def save(self, *args, **kwargs):
        # Before saving, calculate the profit
        self.profit = self.calculate_profit()
        super(Whole_Sale, self).save(*args, **kwargs)

    profit = models.IntegerField(null=True, blank=True)  # To store profit in the database
    
    def __str__(self):
        return self.name         

    
    
class NewEntry(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    phone_number = models.CharField(max_length=100,null=True,blank=True)
    vehicle =  models.CharField(max_length=300,null=True,blank=True)
    registeration_num = models.CharField(max_length=300,null=True,blank=True)
    date = models.DateField()
    last_reading = models.CharField(max_length=500,null=True,blank=True)
    next_reading = models.CharField(max_length=500,null=True,blank=True)
    next_changing_date = models.DateField()
    oil_companies = models.JSONField(null=True,default=dict)
    # oil_quantity = models.CharField(max_length=500,null=True,blank=True)
    # oil_price = models.CharField(max_length=500,null=True,blank=True)
    oil_filter = models.JSONField(null=True,default=dict)
    ac_filter = models.JSONField(null=True,default=dict)
    air_filter = models.JSONField(null=True,default=dict)
    bodyPartEntry = models.JSONField(null=True,default=dict)
    sparePartEntry = models.JSONField(null=True,default=dict)
    cngPartEntry = models.JSONField(null=True,default=dict)
    kabliPartEntry = models.JSONField(null=True,default=dict)
    decorationEntry = models.JSONField(null=True,default=dict)
    silencerEntry = models.JSONField(null=True,default=dict)
    wholeSaleEntry = models.JSONField(null=True,default=dict)
    labour = models.JSONField(null=True,default=dict)
    spare_parts = models.ForeignKey(Spare_Parts,on_delete=models.CASCADE,null=True,blank=True)
    body_parts = models.ForeignKey(Body_Parts,on_delete=models.CASCADE,null=True,blank=True)
    cng_parts = models.ForeignKey(CNG_Parts,on_delete=models.CASCADE,null=True,blank=True)
    kabli_parts = models.ForeignKey(Kabli_Parts,on_delete=models.CASCADE,null=True,blank=True)
    silencer = models.ForeignKey(Silencer,on_delete=models.CASCADE,null=True,blank=True)
    decoration = models.ForeignKey(Decoration,on_delete=models.CASCADE,null=True,blank=True)
    
    
    
    def __str__(self):
        return self.name + ' ' + self.phone_number + ' ' + self.vehicle + ' ' + self.registeration_num

