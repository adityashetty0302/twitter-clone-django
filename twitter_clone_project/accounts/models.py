from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Following(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="current_user")
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name="target")

    class Meta:
        unique_together = ("current_user", "target")
