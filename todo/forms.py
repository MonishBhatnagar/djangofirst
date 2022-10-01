from todo.models import Contact, Todo
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields={"title","description","name","email"}
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields={"name","Sub","messg","email"}