from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from book.models import Book


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.id:
            del self.fields['publish_date']

    class Meta:
        model = Book
        fields = ('title', 'isbn', 'authors', 'publish_date', 'price')

        labels = {
            'isbn': 'ISBN'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'publish_date': DatePickerInput(options={
                "format": "YYYY-MM-DD",
            }),
            'price': forms.TextInput(attrs={'class': 'form-control'})
        }
