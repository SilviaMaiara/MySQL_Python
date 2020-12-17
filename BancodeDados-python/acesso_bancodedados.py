import sys, os, time
import MySQLdb

#Exemplo de acesso ao banco de dados MySQL por meio da linguagem de programação Python

class Bd():
    def __init__(self):
        self.con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='1234',db='mydb5')
        c = self.con.cursor()

class Usuarios(object): 
    def __init__(self, idUsuario = ""):

        self.info = {}
        self.idUsuario = str(idUsuario)

    def visualizarCadastroUsuario(self):
        ban = Bd()
        try:
            c = ban.con.cursor()

            self.retorno = c.execute("select * from Usuario where id_usuario = '" + self.idUsuario +"' ")
            if self.retorno == 0:
                self.textoPesquisa = "Erro na pesquisa!"
            else:
                self.textoPesquisa = "Pesquisa concluida!"
            c.close()
            return self.textoPesquisa

        except:
            self.textoPesquisa = "Erro"
            return self.textoPesquisa
