from django import forms
from mycv.models import ResumeItem, Skill, SkillCategory

class ResumeItemForm(forms.ModelForm):
    class Meta:
        model = ResumeItem
        fields = [
            'title',
            'company',
            'company_url',
            'date_from',
            'date_till',
            'description',
            'skills'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Company'}),
            'company_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Company url'}),
            'date_from': forms.DateInput(attrs={'class': 'form-control', 'placeholder':'From date'}),
            'date_till': forms.DateInput(attrs={'class': 'form-control', 'placeholder':'Till date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Description'}),
            'skills': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = [
            'name',
            'category'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Skill name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

