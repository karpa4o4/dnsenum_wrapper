from django.db import models

class Scan(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('in_progress', 'In progress'),
        ('successeded', 'Successeded'),
        ('failed', 'Failed')
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICE, 
                              default='pending')
    result = models.TextField(null=True, blank=True)