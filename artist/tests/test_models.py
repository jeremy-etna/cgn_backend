from django.test import TestCase
from artist.models import Artist
from CgNetwork.models import CustomUser


class TestModels(TestCase):

    def setUp(self):
        self.random_user = CustomUser.objects.create()
        self.wam = Artist.objects.create(
            user=self.random_user,
            avatar='avatars/artist_default.png',
            title='Mr',
            first_name='Wam',
            last_name='Wam',
            description='Wam',
            cdd=True,
            cdi=True,
            stage=True,
            freelance=True,
            intermittent=True,
            alternate=True,
            website='https://www.wam.com',
            youtube='https://www.youtube.com',
            linkedin='https://www.linkedin.com',
            instagram='https://www.instagram.com',
            github='https://www.github.com',
            luxe=True,
            vfx=True,
            games=True,
            motion=True,
            design=True,
            architecture=True,
            animation=True,
            remote=True,
            mobility=True,
            spectacle_number='123456789',
            siret_number='12345678912345',
            price='12345',
            generalist='Never used',
            conceptart='Never used',
            match_moving='Never used',
            modeling='Never used',
            rigging='Novice',
            animating='Novice',
            texturing='Novice',
            surfacing='Novice',
            rendering='Novice',
            compositing='Novice',
            rotoscopy='Novice',
            video_editing='Novice',
            motionDesign='Novice',
            technical_director='Novice',
            developer='Novice',
            production_manager='Novice',
            productor='Novice',
            coordinator='Novice',
            photoshop='Novice',
            afterEffects='Novice',
            premiere='Novice',
            substancePainter='Novice',
            substanceDesigner='Novice',
            lightroom='Novice',
            Coat='Novice',
            max='Novice',
            affinityDesigner='Novice',
            affinityPhoto='Novice',
            akeytsu='Novice',
            Arnold='Novice',
            blender='Novice',
            cinema4d='Novice',
            clarisseIfx='Novice',
            clipStudioPaint='Novice',
            corelpainter='Novice',
            dazStudio='Novice',
            gaea='Novice',
            gimp='Novice',
            gravitySketch='Novice',
            houdini='Novice',
            illustrator='Novice',
            infinitePainter='Novice',
            keyshot='Novice',
            krita='Novice',
            mangaStudio='Novice',
            mari='Novice',
            marmoset='Novice',
            marvelousDesigner='Novice',
            maya='Novice',
            mentalRay='Novice',
            moi3d='Novice',
            modo='Novice',
            mudbox='Novice',
            nuke='Novice',
            paintToolSai='Novice',
            procreate='Novice',
            quixelSuite='Novice',
            revit='Novice',
            rhino='Novice',
            sketchbookPro='Novice',
            sketchup='Novice',
            speedtree='Novice',
            terragen='Novice',
            unity='Novice',
            unrealEngine='Novice',
            vray='Novice',
            zbrush='Novice',
            xnormal='Novice',
            davinci='Novice',
            resolve='Novice',
            octaneRender='Novice',
            redshift='Novice',
            flame='Novice',
            fusion='Novice',
            natron='Novice',
            meshlab='Novice',
            meshroom='Novice',
            pftrack='Novice',
            equalizer='Novice',
        )

    def test_artist_creation(self):
        self.assertTrue(isinstance(self.wam, Artist))
        self.assertEquals(self.wam.user, self.random_user)
        self.assertEquals(self.wam.avatar, 'avatars/artist_default.png')
        self.assertEquals(self.wam.title, 'Mr')
        self.assertEquals(self.wam.first_name, 'Wam')
        self.assertEquals(self.wam.last_name, 'Wam')
        self.assertEquals(self.wam.description, 'Wam')
        self.assertEquals(self.wam.cdd, True)
        self.assertEquals(self.wam.cdi, True)
        self.assertEquals(self.wam.stage, True)
        self.assertEquals(self.wam.freelance, True)
        self.assertEquals(self.wam.intermittent, True)
        self.assertEquals(self.wam.alternate, True)
        self.assertEquals(self.wam.website, 'https://www.wam.com')
        self.assertEquals(self.wam.youtube, 'https://www.youtube.com')
        self.assertEquals(self.wam.linkedin, 'https://www.linkedin.com')
        self.assertEquals(self.wam.instagram, 'https://www.instagram.com')
        self.assertEquals(self.wam.github, 'https://www.github.com')
        self.assertEquals(self.wam.luxe, True)
        self.assertEquals(self.wam.vfx, True)
        self.assertEquals(self.wam.games, True)
        self.assertEquals(self.wam.motion, True)
        self.assertEquals(self.wam.design, True)
        self.assertEquals(self.wam.architecture, True)
        self.assertEquals(self.wam.animation, True)
        self.assertEquals(self.wam.remote, True)
        self.assertEquals(self.wam.mobility, True)
        self.assertEquals(self.wam.spectacle_number, '123456789')
        self.assertEquals(self.wam.siret_number, '12345678912345')
        self.assertEquals(self.wam.price, '12345')
        self.assertEquals(self.wam.generalist, 'Never used')
        self.assertEquals(self.wam.conceptart, 'Never used')
        self.assertEquals(self.wam.match_moving, 'Never used')
        self.assertEquals(self.wam.modeling, 'Never used')
        self.assertEquals(self.wam.rigging, 'Novice')
        self.assertEquals(self.wam.animating, 'Novice')
        self.assertEquals(self.wam.texturing, 'Novice')
        self.assertEquals(self.wam.surfacing, 'Novice')
        self.assertEquals(self.wam.rendering, 'Novice')
        self.assertEquals(self.wam.compositing, 'Novice')
        self.assertEquals(self.wam.rotoscopy, 'Novice')
        self.assertEquals(self.wam.video_editing, 'Novice')
        self.assertEquals(self.wam.motionDesign, 'Novice')
        self.assertEquals(self.wam.technical_director, 'Novice')
        self.assertEquals(self.wam.developer, 'Novice')
        self.assertEquals(self.wam.production_manager, 'Novice')
        self.assertEquals(self.wam.productor, 'Novice')
        self.assertEquals(self.wam.coordinator, 'Novice')
        self.assertEquals(self.wam.photoshop, 'Novice')
        self.assertEquals(self.wam.afterEffects, 'Novice')
        self.assertEquals(self.wam.premiere, 'Novice')
        self.assertEquals(self.wam.substancePainter, 'Novice')
        self.assertEquals(self.wam.substanceDesigner, 'Novice')
        self.assertEquals(self.wam.affinityDesigner, 'Novice')
        self.assertEquals(self.wam.affinityPhoto, 'Novice')
        self.assertEquals(self.wam.blender, 'Novice')
        self.assertEquals(self.wam.clipStudioPaint, 'Novice')
        self.assertEquals(self.wam.dazStudio, 'Novice')
        self.assertEquals(self.wam.houdini, 'Novice')
        self.assertEquals(self.wam.maya, 'Novice')
        self.assertEquals(self.wam.mudbox, 'Novice')
        self.assertEquals(self.wam.nuke, 'Novice')
        self.assertEquals(self.wam.revit, 'Novice')
        self.assertEquals(self.wam.sketchup, 'Novice')
        self.assertEquals(self.wam.zbrush, 'Novice')
        self.assertEquals(self.wam.redshift, 'Novice')
        self.assertEquals(self.wam.vray, 'Novice')
        self.assertEquals(self.wam.unrealEngine, 'Novice')
        self.assertEquals(self.wam.unity, 'Novice')
        self.assertEquals(self.wam.equalizer, 'Novice')
