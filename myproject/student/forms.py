from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
   class Meta:
    model = Student
    fields = ['name', 'age', 'email', 'course']
    
    def clean_age(self):
       age = self.cleaned_data.get('age')
       if age is not None and age < 18:
         raise forms.ValidationError("Age must be 18 or above")
       return age
