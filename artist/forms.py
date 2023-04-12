from django.forms import ModelForm
from cgnetwork.models import CustomUser
from .models import Artist


class ArtistIdentityForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['avatar',
                  'first_name',
                  'last_name',
                  'title',
                  'description',
                  'price',
                  ]


class ArtistCoordonatesForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['country',
                  'city',
                  'state',
                  'zip_code',
                  'phone_number'
                  ]


class ArtistContractForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['cdd',
                  'cdi',
                  'stage',
                  'freelance',
                  'intermittent',
                  'alternate'
                  ]


class ArtistUrlForm(ModelForm):
    class Meta:
        model = Artist
        fields =['website',
                 'youtube',
                 'linkedin',
                 'instagram',
                 'github'
                 ]


class ArtistSectorForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['luxe',
                  'vfx',
                  'games',
                  'motion',
                  'design',
                  'architecture',
                  'animation'
                  ]


class ArtistArtisticSkillForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['generalist',
                  'conceptart',
                  'match_moving',
                  'modeling',
                  'rigging',
                  'animating',
                  'texturing',
                  'surfacing',
                  'rendering',
                  'compositing',
                  'rotoscopy',
                  'video_editing',
                  'motionDesign',
                  'technical_director',
                  'developer',
                  'production_manager',
                  'productor',
                  'coordinator'
                  ]


class ArtistSoftwareForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['photoshop',
                  'afterEffects',
                  'substancePainter',
                  'lightroom',
                  'clipStudioPaint',
                  'corelpainter',
                  'gimp',
                  'illustrator',
                  'infinitePainter',
                  'krita',
                  'paintToolSai',
                  'davinci',
                  'flame',
                  'fusion',
                  'mangaStudio',
                  'natron',
                  'nuke',
                  'premiere',
                  'resolve',
                  'sketchbookPro',
                  'Coat',
                  'mudbox',
                  'zbrush',
                  'marmoset',
                  'unity',
                  'unrealEngine',
                  'xnormal',
                  'blender',
                  'cinema4d',
                  'houdini',
                  'maya',
                  'max',
                  'Arnold',
                  'keyshot',
                  'mentalRay',
                  'octaneRender',
                  'redshift',
                  'vray',
                  'sketchup',
                  'rhino',
                  'moi3d',
                  'gaea',
                  'speedtree',
                  'terragen',
                  'quixelSuite',
                  'substanceDesigner',
                  'mari',
                  'pftrack',
                  'equalizer',
                  'dazStudio',
                  'clarisseIfx',
                  'modo',
                  'meshlab',
                  'meshroom',
                  'akeytsu',
                  'affinityDesigner',
                  'affinityPhoto',
                  'gravitySketch',
                  'marvelousDesigner',
                  'procreate',
                  'revit'
                  ]
