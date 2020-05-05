from django import forms
from .models import Homework

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ["student","title","lesson","book","topic","initial_date","final_date","content"]


class HomeworkForm2(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ["total_solved","true_solved","false_solved"]