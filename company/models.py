from django.db import models
from django.utils import timezone
from django.conf import settings

SECTORS = (
    ('luxe', 'Luxe'),
    ('vfx', 'VFX'),
    ('games', 'Games'),
    ('motion', 'Motion'),
    ('design', 'Design'),
    ('architecture', 'Architecture'),
    ('animation', 'Animation'),
)

SKILL_LEVELS = (
    ('Never used', '1 - Never used'),
    ('Novice', '2 - Novice'),
    ('Advanced Beginner', '3 - Advanced Beginner'),
    ('Competent', '4 - Competent'),
    ('Proficient', '5 - Proficient'),
    ('Expert', '6 - Expert')
)


COMPANY_SIZES = (
    ('1 - 10', '1 - 10'),
    ('11 - 50', '11 - 50'),
    ('51 - 99', '51 - 99')
)

CONTRACT_TYPES = (
    ('CDI', 'CDI'),
    ('CDD', 'CDD'),
    ('Freelance', 'Freelance'),
    ('Intermittent', 'Intermittent'),
    ('Stage', 'Stage'),
    ('Alternate', 'Alternate'),
)


class Company(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos', default='logos/company_default.png')
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    company_size = models.CharField(max_length=30, choices=COMPANY_SIZES)
    website = models.CharField(max_length=100)
    # SECTORS
    animation = models.BooleanField(default=False)
    architecture = models.BooleanField(default=False)
    design = models.BooleanField(default=False)
    games = models.BooleanField(default=False)
    luxe = models.BooleanField(default=False)
    motion = models.BooleanField(default=False)
    vfx = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


class Job(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_size = models.CharField(max_length=30, choices=COMPANY_SIZES)
    logo = models.ImageField(upload_to='logos', default='logos/company_default.png')
    creation_date = models.DateTimeField(default=timezone.now)

    title = models.CharField(max_length=100)
    description = models.TextField()
    sector = models.CharField(max_length=30, choices=SECTORS)
    contract_type = models.CharField(max_length=30, choices=CONTRACT_TYPES)
    salary_min = models.CharField(max_length=5)
    salary_max = models.CharField(max_length=5)

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
        return self.company_name
