import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
import random
from colorama import Cursor
import mysql.connector

DB= mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="dados",
                auth_plugin='mysql_native_password'
            )

class Conta():
    def __init__(self,agencia,conta,feedback,feedback2,l,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,botao,botaoS,v1,v2,v3,v4,v5,v6,v9,v11,v12,z2):
        self.feedback=feedback
        self.feedback2=feedback2
        self.l=l
        self.l2=l2
        self.l3=l3
        self.l4=l4
        self.l5=l5
        self.l6=l6
        self.l7=l7
        self.l8=l8
        self.l9=l9
        self.l10=l10
        self.l11=l11
        self.l12=l12
        self.botao=botao
        self.botaoS=botaoS
        self.v1=v1
        self.v2=v2
        self.z2=z2
        self.v3=v3
        self.v4=v4
        self.v5=v5
        self.v6=v6
        self.v9=v9
        self.v11=v11
        self.v12=v12
        self.agencia=agencia
        self.conta=conta
        pass

    def texto(self):
        self.l= QLineEdit('',janela)
        self.l.setGeometry(10,30,150,25)
        self.l2= QLineEdit('',janela)
        self.l2.setGeometry(180,30,150,25)
        self.l2.setMaxLength(11)
        self.l3= QLineEdit('',janela)
        self.l3.setGeometry(10,80,150,25)
        self.l4= QLineEdit('',janela)
        self.l4.setGeometry(180,80,150,25)
        self.l5= QLineEdit('',janela)
        self.l5.setGeometry(10,130,150,25)
        self.l6= QLineEdit('',janela)
        self.l6.setGeometry(180,130,150,25)
        self.l7= QLineEdit('',janela)
        self.l7.setGeometry(10,180,150,25)
        self.l8= QLineEdit('',janela)
        self.l8.setGeometry(180,180,150,25)
        self.l9= QLineEdit('',janela)
        self.l9.setGeometry(10,230,150,25)
        self.l10= QLineEdit('',janela)
        self.l10.setGeometry(180,230,150,25)
        self.l11= QLineEdit('',janela)
        self.l11.setGeometry(10,280,150,25)
        self.l12= QLineEdit('',janela)
        self.l12.setGeometry(180,280,150,25)

    def fDb(self): 
        self.feedback= QLabel("",janela)
        self.feedback.move(200,350)
        self.feedback.setStyleSheet('font-size:20px')
        pass
    
    def fDb2(self): 
        self.feedback2= QLabel("",janela)
        self.feedback2.move(380,30)
        self.feedback2.setStyleSheet('font-size:16px')
        pass

    def f1(self): #criar
        
        self.v1=self.l.text()
        self.v2=self.l2.text()
        self.z2=len(self.v2)
        self.v3=self.l3.text()
        self.v4=self.l4.text()
        self.v5=self.l5.text()
        self.v6=self.l6.text()
        self.v9=self.l9.text()
        self.v11=self.l11.text()
        self.v12=self.l12.text()
        if self.v1==''or self.v2==''or self.v3==''or self.v4==''or self.v5==''or self.v6==''or self.v9==''or self.v11==''or self.v12=='':
            self.feedback.setText('Preencha todos os\n campos obrigatórios')
            self.feedback.adjustSize()
        elif self.z2!=11:
            self.feedback.setText('O CPF deve ter 11 digitos')
            self.feedback.adjustSize()
        elif self.v11!=self.v12:
            self.feedback.setText('As senhas não se coincidem\n digite novamente')
            self.feedback.adjustSize()
        elif self.v11==self.v12:
            self.feedback.setText('Conta cadastrada com sucesso')
            self.feedback.adjustSize()
            self.agencia=random.randint(100,999)
            self.conta=random.randint(10000000,99999999)
            print(self.conta,self.agencia)
            cursor= DB.cursor()
            cmd= "INSERT INTO informacoes (nome,agencia,conta,senha) VALUES (%s,%s,%s,%s)"
            info= (str(self.v1),self.agencia,self.conta,str(self.v12))
            cursor.execute(cmd,info)
            DB.commit()
            self.feedback2.setText(f'Agência: {self.agencia}\nconta: {self.conta}')
            self.feedback2.adjustSize()
            pass
    def bt(self):
        self.botao= QPushButton("Criar",janela)
        self.botao.setGeometry(350,100,150,40)
        self.botao.setStyleSheet('background-color:white;color:blue')
        self.botao.clicked.connect(self.f1)
        
        pass
    def botao2(self):
        self.botaoS= QPushButton("Voltar",janela)
        self.botaoS.setGeometry(350,200,150,40)
        self.botaoS.setStyleSheet('background-color:white;color:blue')
        self.botaoS.clicked.connect(tela)
        pass

def tela(): #tela-de-login
    janela.hide()
    tela2.show()

app= QApplication(sys.argv)

janela= QWidget()
janela.resize(525,400)
janela.setWindowTitle("Conta")

tela2= QWidget()
tela2.resize(525,400)
tela2.setWindowTitle("Login")

#Tela-de-Login
texto=QLabel("Conta:", tela2)
texto.move(230,100)
texto.setStyleSheet('font-size:20px')

texto2=QLabel("Senha:", tela2)
texto2.move(100,180)
texto2.setStyleSheet('font-size:20px')

texto3=QLabel("Agência:", tela2)
texto3.move(100,100)
texto3.setStyleSheet('font-size:20px')

L_agencia= QLineEdit('',tela2)
L_agencia.setGeometry(100,130,50,25)
L_agencia.setMaxLength(3)

L_conta= QLineEdit('',tela2)
L_conta.setGeometry(230,130,80,25)
L_conta.setMaxLength(8)

L_senha= QLineEdit('',tela2)
L_senha.setGeometry(100,210,150,25)



def ler_banco():
    lido1=L_agencia.text()
    lido2=L_conta.text()
    lido3=L_senha.text()
    resultado=1
    if resultado!=1:
        pass
    else:
        pass
    cursor=DB.cursor()
    query= "SELECT agencia,conta,senha from informacoes where agencia like '"+lido1 + "' and conta like '"+lido2 + "' and senha like '" +lido3 + "' "
    cursor.execute(query)
    resultado= cursor.fetchone()

    if resultado== None:
        feedback3.setText("Dados incorretos,\nverifique e digite\nnovamente")
        feedback3.adjustSize()
    else:
        feedback3.setText("Login feito\ncom sucesso")
        feedback3.adjustSize()


    pass

b_login= QPushButton("Entrar",tela2)
b_login.setGeometry(300,200,120,40)
b_login.setStyleSheet('background-color:white;color:blue')
b_login.clicked.connect(ler_banco)

feedback3= QLabel("",tela2)
feedback3.move(225,300)
feedback3.setStyleSheet('font-size:25px')


#Tela-de-Cadastro
label=QLabel("Nome:",janela)
label.move(10,5)
label.setStyleSheet('font-size:20px')

label2= QLabel("CPF:",janela)
label2.move(180,5)
label2.setStyleSheet('font-size:20px')

label3= QLabel("Nacionalidade:",janela)
label3.move(10,55)
label3.setStyleSheet('font-size:20px')

label4= QLabel("Cidade:",janela)
label4.move(180,55)
label4.setStyleSheet('font-size:20px')

label5= QLabel("Estado:",janela)
label5.move(10,105)
label5.setStyleSheet('font-size:20px')

label6= QLabel("Endereço:",janela)
label6.move(180,105)
label6.setStyleSheet('font-size:20px')

label7= QLabel("Telefone celular:",janela)
label7.move(10,155)
label7.setStyleSheet('font-size:20px')

label8= QLabel("Renda mensal:",janela)
label8.move(180,155)
label8.setStyleSheet('font-size:20px')

label9= QLabel("Nome da Mãe:",janela)
label9.move(10,205)
label9.setStyleSheet('font-size:20px')

label10= QLabel("Nome do Pai:",janela)
label10.move(180,205)
label10.setStyleSheet('font-size:20px')

label11= QLabel("Senha da conta:",janela)
label11.move(10,255)
label11.setStyleSheet('font-size:20px')

label12= QLabel("Digite novamente:",janela)
label12.move(180,255)
label12.setStyleSheet('font-size:20px')



conta=Conta(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
conta.texto()
conta.fDb()
conta.botao2()
conta.bt()
conta.fDb2()
#conta.f1()


janela.show()
app.exec()

