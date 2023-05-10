from django.forms import ModelForm
from job.models import Job


class JobCreationForm(ModelForm):
    class Meta:
        model = Job
        exclude = [
            'user',
            'creation_date',
            'views'
        ]
