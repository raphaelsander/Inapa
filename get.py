#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

## Dependencias
# apt install python-mechanize
# apt install python-bs4

'''
Abaixo temos os cursos e seus respectivos
códigos no dropdown do formulário de login

1 - Engenharia Elétrica
2 - Engenharia da Computação
12 - Engenharia de Telecomunicações
6 - Engenharia Biomédica
24 - Engenharia de Controle e Automação
5 - Tec. em Redes de Computadores
7 - Tec. em Automação Industrial
21 - Tec. em Gestão de Telecomunicações
31 - Curso de Aluno Especial
'''

from mechanize import Browser
from bs4 import BeautifulSoup

def get_provas(matr, senha, curso):

	URL = "https://siteseguro.inatel.br/PortalAcademico/Academico/Sra/WebListarHorariosProva.aspx"

	br = Browser()
	br.set_handle_robots(False)
	br.open(URL)

	br.select_form('aspnetForm')
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	br.form['ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$tbMatricula'] = matr
	br.form['ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$Password'] = senha
	br.form['ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$dropSubCurso'] = [curso]

	response = br.submit(name='ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$LoginButton')

	dados = response.read()

	soup = BeautifulSoup(dados, 'html.parser')

	soup2 = soup.find(id='ctl00_Corpo_UCCalendarioProvas1_GridDados')
	all_td = soup2.find_all("td")
	lista_provas = []

	for lista_provas_texto in all_td:
		lista_provas.append(lista_provas_texto.get_text())

	return lista_provas

def get_horario(matr, senha, curso):

	URL = "https://siteseguro.inatel.br/PortalAcademico/Academico/Sra/WebQuadroAulas.aspx"

	br = Browser()
	br.set_handle_robots(False)
	br.open(URL)

	br.set_handle_robots(False)

	br.select_form('aspnetForm')
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	br.form['ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$tbMatricula'] = matr
	br.form['ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$Password'] = senha
	br.form['ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$dropSubCurso'] = [curso]

	response = br.submit(name='ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$LoginButton')

	dados = response.read()

	soup = BeautifulSoup(dados, 'html.parser')

	soup2 = soup.find(id='ctl00_Corpo_UCQuadroHorarios1_GridDados')
	all_td = soup2.find_all("td")
	aux = []

	for var in all_td:
		aux.append(var.get_text())

	lista_horario = []

	for x in range(0, 15):
		lista_horario.append(aux[2 + (19 * x)])
		lista_horario.append(aux[5 + (19 * x)])
		lista_horario.append(aux[8 + (19 * x)])
		lista_horario.append(aux[11 + (19 * x)])
		lista_horario.append(aux[14 + (19 * x)])
		lista_horario.append(aux[17 + (19 * x)])

	return lista_horario