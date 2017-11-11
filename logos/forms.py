from django import forms

from loxodon import settings
from logos.models import LogoAnalyze

class LogoAnalyzeForm(forms.ModelForm):
    video = forms.FileField(label='Upload the logo video')

    class Meta:
        model = LogoAnalyze
        fields = ('video',)