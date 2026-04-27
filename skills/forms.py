from django import forms

from skills.models import Skills

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'