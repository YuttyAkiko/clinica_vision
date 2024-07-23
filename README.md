# Clínica Vision 👁️‍🗨️
## 📌 Projeto em desenvolvimento 🚧

### Olá! 👋

Somos a DEV TEAM! 👩‍💻
<br> [Caroline Santos](https://github.com/Caroline-Stos)
<br> [Yutty Takeyama](https://github.com/YuttyAkiko) 

A Clínica Vision é uma empresa fictícia de pequeno porte que atua no ramo da
oftalmologia, foi criada pelo médico Dr. Johnny em 2023.
A empresa, por ser nova, iniciou a administração dos registros de forma simples, utilizando
softwares de planilhas eletrônicas e, com o sucesso da clínica, sua gestão passou a se tornar
complicada devido à alta demanda dos pacientes.

A Clínica Vision nos contratou para desenvolver um sistema web integrado onde seja possível realizar a gestão da clínica de forma automatizada e ter acesso fácil aos dados sobre as informações de seus pacientes.

Para acessar 👉 [Clique aqui](https://clinicavision.pythonanywhere.com/)

<!-- ## Protótipo de alta fidelidade
<img src="static/img/home_vision.png" width="400px"> -->

## ⚠️ Configure o ambiente para executar a aplicação
Faça o clone do projeto usando o comando:
```
$ git clone https://github.com/YuttyAkiko/vision.git
```


Entre na pasta criada e inicie um ambiente virtual:
```
$ cd clinica_vision
$ python -m venv .venv
```
Depois você deve ativá-lo com o seguinte comando:
```
$ .venv/Scripts/activate
```
ou

```
$ source ./venv/bin/activate
```
Após ativado, instale as bibliotecas necessárias para executar o projeto:
```
 (venv)$ pip install -r requirements.txt
```
Para poder ter o primeiro acesso você pode configurar a aplicação. Para isso, vamos executar o comando 
'migrate' para gerar o banco de dados padrão do Django(SQLite). E depois criar o superusuario:
```
(venv)$ ./manage.py migrate
(venv)$ ./manage.py makemigrations
(venv)$ ./manage.py createsuperuser
Apelido/Usuário: 
E-mail: 
Password: 
Password (again):
```

Use o comando a seguir para iniciar o servidor localhost:
```
(venv)$ ./manage.py runserver
```


Para visualizar se tudo esta executando como esperado vamos acessar o seguinte endereço:
[http://localhost:8000/](http://localhost:8000/)

Ou você pode ter acesso ao admin do Django:
[http://localhost:8000/admin](http://localhost:8000/admin)
