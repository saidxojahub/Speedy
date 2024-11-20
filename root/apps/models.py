from django.db import models

class SpeedTestResult(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    speed_mbps = models.FloatField()

    def __str__(self):
        return f"{self.speed_mbps} Mbps at {self.timestamp}"