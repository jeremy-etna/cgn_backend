from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.conf import settings
from users.models.artist import Artist
from users.models.company import Company
from django.utils import timezone
from django.db import models


class UserRole(models.TextChoices):
    ARTIST = 'artist', 'artist'
    COMPANY = 'company', 'company'


class SkillLevel(models.TextChoices):
    NEVER_PRACTICED = 'Never practiced', '1 - Never practiced'
    NOVICE = 'Novice', '2 - Novice'
    ADVANCED_BEGINNER = 'Advanced Beginner', '3 - Advanced, Beginner'
    COMPETENT = 'Competent', '4 - Competent'
    PROFICIENT = 'Proficient', '5 - Proficient'
    EXPERT = 'Expert', '6 - Expert'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, blank=False)
    register_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    user_role = models.CharField(max_length=30, choices=UserRole.choices)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_role']
    objects = CustomUserManager()

    def __str__(self):
        return self.email


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        if instance.user_role == 'artist':
            Artist.objects.create(user=instance)
            Coordinate.objects.create(user=instance)
            Mobility.objects.create(user=instance)
            Contract.objects.create(user=instance)
            Administrative.objects.create(user=instance)
            SocialMedia.objects.create(user=instance)
            Sector.objects.create(user=instance)
            Competence.objects.create(user=instance)
            Software.objects.create(user=instance)

        elif instance.user_role == 'company':
            Company.objects.create(user=instance)
            Coordinate.objects.create(user=instance)
            Mobility.objects.create(user=instance)
            Contract.objects.create(user=instance)
            Administrative.objects.create(user=instance)
            SocialMedia.objects.create(user=instance)
            Sector.objects.create(user=instance)
            Competence.objects.create(user=instance)
            Software.objects.create(user=instance)


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)


class Coordinate(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    street_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)


class Mobility(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    remote = models.BooleanField(default=False)
    mobility = models.BooleanField(default=False)


class Administrative(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    spectacle_number = models.CharField(max_length=10, blank=True)
    siret_number = models.CharField(max_length=14, blank=True)
    price = models.CharField(max_length=5, blank=True)


class Contract(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cdd = models.BooleanField(default=False)
    cdi = models.BooleanField(default=False)
    stage = models.BooleanField(default=False)
    freelance = models.BooleanField(default=False)
    intermittent = models.BooleanField(default=False)
    alternate = models.BooleanField(default=False)


class SocialMedia(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    website = models.URLField(max_length=255, blank=True)
    youtube = models.URLField(max_length=255, blank=True)
    linkedin = models.URLField(max_length=255, blank=True)
    instagram = models.URLField(max_length=255, blank=True)
    github = models.URLField(max_length=255, blank=True)


class Sector(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    luxe = models.BooleanField(default=False)
    vfx = models.BooleanField(default=False)
    games = models.BooleanField(default=False)
    motion = models.BooleanField(default=False)
    design = models.BooleanField(default=False)
    architecture = models.BooleanField(default=False)
    animation = models.BooleanField(default=False)


class Competence(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    generalist = models.CharField(max_length=30, choices=SkillLevel.choices)
    conceptart = models.CharField(max_length=30, choices=SkillLevel.choices)
    match_moving = models.CharField(max_length=30, choices=SkillLevel.choices)
    modeling = models.CharField(max_length=30, choices=SkillLevel.choices)
    rigging = models.CharField(max_length=30, choices=SkillLevel.choices)
    animating = models.CharField(max_length=30, choices=SkillLevel.choices)
    texturing = models.CharField(max_length=30, choices=SkillLevel.choices)
    surfacing = models.CharField(max_length=30, choices=SkillLevel.choices)
    rendering = models.CharField(max_length=30, choices=SkillLevel.choices)
    compositing = models.CharField(max_length=30, choices=SkillLevel.choices)
    rotoscopy = models.CharField(max_length=30, choices=SkillLevel.choices)
    video_editing = models.CharField(max_length=30, choices=SkillLevel.choices)
    motionDesign = models.CharField(max_length=30, choices=SkillLevel.choices)
    technical_director = models.CharField(max_length=30, choices=SkillLevel.choices)
    developer = models.CharField(max_length=30, choices=SkillLevel.choices)
    production_manager = models.CharField(max_length=30, choices=SkillLevel.choices)
    producer = models.CharField(max_length=30, choices=SkillLevel.choices)
    coordinator = models.CharField(max_length=30, choices=SkillLevel.choices)


class Software(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photoshop = models.CharField(max_length=30, choices=SkillLevel.choices)
    afterEffects = models.CharField(max_length=30, choices=SkillLevel.choices)
    premiere = models.CharField(max_length=30, choices=SkillLevel.choices)
    substancePainter = models.CharField(max_length=30, choices=SkillLevel.choices)
    substanceDesigner = models.CharField(max_length=30, choices=SkillLevel.choices)
    lightroom = models.CharField(max_length=30, choices=SkillLevel.choices)
    Coat = models.CharField(max_length=30, choices=SkillLevel.choices)
    max = models.CharField(max_length=30, choices=SkillLevel.choices)
    affinityDesigner = models.CharField(max_length=30, choices=SkillLevel.choices)
    affinityPhoto = models.CharField(max_length=30, choices=SkillLevel.choices)
    akeytsu = models.CharField(max_length=30, choices=SkillLevel.choices)
    Arnold = models.CharField(max_length=30, choices=SkillLevel.choices)
    blender = models.CharField(max_length=30, choices=SkillLevel.choices)
    cinema4d = models.CharField(max_length=30, choices=SkillLevel.choices)
    clarisseIfx = models.CharField(max_length=30, choices=SkillLevel.choices)
    clipStudioPaint = models.CharField(max_length=30, choices=SkillLevel.choices)
    corelpainter = models.CharField(max_length=30, choices=SkillLevel.choices)
    dazStudio = models.CharField(max_length=30, choices=SkillLevel.choices)
    gaea = models.CharField(max_length=30, choices=SkillLevel.choices)
    gimp = models.CharField(max_length=30, choices=SkillLevel.choices)
    gravitySketch = models.CharField(max_length=30, choices=SkillLevel.choices)
    houdini = models.CharField(max_length=30, choices=SkillLevel.choices)
    illustrator = models.CharField(max_length=30, choices=SkillLevel.choices)
    infinitePainter = models.CharField(max_length=30, choices=SkillLevel.choices)
    keyshot = models.CharField(max_length=30, choices=SkillLevel.choices)
    krita = models.CharField(max_length=30, choices=SkillLevel.choices)
    mangaStudio = models.CharField(max_length=30, choices=SkillLevel.choices)
    mari = models.CharField(max_length=30, choices=SkillLevel.choices)
    marmoset = models.CharField(max_length=30, choices=SkillLevel.choices)
    marvelousDesigner = models.CharField(max_length=30, choices=SkillLevel.choices)
    maya = models.CharField(max_length=30, choices=SkillLevel.choices)
    mentalRay = models.CharField(max_length=30, choices=SkillLevel.choices)
    moi3d = models.CharField(max_length=30, choices=SkillLevel.choices)
    modo = models.CharField(max_length=30, choices=SkillLevel.choices)
    mudbox = models.CharField(max_length=30, choices=SkillLevel.choices)
    nuke = models.CharField(max_length=30, choices=SkillLevel.choices)
    paintToolSai = models.CharField(max_length=30, choices=SkillLevel.choices)
    procreate = models.CharField(max_length=30, choices=SkillLevel.choices)
    quixelSuite = models.CharField(max_length=30, choices=SkillLevel.choices)
    revit = models.CharField(max_length=30, choices=SkillLevel.choices)
    rhino = models.CharField(max_length=30, choices=SkillLevel.choices)
    sketchbookPro = models.CharField(max_length=30, choices=SkillLevel.choices)
    sketchup = models.CharField(max_length=30, choices=SkillLevel.choices)
    speedtree = models.CharField(max_length=30, choices=SkillLevel.choices)
    terragen = models.CharField(max_length=30, choices=SkillLevel.choices)
    unity = models.CharField(max_length=30, choices=SkillLevel.choices)
    unrealEngine = models.CharField(max_length=30, choices=SkillLevel.choices)
    vray = models.CharField(max_length=30, choices=SkillLevel.choices)
    zbrush = models.CharField(max_length=30, choices=SkillLevel.choices)
    xnormal = models.CharField(max_length=30, choices=SkillLevel.choices)
    davinci = models.CharField(max_length=30, choices=SkillLevel.choices)
    resolve = models.CharField(max_length=30, choices=SkillLevel.choices)
    octaneRender = models.CharField(max_length=30, choices=SkillLevel.choices)
    redshift = models.CharField(max_length=30, choices=SkillLevel.choices)
    flame = models.CharField(max_length=30, choices=SkillLevel.choices)
    fusion = models.CharField(max_length=30, choices=SkillLevel.choices)
    natron = models.CharField(max_length=30, choices=SkillLevel.choices)
    meshlab = models.CharField(max_length=30, choices=SkillLevel.choices)
    meshroom = models.CharField(max_length=30, choices=SkillLevel.choices)
    pftrack = models.CharField(max_length=30, choices=SkillLevel.choices)
    equalizer = models.CharField(max_length=30, choices=SkillLevel.choices)
