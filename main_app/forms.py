from django import forms


class BookForm(forms.Form):
    isbn = forms.CharField(max_length=10)
    book_name = forms.CharField(max_length=100)
    price = forms.IntegerField()
    author = forms.CharField(max_length=100)