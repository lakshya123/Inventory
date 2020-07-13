from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
    def clean_ISBN(self):
        ISBN = self.cleaned_data.get('ISBN')
        if(ISBN == ""):
            raise forms.ValidationError('FIELD CANNOT BE EMPTY')

        for instance in Book.objects.all():
            if(instance.ISBN == ISBN):
                raise forms.ValidationError(ISBN + ' Already Exists')
        return ISBN

    def clean_Title(self):
        Title = self.cleaned_data.get('Title')
        if(Title == ""):
            raise forms.ValidationError('FIELD CANNOT BE EMPTY')

        for instance in Book.objects.all():
            if(instance.Title == Title):
                raise forms.ValidationError(Title + ' Already Exists')
        return Title
    
    def clean_Author(self):
        Author = self.cleaned_data.get('Author')
        if(Author == ""):
            raise forms.ValidationError('FIELD CANNOT BE EMPTY')
        return Author
    
    def clean_Language(self):
        Language = self.cleaned_data.get('Language')
        if(Language == ""):
            raise forms.ValidationError('FIELD CANNOT BE EMPTY')
    
        return Language
    
    def clean_Subject(self):
        Subject = self.cleaned_data.get('Subject')
        if(Subject == ""):
            raise forms.ValidationError('FIELD CANNOT BE EMPTY')

        return Subject
    
    def clean_Stock(self):
        Stock = self.cleaned_data.get('Stock')
        if(Stock == ""):
            raise forms.ValidationError('FIELD CANNOT BE EMPTY')
            
        if(Stock <= 0):
            raise forms.ValidationError('ADD A POSTIVE VALUE')

        return Stock


class BookEdit(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        

class BookSearch(forms.ModelForm):
    
    class Meta:
        model  = Book
        fields = ['Title','Author','Subject','Language']


