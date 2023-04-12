from cgnetwork.models import (
    Coordinate,
    Contract,
    Mobility,
    Administrative,
    SocialMedia,
    Sector,
    Competence,
    Software,
)
from users.models.artist import Artist


def get_profile_data(user_id: int) -> dict:
    models = [
        (Artist, 'identity'),
        (Coordinate, 'coordinate'),
        (Contract, 'contract'),
        (Mobility, 'mobility'),
        (Administrative, 'administrative'),
        (SocialMedia, 'socialMedia'),
        (Sector, 'sector'),
        (Competence, 'competence'),
        (Software, 'software'),
    ]
    context = {}
    for model, context_key in models:
        context[context_key] = model.objects.get(user_id=user_id)
    return context


def convert_objects_to_dict(context: dict) -> dict:
    for key, obj in context.items():
        if hasattr(obj, '__dict__'):
            context[key] = {
                field.name: getattr(obj, field.name)
                for field in obj._meta.fields
                if field.name not in ('id', 'user')
            }
    return context


def get_artist_data(user_id):
    artist = Artist.objects.get(user_id=user_id)
    coordinate = Coordinate.objects.get(user_id=user_id)
    mobility = Mobility.objects.get(user_id=user_id)
    administrative = Administrative.objects.get(user_id=user_id)
    socialMedia = SocialMedia.objects.get(user_id=user_id)
    sector = Sector.objects.get(user_id=user_id)
    competence = Competence.objects.get(user_id=user_id)
    software = Software.objects.get(user_id=user_id)

    context = {
        'identity': artist,
        'coordinate': coordinate,
        'mobility': mobility,
        'administrative': administrative,
        'socialMedia': socialMedia,
        'sector': sector,
        'competence': competence,
        'software': software,
    }
    return context


def get_job_data(job):
    context = {}
    context['identity'] = {'logo': job.logo,
                           'title': job.title,
                           'company_name': job.company_name,
                           'description': job.description,
                           'company_size': job.company_size,
                           'sector': job.sector,
                           'contract_type': job.contract_type,
                           'salary_min': job.salary_min,
                           'salary_max': job.salary_max
                        }

    context['artistic_skills'] = {'generalist': job.generalist,
                                  'conceptart': job.conceptart,
                                  'match_moving': job.match_moving,
                                  'modeling': job.modeling,
                                  'rigging': job.rigging,
                                  'animating': job.animating,
                                  'texturing': job.texturing,
                                  'surfacing': job.surfacing,
                                  'rendering': job.rendering,
                                  'compositing': job.compositing,
                                  'video_editing': job.video_editing,
                                  'motionDesign': job.motionDesign,
                                  'technical_director': job.technical_director,
                                  'developer': job.developer,
                                  'production_manager': job.production_manager,
                                  'productor': job.productor,
                                  'coordinator': job.coordinator
                                  }

    context['softwares'] = {'photoshop': job.photoshop,
                            'afterEffects': job.afterEffects,
                            'premiere': job.premiere,
                            'substancePainter': job.substancePainter,
                            'substanceDesigner': job.substanceDesigner,
                            'lightroom': job.lightroom,
                            'Coat': job.Coat,
                            'max': job.max,
                            'affinityDesigner': job.affinityDesigner,
                            'affinityPhoto': job.affinityPhoto,
                            'akeytsu': job.akeytsu,
                            'Arnold': job.Arnold,
                            'blender': job.blender,
                            'cinema4d': job.cinema4d,
                            'clarisseIfx': job.clarisseIfx,
                            'clipStudioPaint': job.clipStudioPaint,
                            'corelpainter': job.corelpainter,
                            'dazStudio': job.dazStudio,
                            'gaea': job.gaea,
                            'gimp': job.gimp,
                            'gravitySketch': job.gravitySketch,
                            'houdini': job.houdini,
                            'illustrator': job.illustrator,
                            'infinitePainter': job.infinitePainter,
                            'keyshot': job.keyshot,
                            'krita': job.krita,
                            'mangaStudio': job.mangaStudio,
                            'mari': job.mari,
                            'marmoset': job.marmoset,
                            'marvelousDesigner': job.marvelousDesigner,
                            'maya': job.maya,
                            'mentalRay': job.mentalRay,
                            'moi3d': job.moi3d,
                            'modo': job.modo,
                            'mudbox': job.mudbox,
                            'nuke': job.nuke,
                            'paintToolSai': job.paintToolSai,
                            'procreate': job.procreate,
                            'quixelSuite': job.quixelSuite,
                            'revit': job.revit,
                            'rhino': job.rhino,
                            'sketchbookPro': job.sketchbookPro,
                            'sketchup': job.sketchup,
                            'speedtree': job.speedtree,
                            'terragen': job.terragen,
                            'unity': job.unity,
                            'unrealEngine': job.unrealEngine,
                            'vray': job.vray,
                            'zbrush': job.zbrush,
                            'xnormal': job.xnormal,
                            'davinci': job.davinci,
                            'resolve': job.resolve,
                            'octaneRender': job.octaneRender,
                            'redshift': job.redshift,
                            'flame': job.flame,
                            'fusion': job.fusion,
                            'natron': job.natron,
                            'meshlab': job.meshlab,
                            'meshroom': job.meshroom,
                            'pftrack': job.pftrack,
                            'equalizer': job.equalizer
                            }
    return context


def get_company_data(company):
    context = {}
    context['identity'] = {'logo': company.logo,
                           'company_name': company.company_name,
                           'description': company.description,
                           'company_size': company.company_size,
                        }
    context['coordonates'] = {'email': company.user.email,
                              'phone': company.user.phone_number,
                              'country': company.user.country,
                              'state': company.user.state,
                              'city': company.user.city,
                              'zip_code': company.user.zip_code,
                              'street_name': company.user.street_name,
                              'street_number': company.user.street_number,
                              }
    context['urls'] = {'website': company.website}
    context['sectors'] = {'luxe': company.luxe,
                          'vfx': company.vfx,
                          'games': company.games,
                          'motion': company.motion,
                          'design': company.design,
                          'architecture': company.architecture,
                          'animation': company.animation,
                        }
    return context
