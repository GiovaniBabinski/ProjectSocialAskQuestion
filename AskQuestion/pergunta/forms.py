from django import forms
from django.contrib.auth import get_user_model
from .models import Pergunta,Resposta

User = get_user_model()


#Formulários de registro e perfil pessoal
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Digite sua senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme sua senha", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd ['password2']:
            raise forms.ValidationError("As senhas não conferem!")

        return cd['password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email')



#Formularios referentes às perguntas
class PerguntaRegistrationForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields =('titulo','descricao')



class UpdatePerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields =('titulo','descricao',)


#Formularios referentes às respostas
class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields=('descricao',)


class UpdateRespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ('descricao',)



