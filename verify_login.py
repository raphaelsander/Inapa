from mechanize import Browser
from bs4 import BeautifulSoup

def verify(curso, matr, senha):

    URL = "https://siteseguro.inatel.br/PortalAcademico/WebLogin.aspx"

    br = Browser()
    br.set_handle_robots(False)
    br.open(URL)

    br.select_form('aspnetForm')
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    br.form['ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$tbMatricula'] = matr
    br.form['ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$Password'] = senha
    br.form['ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$dropSubCurso'] = [curso]

    response = br.submit(name='ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$LoginButton')

    dados = response.read()

    soup = BeautifulSoup(dados, 'html.parser')

    try:
        soup2 = soup.find(id='ctl00_LoginName1')
        if soup2 == None:
            return False
        else:
            return True
    except:
        return False