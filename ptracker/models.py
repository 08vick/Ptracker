from datetime import timedelta

from django.db import models

class Pregnancy(models.Model):
    user_name = models.CharField(max_length=100)
    lmp_date = models.DateField()
    baby_birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user_name

    def save(self, *args, **kwargs):
        if not self.baby_birth_date:  # If birthdate is not provided, calculate it
            self.baby_birth_date = self.lmp_date + timedelta(days=280)  # 280 days (40 weeks) from LMP
        super().save(*args, **kwargs)

    def get_immunization_schedule(self):
        """Return a simple immunization schedule based on baby's birthdate."""
        if not self.baby_birth_date:
            return None  # If baby_birth_date is not set, return None to prevent errors
        schedule = {
            'BCG (At Birth)': self.baby_birth_date,
            'Polio (OPV0)': self.baby_birth_date,
            'Hepatitis B (At Birth)': self.baby_birth_date,
            'DTP1 (6 Weeks)': self.baby_birth_date + timedelta(weeks=6),
            'DTP2 (10 Weeks)': self.baby_birth_date + timedelta(weeks=10),
            'DTP3 (14 Weeks)': self.baby_birth_date + timedelta(weeks=14),
            'Polio (OPV1)': self.baby_birth_date + timedelta(weeks=6),
            'Polio (OPV2)': self.baby_birth_date + timedelta(weeks=10),
            'Polio (OPV3)': self.baby_birth_date + timedelta(weeks=14),
            'Measles (MCV, 9 months)': self.baby_birth_date + timedelta(weeks=39),  # 9 months = 39 weeks
        }
        return schedule
