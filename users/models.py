from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser


class ClientChoice(Enum):
    CLIENT = ("Client",)
    PILOT = "Pilot"


class CustomUser(AbstractUser):
    user_type = models.CharField(
        max_length=25, choices=[("What role are you?", 0), ("Client", 1), ("Pilot", 2)]
    )
    tel_number = models.CharField(max_length=15, help_text="Enter phone number")

    class Meta:
        verbose_name = "User"
        verbose_name_plural  = "User"
