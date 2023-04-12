from django.db import models
from django.conf import settings
from cgnetwork.validators import validate_file_size
from django.core.validators import FileExtensionValidator


SKILL_LEVELS = (
    ('Never used', '1 - Never practiced'),
    ('Novice', '2 - Novice'),
    ('Advanced Beginner', '3 - Advanced Beginner'),
    ('Competent', '4 - Competent'),
    ('Proficient', '5 - Proficient'),
    ('Expert', '6 - Expert')
)


class Artist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # IDENTITY
    avatar = models.ImageField(
        upload_to='avatars',
        default='avatars/artist_default.png',
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
        ])
    title = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    # CONTRACT TYPES
    cdd = models.BooleanField(default=False)
    cdi = models.BooleanField(default=False)
    stage = models.BooleanField(default=False)
    freelance = models.BooleanField(default=False)
    intermittent = models.BooleanField(default=False)
    alternate = models.BooleanField(default=False)
    # URLS
    website = models.URLField(max_length=255, blank=True)
    youtube = models.URLField(max_length=255, blank=True)
    linkedin = models.URLField(max_length=255, blank=True)
    instagram = models.URLField(max_length=255, blank=True)
    github = models.URLField(max_length=255, blank=True)
    # SECTORS
    luxe = models.BooleanField(default=False)
    vfx = models.BooleanField(default=False)
    games = models.BooleanField(default=False)
    motion = models.BooleanField(default=False)
    design = models.BooleanField(default=False)
    architecture = models.BooleanField(default=False)
    animation = models.BooleanField(default=False)
    # MOBILITY
    remote = models.BooleanField(default=False)
    mobility = models.BooleanField(default=False)
    # ADMINISTRATIVE
    spectacle_number = models.CharField(max_length=10, blank=True)
    siret_number = models.CharField(max_length=14, blank=True)
    price = models.CharField(max_length=5, blank=True)
    # ARTISTIC SKILLS
    generalist = models.CharField(max_length=30, choices=SKILL_LEVELS)
    conceptart = models.CharField(max_length=30, choices=SKILL_LEVELS)
    match_moving = models.CharField(max_length=30, choices=SKILL_LEVELS)
    modeling = models.CharField(max_length=30, choices=SKILL_LEVELS)
    rigging = models.CharField(max_length=30, choices=SKILL_LEVELS)
    animating = models.CharField(max_length=30, choices=SKILL_LEVELS)
    texturing = models.CharField(max_length=30, choices=SKILL_LEVELS)
    surfacing = models.CharField(max_length=30, choices=SKILL_LEVELS)
    rendering = models.CharField(max_length=30, choices=SKILL_LEVELS)
    compositing = models.CharField(max_length=30, choices=SKILL_LEVELS)
    rotoscopy = models.CharField(max_length=30, choices=SKILL_LEVELS)
    video_editing = models.CharField(max_length=30, choices=SKILL_LEVELS)
    motionDesign = models.CharField(max_length=30, choices=SKILL_LEVELS)
    technical_director = models.CharField(max_length=30, choices=SKILL_LEVELS)
    developer = models.CharField(max_length=30, choices=SKILL_LEVELS)
    production_manager = models.CharField(max_length=30, choices=SKILL_LEVELS)
    productor = models.CharField(max_length=30, choices=SKILL_LEVELS)
    coordinator = models.CharField(max_length=30, choices=SKILL_LEVELS)
    # SOFTWARE
    photoshop = models.CharField(max_length=30, choices=SKILL_LEVELS)
    afterEffects = models.CharField(max_length=30, choices=SKILL_LEVELS)
    premiere = models.CharField(max_length=30, choices=SKILL_LEVELS)
    substancePainter = models.CharField(max_length=30, choices=SKILL_LEVELS)
    substanceDesigner = models.CharField(max_length=30, choices=SKILL_LEVELS)
    lightroom = models.CharField(max_length=30, choices=SKILL_LEVELS)
    Coat = models.CharField(max_length=30, choices=SKILL_LEVELS)
    max = models.CharField(max_length=30, choices=SKILL_LEVELS)
    affinityDesigner = models.CharField(max_length=30, choices=SKILL_LEVELS)
    affinityPhoto = models.CharField(max_length=30, choices=SKILL_LEVELS)
    akeytsu = models.CharField(max_length=30, choices=SKILL_LEVELS)
    Arnold = models.CharField(max_length=30, choices=SKILL_LEVELS)
    blender = models.CharField(max_length=30, choices=SKILL_LEVELS)
    cinema4d = models.CharField(max_length=30, choices=SKILL_LEVELS)
    clarisseIfx = models.CharField(max_length=30, choices=SKILL_LEVELS)
    clipStudioPaint = models.CharField(max_length=30, choices=SKILL_LEVELS)
    corelpainter = models.CharField(max_length=30, choices=SKILL_LEVELS)
    dazStudio = models.CharField(max_length=30, choices=SKILL_LEVELS)
    gaea = models.CharField(max_length=30, choices=SKILL_LEVELS)
    gimp = models.CharField(max_length=30, choices=SKILL_LEVELS)
    gravitySketch = models.CharField(max_length=30, choices=SKILL_LEVELS)
    houdini = models.CharField(max_length=30, choices=SKILL_LEVELS)
    illustrator = models.CharField(max_length=30, choices=SKILL_LEVELS)
    infinitePainter = models.CharField(max_length=30, choices=SKILL_LEVELS)
    keyshot = models.CharField(max_length=30, choices=SKILL_LEVELS)
    krita = models.CharField(max_length=30, choices=SKILL_LEVELS)
    mangaStudio = models.CharField(max_length=30, choices=SKILL_LEVELS)
    mari = models.CharField(max_length=30, choices=SKILL_LEVELS)
    marmoset = models.CharField(max_length=30, choices=SKILL_LEVELS)
    marvelousDesigner = models.CharField(max_length=30, choices=SKILL_LEVELS)
    maya = models.CharField(max_length=30, choices=SKILL_LEVELS)
    mentalRay = models.CharField(max_length=30, choices=SKILL_LEVELS)
    moi3d = models.CharField(max_length=30, choices=SKILL_LEVELS)
    modo = models.CharField(max_length=30, choices=SKILL_LEVELS)
    mudbox = models.CharField(max_length=30, choices=SKILL_LEVELS)
    nuke = models.CharField(max_length=30, choices=SKILL_LEVELS)
    paintToolSai = models.CharField(max_length=30, choices=SKILL_LEVELS)
    procreate = models.CharField(max_length=30, choices=SKILL_LEVELS)
    quixelSuite = models.CharField(max_length=30, choices=SKILL_LEVELS)
    revit = models.CharField(max_length=30, choices=SKILL_LEVELS)
    rhino = models.CharField(max_length=30, choices=SKILL_LEVELS)
    sketchbookPro = models.CharField(max_length=30, choices=SKILL_LEVELS)
    sketchup = models.CharField(max_length=30, choices=SKILL_LEVELS)
    speedtree = models.CharField(max_length=30, choices=SKILL_LEVELS)
    terragen = models.CharField(max_length=30, choices=SKILL_LEVELS)
    unity = models.CharField(max_length=30, choices=SKILL_LEVELS)
    unrealEngine = models.CharField(max_length=30, choices=SKILL_LEVELS)
    vray = models.CharField(max_length=30, choices=SKILL_LEVELS)
    zbrush = models.CharField(max_length=30, choices=SKILL_LEVELS)
    xnormal = models.CharField(max_length=30, choices=SKILL_LEVELS)
    davinci = models.CharField(max_length=30, choices=SKILL_LEVELS)
    resolve = models.CharField(max_length=30, choices=SKILL_LEVELS)
    octaneRender = models.CharField(max_length=30, choices=SKILL_LEVELS)
    redshift = models.CharField(max_length=30, choices=SKILL_LEVELS)
    flame = models.CharField(max_length=30, choices=SKILL_LEVELS)
    fusion = models.CharField(max_length=30, choices=SKILL_LEVELS)
    natron = models.CharField(max_length=30, choices=SKILL_LEVELS)
    meshlab = models.CharField(max_length=30, choices=SKILL_LEVELS)
    meshroom = models.CharField(max_length=30, choices=SKILL_LEVELS)
    pftrack = models.CharField(max_length=30, choices=SKILL_LEVELS)
    equalizer = models.CharField(max_length=30, choices=SKILL_LEVELS)

    def __str__(self):
        name = self.first_name + "_" + self.last_name
        return name
