from django import forms
from .models import Pizza, Size

# class PizzaForm(forms.Form):
#     Size_Options = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label="Size", choices = Size_Options)
    # Top_Options = [('pep', 'Pepperoni'), ('cheese', 'Cheese'), ('olive', 'Olives')]
    # toppings = forms.MultipleChoiceField(choices=Top_Options, widget=forms.CheckboxSelectMultiple)

class PizzaForm(forms.ModelForm):

    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1':'Topping 1','topping2':'Topping 2'}
        # widgets = {'size':forms.RadioSelect}

class MultiplePizzaform(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)