from django.db import models

# Create your models here.
CURRENCIES_CHOICES = [("CAD", "Canadian Dollar"),("USD", "American Dollar")]
LANGUAGES_CHOICES = [("fr", "French"),("en", "English")]
METHODS_CHOICES = [("oneapi", "oneapi"),("catalyst", "catalyst"), ("telus", "telus"), ("videotron", "videotron")]
TRANSACTIONS_STATUS = [("SUCCESS", "Success"),("FAILED", "Failed"), ("PROGRESSING","Progressing")]

class Client(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    cellnum = models.CharField(max_length=10)
    method = models.CharField(max_length=9,
                              choices=METHODS_CHOICES,
                              default="oneapi")

    def __unicode__(self):
        return u"%s" % self.cellnum

class Transaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    currency = models.CharField(choices=CURRENCIES_CHOICES,
                                default='CAD',
                                max_length=5)
    client = models.ForeignKey(Client, related_name="transactions", blank=True)
    user = models.ForeignKey("auth.User", related_name="transactions", blank=True)
    status = models.CharField(choices=TRANSACTIONS_STATUS,
                                max_length=11,
                                default="PROGRESSING")
    
    class Meta:
        ordering = ('created',)