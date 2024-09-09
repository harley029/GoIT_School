from django import forms
from .models import Tag, Author, Quote


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]

    def clean_fullname(self):
        fullname = self.cleaned_data.get("fullname")
        if Author.objects.filter(fullname=fullname).exists():
            raise forms.ValidationError("This author is already exists.")
        return fullname


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["quote", "author", "tags"]

    def clean_quote(self):
        quote = self.cleaned_data.get("quote")
        if Quote.objects.filter(quote=quote).exists():
            raise forms.ValidationError("This quote is already exists.")
        return quote
