from django.forms import ModelForm
from CgNetwork.models import CustomUser
from .models import Company, Job


class CompanyIdentityForm(ModelForm):
    class Meta:
        model = Company
        fields = ['logo',
                  'company_name',
                  'description',
                  'company_size',
                  ]


class CompanyCoordonatesForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['country',
                  'state',
                  'city',
                  'zip_code',
                  'street_name',
                  'street_number',
                  'phone_number'
                 ]


class CompanyUrlForm(ModelForm):
    class Meta:
        model = Company
        fields =['website',
                 ]


class CompanySectorForm(ModelForm):
    class Meta:
        model = Company
        fields = ['luxe',
                  'vfx',
                  'games',
                  'motion',
                  'design',
                  'architecture',
                  'animation'
                  ]


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title',
                  'description',
                  'contract_type',
                  'sector',
                  'salary_min',
                  'salary_max'
                 ]


class JobArtisticSkillForm(ModelForm):
    class Meta:
        model = Job
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


class JobSoftwareForm(ModelForm):
    class Meta:
        model = Job
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

