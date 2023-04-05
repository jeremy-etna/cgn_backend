from django.test import SimpleTestCase
from artist.forms import (
    ArtistIdentityForm,
    ArtistCoordonatesForm,
    ArtistContractForm,
    ArtistUrlForm,
    ArtistArtisticSkillForm,
    ArtistSectorForm,
    ArtistSoftwareForm
    )


class TestForms(SimpleTestCase):

    def test_ArtistIdentityForm_valid_data(self):
        form = ArtistIdentityForm(data={
            'avatar': 'random.jpg',
            'first_name': 'jeremy',
            'last_name': 'oblet',
            'title': 'developer',
            'description': 'Lorem ipsum',
            'price': '220'
        })
        self.assertTrue(form.is_valid())

    def test_ArtistIdentityForm_no_data(self):
        form = ArtistIdentityForm(data={})
        self.assertTrue(form.is_valid())

    def test_ArtistCoordonatesForm_valid_data(self):
        form = ArtistCoordonatesForm(data={
            'country': 'France',
            'city': 'Paris',
            'state': 'Ile de France',
            'zip_code': '75000',
            'phone_number': '0606060606'
        })
        self.assertTrue(form.is_valid())

    def test_ArtistCoordonatesForm_no_data(self):
        form = ArtistCoordonatesForm(data={})
        self.assertTrue(form.is_valid())

    def test_ArtistContractForm_valid_data(self):
        form = ArtistContractForm(data={
            'cdd': True,
            'cdi': True,
            'stage': True,
            'freelance': True,
            'intermittent': True,
            'alternate': True
        })
        self.assertTrue(form.is_valid())

    def test_ArtistContractForm_no_data(self):
        form = ArtistContractForm(data={})
        self.assertTrue(form.is_valid())

    def test_ArtistUrlForm_valid_data(self):
        form = ArtistUrlForm(data={
            'website': 'https://www.google.com',
            'youtube': 'https://www.youtube.com',
            'linkedin': 'https://www.linkedin.com',
            'instagram': 'https://www.instagram.com',
            'github': 'https://www.github.com'
        })
        self.assertTrue(form.is_valid())

    def test_ArtistUrlForm_no_data(self):
        form = ArtistUrlForm(data={})
        self.assertTrue(form.is_valid())

    def test_ArtistArtisticSkillForm_valid_data(self):
        form = ArtistArtisticSkillForm(data={
            'generalist': 'Never used',
            'conceptart': 'Never used',
            'match_moving': 'Never used',
            'modeling': 'Never used',
            'rigging': 'Never used',
            'animating': 'Never used',
            'texturing': 'Never used',
            'surfacing': 'Never used',
            'rendering': 'Never used',
            'compositing': 'Never used',
            'rotoscopy': 'Never used',
            'video_editing': 'Never used',
            'motionDesign': 'Never used',
            'technical_director': 'Never used',
            'developer': 'Never used',
            'production_manager': 'Never used',
            'productor': 'Never used',
            'coordinator': 'Never used'
        })
        self.assertTrue(form.is_valid())

    def test_ArtistArtisticSkillForm_no_data(self):
        form = ArtistArtisticSkillForm(data={})
        self.assertFalse(form.is_valid())

    def test_ArtistSectorForm_valid_data(self):
        form = ArtistSectorForm(data={
            'luxe': True,
            'vfx': True,
            'games': True,
            'motion': True,
            'design': True,
            'architecture': True
        })
        self.assertTrue(form.is_valid())

    def test_ArtistSectorForm_no_data(self):
        form = ArtistSectorForm(data={})
        self.assertTrue(form.is_valid())

    def test_ArtistSoftwareForm_valid_data(self):
        form = ArtistSoftwareForm(data={
            'photoshop': 'Novice',
            'afterEffects': 'Novice',
            'substancePainter': 'Novice',
            'lightroom': 'Novice',
            'clipStudioPaint': 'Novice',
            'corelpainter': 'Novice',
            'gimp': 'Novice',
            'illustrator': 'Novice',
            'infinitePainter': 'Novice',
            'krita': 'Novice',
            'paintToolSai': 'Novice',
            'davinci': 'Novice',
            'flame': 'Novice',
            'fusion': 'Novice',
            'mangaStudio': 'Novice',
            'natron': 'Novice',
            'nuke': 'Novice',
            'premiere': 'Novice',
            'resolve': 'Novice',
            'sketchbookPro': 'Novice',
            'Coat': 'Novice',
            'mudbox': 'Novice',
            'zbrush': 'Novice',
            'marmoset': 'Novice',
            'unity': 'Novice',
            'unrealEngine': 'Novice',
            'xnormal': 'Novice',
            'blender': 'Novice',
            'cinema4d': 'Novice',
            'houdini': 'Novice',
            'maya': 'Novice',
            'max': 'Novice',
            'Arnold': 'Novice',
            'keyshot': 'Novice',
            'mentalRay': 'Novice',
            'octaneRender': 'Novice',
            'redshift': 'Novice',
            'vray': 'Novice',
            'sketchup': 'Novice',
            'rhino': 'Novice',
            'moi3d': 'Novice',
            'gaea': 'Novice',
            'speedtree': 'Novice',
            'terragen': 'Novice',
            'quixelSuite': 'Novice',
            'substanceDesigner': 'Novice',
            'mari': 'Novice',
            'pftrack': 'Novice',
            'equalizer': 'Novice',
            'dazStudio': 'Novice',
            'clarisseIfx': 'Novice',
            'modo': 'Novice',
            'meshlab': 'Novice',
            'meshroom': 'Novice',
            'akeytsu': 'Novice',
            'affinityDesigner': 'Novice',
            'affinityPhoto': 'Novice',
            'gravitySketch': 'Novice',
            'marvelousDesigner': 'Novice',
            'procreate': 'Novice',
            'revit': 'Novice'
        })
        self.assertTrue(form.is_valid())

    def test_ArtistSoftwareForm_no_data(self):
        form = ArtistSoftwareForm(data={})
        self.assertFalse(form.is_valid())