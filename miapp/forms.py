from django import forms

class consultar(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Correo', max_length = 200)
    CHOICES=[('M','Masculino'),
         ('F','Femenino')]

    sexo = forms.ChoiceField(label='Sexo',choices=CHOICES, widget=forms.RadioSelect)
    consulta = forms.CharField(widget=forms.Textarea, label='consulta')
