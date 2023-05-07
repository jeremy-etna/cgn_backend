from django.db import models

MOBILITIES = [
    "full remote",
    "hybrid",
    "on site",
    "Relocation Assistance",
]

CONTRACTS = [
    "full-time",
    "part-time",
    "freelance",
    "Internship",
    "apprenticeship",
]

WEBSITES = [
    "portfolio",
    "youtube",
    "linkedin",
    "instagram",
    "github",
]

SECTORS = [
    "luxury",
    "vfx",
    "video games",
    "motion",
    "design",
    "architecture",
    "animation",
]

COMPETENCES = [
    "generalist",
    "conceptart",
    "match_moving",
    "modeling",
    "rigging",
    "animating",
    "texturing",
    "surfacing",
    "rendering",
    "compositing",
    "rotoscopy",
    "video_editing",
    "motionDesign",
    "technical_director",
    "developer",
    "production_manager",
    "producer",
    "coordinator",
]

SOFTWARES = [
    "photoshop",
    "afterEffects",
    "premiere",
    "substancePainter",
    "substanceDesigner",
    "lightroom",
    "Coat",
    "max",
    "affinityDesigner",
    "affinityPhoto",
    "akeytsu",
    "Arnold",
    "blender",
    "cinema4d",
    "clarisseIfx",
    "clipStudioPaint",
    "corelpainter",
    "dazStudio",
    "gaea",
    "gimp",
    "gravitySketch",
    "houdini",
    "illustrator",
    "infinitePainter",
    "keyshot",
    "krita",
    "mangaStudio",
    "mari",
    "marmoset",
    "marvelousDesigner",
    "maya",
    "mentalRay",
    "moi3d",
    "modo",
    "mudbox",
    "nuke",
    "paintToolSai",
    "procreate",
    "quixelSuite",
    "revit",
    "rhino",
    "sketchbookPro",
    "sketchup",
    "speedtree",
    "terragen",
    "unity",
    "unrealEngine",
    "vray",
    "zbrush",
    "xnormal",
    "davinci",
    "resolve",
    "octaneRender",
    "redshift",
    "flame",
    "fusion",
    "natron",
    "meshlab",
    "meshroom",
    "pftrack",
    "equalizer",
]


class Role(models.TextChoices):
    ARTIST = "artist", "artist"
    COMPANY = "company", "company"


class SkillLevel(models.TextChoices):
    NEVER_PRACTICED = "Never practiced", "1 - Never practiced"
    NOVICE = "Novice", "2 - Novice"
    ADVANCED_BEGINNER = "Advanced Beginner", "3 - Advanced, Beginner"
    COMPETENT = "Competent", "4 - Competent"
    PROFICIENT = "Proficient", "5 - Proficient"
    EXPERT = "Expert", "6 - Expert"


class CompanySize(models.TextChoices):
    SIZE_1_10 = "1 - 10", "1 - 10"
    SIZE_11_50 = "11 - 50", "11 - 50"
    SIZE_51_99 = "51 - 99", "51 - 99"