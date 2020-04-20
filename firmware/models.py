from django.db import models


class ServerFirmware(models.Model):
    nameVersion = models.CharField(max_length=20)
    version = models.CharField(max_length=10)
    buildVersion = models.IntegerField()
    updateDate = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='server_firmware')

    def __str__(self):
        return f'{self.nameVersion} {self.version}'

    class Meta:
        verbose_name_plural = 'Firmware del servidor'


class EncoderFirmware(models.Model):
    nameVersion = models.CharField(max_length=20)
    version = models.CharField(max_length=10)
    buildVersion = models.IntegerField()
    updateDate = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='encoder_firmware')

    def __str__(self):
        return f'{self.nameVersion} {self.version}'

    class Meta:
        verbose_name_plural = 'Firmware del encoder'
