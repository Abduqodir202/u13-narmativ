from django import forms

from tables.models import Tables



class TablesForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea,
                                  label="Natija")
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
        title = self.cleaned_data['title']
        if len(title) < 7:
            raise forms.ValidationError("7 ta harfdan koproq kiriting")
        return title

    def clean(self):
        title = self.cleaned_data['title']
        description = self.cleaned_data['description']

        if title == description:
            raise forms.ValidationError("title va descriptionga bir xil malumot mumkin emas")
        return self.cleaned_data