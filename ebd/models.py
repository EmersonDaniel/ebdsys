from django.db import models

class Membros(models.Model):

	nome = models.CharField(max_length=100)

	classe = models.CharField(max_length=20)

	'''posteriormente definir aqui metodos para
	retorno de alguns dados, possivelmente isso
	substitua alguns ou todos querysets'''