from django.db import models
from django.core.validators import FileExtensionValidator

class EmailMessage(models.Model):

    text = models.TextField(blank=True, null=True)
    
    file = models.FileField(
        upload_to= 'uploads/',
        blank=True,    
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'txt'])]
    )
    
    def __str__(self):
        return super().__str__()