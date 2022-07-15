from django import forms

class BMIForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    height = forms.FloatField(label = 'Height in metres')
    weight = forms.FloatField(label = 'Weight in kgs')
    
class SearchForm(forms.Form):
    search = forms.CharField (label='Search', max_length = 100)

class NewProfile(forms.Form):
    name = forms.CharField(label='Name: ', max_length=100)
    age = forms.IntegerField(label = 'Age: ')
    address = forms.CharField(label = 'Address: ')
    gender = forms.CharField(label = 'Gender: ')
    phone_number = forms.IntegerField(label = 'Phone Number: ')
    occupation = forms.CharField(label = 'Occupation: ')
    relation = forms.CharField(label = 'Relation: ')
    extra = forms.CharField(label = 'Extra: ')
