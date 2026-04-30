from django import forms
from tables.models import Tables


class TablesForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea, label="Natija")
    price = forms.DecimalField(max_digits=10, decimal_places=2)


class TableModelForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = ['title', 'description', 'price', 'authors']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your description',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if title and len(title.strip()) < 7:
            raise forms.ValidationError("7 ta harfdan ko‘proq kiriting")

        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')

        if title and description and title == description:
            self.add_error('description', "title va description bir xil bo‘lmasin")

        return cleaned_data