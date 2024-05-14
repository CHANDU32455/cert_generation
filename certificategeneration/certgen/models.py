from django.db import models
import uuid

class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    heading = models.CharField(max_length=100,null=False, blank=False)
    certificate_about = models.TextField(max_length=150, blank=False,null=False )
    certificant_name = models.CharField(max_length=100, blank=False,null=False )
    issue_date = models.DateField(default='2024-01-01')
    company_name = models.CharField(max_length=100, blank=False,null=False )
    certificate_provider_name = models.CharField(max_length=100, blank=False,null=False)

    def __str__(self):
        return str(self.id)  # uid generated is actually a alphanumerical stuff. we are treating it to string.
            
class BulkCertificates(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    heading = models.CharField(max_length=100, blank=False, null=False)
    certificate_about = models.TextField(max_length=150, blank=False, null=False)
    usernames = models.FileField(upload_to='usernamefiles/', blank=False, null=False)
    issue_date = models.DateField(default='2024-01-01')
    company_name = models.CharField(max_length=100, blank=False, null=False)
    certificate_provider_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    number_of_certificates = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.id)