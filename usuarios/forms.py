from django import forms


class LoginForm(forms.Form):
    nome_Login = forms.CharField(label='Usuario', required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'inclua o usuario'}))
    senha = forms.CharField(label='Senha', required=True, max_length=70, widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ) )

# valida o campo nome_login 
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_Login')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome