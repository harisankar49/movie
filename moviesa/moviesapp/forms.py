from django import forms#This line imports the forms module from the django package, which is necessary for creating Django forms.
from .models import movie#This line imports the movie model from the same Django app. The dot (.) before models indicates that the models module is in the same directory as the current module.

class movieform(forms.ModelForm):#This line imports the movie model from the same Django app. The dot (.) before models indicates that the models module is in the same directory as the current module.
    class Meta:
        model=movie #This line specifies the model associated with the form. In your provided code, model = movie indicates that the form (movieform) is associated with the movie model.
        fields=['name','desc','year','img']#This line allows you to specify the fields from the model that should be included in the form. In your code, fields = ['name', 'desc', 'year', 'img'] indicates that the form will include fields for the movie's name, description, year, and image.



#In Django, the class Meta inside a form is used to provide additional information about the form's behavior and characteristics. It is a way to include metadata for the form. The Meta class is not required in a form, but it allows you to customize various aspects of the form's behavior.






