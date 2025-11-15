from django.db import models
from django.core.validators import FileExtensionValidator

class EmailMessage(models.Model):

    text = models.TextField(blank=True, null=True)
    data_req = models.DateTimeField(auto_now_add=True)
    ai_response = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    
    file = models.FileField(
        upload_to= 'uploads/',
        blank=True,    
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'txt'])]
    )
    
    def __str__(self):
        return super().__str__()