import smtplib
import email.message
import mysql.connector
import pandas as pd
from conteudo import content

connect = mysql.connector.connect(
	host='HOST_DB',
	user='USER_DB',
	password='PASSWORD_DB',
	database='DATABASE'
)

cursor = connect.cursor() 

#  ENVIAR ================================
def enviar():

	lista_emails = []

	cursor = connect.cursor() 
	command = f'SELECT * FROM list'
	cursor.execute(command)
	resultado = cursor.fetchall()

	for gmail in resultado:
		lista_emails.append(gmail[2])

	for emails in lista_emails:
		msg = email.message.Message()
		msg['Subject'] = 'Assunto'
		msg['From'] = 'EMAIL_FROM
		password = 'SENHA_DO_APP'
		msg['To'] = emails

		msg.add_header('Content-Type', 'text/html')
		msg.set_payload(content)


		dominio = smtplib.SMTP('smtp.gmail.com: 587')
		dominio.starttls()

	# Login Credentials For sending the mail
		dominio.login(msg['From'], password) 
		dominio.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

		print("Email enviado")
	
	cursor.close()
	connect.close()
    

def create():
	name = input('digite o nome: ')
	if name == '':
		while name == '':
			print('preencha o campo corretamente')
			name = input('digite o nome: ')


	email = input('digite o email: ')
	if email == '':
		while email == '':
			print('preencha o campo corretamente')
			email = input('digite o email: ')

	else:
		command = f'INSERT INTO list (name,email) VALUES ("{name}","{email}")'
		cursor.execute(command)
		connect.commit()

	read()

#  READ ================================
def read():
	print('')
	command = f'SELECT * FROM list'

	cursor.execute(command)
	results = cursor.fetchall()

	columns = ["ID", "NAME", "EMAIL"]
	print(pd.DataFrame(results, columns=columns))	
	print('')

#  DELETE ================================
def delete():
	email = input('digite o email para DELETAR: ')
	if email == '':
		while email == '':
			print('preencha o campo corretamente')
			email = input('digite o email para DELETAR: ')

	command = f'DELETE FROM list WHERE email = "{email}"'

	cursor.execute(command)
	connect.commit()
	
	read()

def options():
	print(
	'''
Digite a opção desejada:

1 - Enviar newsletter:
2 - Adicionar
3 - Deletar
4 - Vizualizar
''')

	option = int(input("> "))

	if option == 1:
		enviar()
	if option == 2:
		create()
	if option == 3:
		delete()
	if option == 4:
		read()

while True:
	options()