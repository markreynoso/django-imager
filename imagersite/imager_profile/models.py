from django.db import models
from django.contrib.auth.models import User


class ImagerProfile(models.Model):
    """Create a new imager profile."""
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=11, blank=False)
    website = models.URLField()
    location = models.CharField(max_length=30, blank=False)
    fee = models.DecimalField(decimal_places=2, max_digits=6, blank=False)
    CAMERAS = {
        ('CANON', 'Canon'),
        ('NIKON', 'Nikon'),
        ('SONY', 'Sony'),
        ('FUJIFILM', 'Fujifilm')
    }
    camera = models.CharField(
        max_length=4,
        choices=CAMERAS,
        default='CANON'
    )
    SERVICES = {
        ('WEDDINGS', 'Weddings'),
        ('SCHOOL', 'School'),
        ('FAMILY', 'Family'),
        ('BABIES', 'Babies'),
        ('NATURE', 'Nature'),
        ('ABSTACT', 'Abstract'),
        ('OTHER', 'Other')
    }
    services = models.CharField(
        max_length=7,
        choices=SERVICES,
        default='OTHER'
    )
    bio = models.TextField()
    PHOTO_STYLES = {
        ('BW', 'Black and white'),
        ('COLOR', 'Color'),
        ('STILL', 'Still'),
        ('ACTION', 'Action'),
    }
    photo_styles = models.CharField(
        max_length=4,
        choices=PHOTO_STYLES,
        default='COLOR'
    )
