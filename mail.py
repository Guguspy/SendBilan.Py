from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
import email.mime.application
import time
import datetime
from time import strftime
from time import gmtime, strftime
from tkinter import *
from tkinter import messagebox

##############   DEF   #########################

def wipe():
    entry_mail.delete(first =0, last =1000)
    entry_nom.delete(first =0, last =1000)
    entry_prenom.delete(first =0, last =1000)
    entry_detail.delete(first =0, last =1000)
    var.set(None)
    
def mail():
    try :     
        rien=''
        verifmail=''
        gmail='@'
        a=0
        z=0
        noproblem=0
        verifcompteur=0
        mail=entry_mail.get()
        verifmail = mail
        verifmail=verifmail.lower()   
        if gmail in verifmail:
            a=1
            verifcompteur=verifcompteur+1
        else:
            messagebox.showerror("Erreur","Veillez entrer une adresse mail !")
            
        nom=entry_nom.get()
        if nom==rien:
            messagebox.showerror("Erreur","Le nom ne peut pas être vide !")
        else:
            nom=nom.upper()
            verifcompteur=verifcompteur+1
    
        prenom=entry_prenom.get()
        if prenom==rien:
            messagebox.showerror("Erreur","Le prenom ne peut pas être vide !")
        else:
            prenom=prenom.capitalize()
            verifcompteur=verifcompteur+1
    
        explication=entry_detail.get()
        if explication==rien:
            messagebox.showerror("Erreur","L'explication ne peut pas être vide !")
        else:
            explication=explication.capitalize()
            verifcompteur=verifcompteur+1

        genre=''
        
        if var.get()==1 :
            genre='Mlle'
            verifcompteur=verifcompteur+1
        elif var.get()==2:
            genre='Mme'
            verifcompteur=verifcompteur+1
        elif var.get()==3:
            genre='Mr'
            verifcompteur=verifcompteur+1
        elif var.get()==0:
            genre=''
            verifcompteur=verifcompteur+1
        else:
            messagebox.showerror("Erreur","Veuillez selectionner le genre !")

        if verifcompteur == 5:
            noproblem=1
            sendmail()
        else:
            verifcompteur=0

    except:
        if noproblem == 0:
            messagebox.showwarning("Erreur","Un problème est survenu ! Vérifiez votre connexion internet !")

def sendmail():
    try:
        mail=entry_mail.get()
        nom=entry_nom.get()
        nom=nom.upper()
        prenom=entry_prenom.get()
        prenom=prenom.capitalize()
        explication=entry_detail.get()
        explication=explication.capitalize()

        if var.get()==1 :
            genre=' Mlle'
        elif var.get()==2:
            genre=' Mme'
        elif var.get()==3:
            genre=' Mr'
        elif var.get()==0:
            genre=''
    
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        s = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        s.login('MAIL','PASS')

        msg = MIMEMultipart()
        msg['Subject'] = 'Votre compte rendu'
        msg['From'] = 'Votre pedicure-podologue'
        msg['To'] = mail

        date = datetime.datetime.now()
        str(date)
        dateyear = str(date.year)
        datemonth = str(date.month)
        dateday = str(date.day)

        if dateday == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            dateday=str(dateday).zfill(2)
        else:
            dateday=str(dateday)

        if datemonth == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            datemonth=str(datemonth).zfill(2)
        else:
            datemonth=str(datemonth)

        base='Veuillez trouver ci-joint votre compte rendu de séance chez Monsieur REVERDY Patrick [Pédicure-Podologue]'
        rajout='\n\n\n\nMerci de ne pas correspondre via cette adresse mail.\nVeuillez noter que ce courriel a été envoyé à partir d\'une adresse ne pouvant recevoir d\'e-mails.\n\n'
        
        txt = MIMEText('Bonjour'+genre+' '+nom+' '+prenom+','+'\n'+base+'.\nRendez-vous datant du '+dateday+'/'+datemonth+'/'+dateyear+'.\n\nCompte rendu :\n'+explication+'.\n\nCordialement,\nPatrick REVERDY\n[Pédicure-Podologue]\n14 Rue de Boigne, 73000, Chambéry | 04-79-85-57-33'+rajout)
        msg.attach(txt)

        filename = '[MAIL]\\logo.png' #path to file
        fo=open(filename,'rb')
        attach = email.mime.application.MIMEApplication(fo.read(),_subtype="png")
        fo.close()
        attach.add_header('Content-Disposition','attachment',filename='logo.png')
        msg.attach(attach)

        filename = '[PJ]\\bilan.pdf' #path to file
        fo=open(filename,'rb')
        attach = email.mime.application.MIMEApplication(fo.read(),_subtype="pdf")
        fo.close()
        attach.add_header('Content-Disposition','attachment',filename='Bilan.pdf')
        msg.attach(attach)

        s.send_message(msg)
        s.quit()

        messagebox.showinfo("Email envoyé","L'email a été envoyé avec succès à "+mail+" !")
        wipe()

    except:
        if noproblem == 0:
            messagebox.showwarning("Erreur","Un problème est survenu ! Vérifiez votre connexion internet !")
        
################################################


##############   TKINTER   #########################

app = Tk()
app.title('SendMail.Py | V 3.2')
app.iconbitmap("custom.ico")

global var
var = IntVar()
 
def result():
    print(var.get())


    #Centrer fenetre tkinter
screen_x = app.winfo_screenwidth()
screen_y = app.winfo_screenheight()
windows_x = 750
windows_y= 945

posX = (screen_x // 2)- (windows_x //2)
posY = (screen_y // 2)- (windows_y //2)
geo= "{}x{}+{}+{}".format(windows_x, windows_y, posX, posY)

app.geometry(geo)

    #redimensionable = False
app.resizable(width=False, height=False)

    #title
mainframe = LabelFrame(app, text='[By Gugus | reverdyguillaume73@gmail.com]',font=("Russo One","12"), borderwidth='5px',cursor='X_cursor')#,"italic" 
mainframe.grid(row=0, column=1, pady=10, padx=20)
label_welcome = Label(mainframe, text="SendMail.Py",font=("Roboto Slab Light","25","bold" ))
label_welcome.grid(row=0, column=3, pady=15, padx=80)

    #mail
mailframe = LabelFrame(app, text='[Mail]',font=("Comic Sans MS","10","italic" ))
mailframe.grid(row=2, column=1, pady=15, padx=30)
label_mail = Label(mailframe, text="Mail :", font=("Catamaran Medium","16" ))#font=("Comic Sans MS","12" )
label_mail.grid(row=2, column=3, pady=15, padx=10)
entry_mail= Entry(mailframe, width=40, borderwidth='2px',cursor='bottom_side', font=("Catamaran Medium","16" ) )  #pressepapier -> exportselection=0
entry_mail.grid(row=2, column=5, pady=15, padx=20)

    #Nom
nomframe = LabelFrame(app, text='[Nom]',font=("Comic Sans MS","10","italic" ))
nomframe.grid(row=3, column=1, pady=15, padx=30)
label_nom = Label(nomframe, text="Nom :", font=("Catamaran Medium","14" ))
label_nom.grid(row=2, column=3, pady=15, padx=10)
entry_nom= Entry(nomframe, width=30, borderwidth='2px',cursor='bottom_side', font=("Catamaran Medium","14"))  #pressepapier -> exportselection=0
entry_nom.grid(row=2, column=5, pady=15, padx=20)

    #prenom
prenomframe = LabelFrame(app, text='[Prenom]',font=("Comic Sans MS","10","italic" ))
prenomframe.grid(row=4, column=1, pady=15, padx=30)
label_prenom = Label(prenomframe, text="Prénom :", font=("Catamaran Medium","14" ))
label_prenom.grid(row=2, column=3, pady=15, padx=10)
entry_prenom= Entry(prenomframe, width=25, borderwidth='2px',cursor='bottom_side', font=("Catamaran Medium","14"))  #pressepapier -> exportselection=0
entry_prenom.grid(row=2, column=5, pady=15, padx=20)

    #details
detailframe = LabelFrame(app, text='[Détails]',font=("Comic Sans MS","10","italic" ))
detailframe.grid(row=5, column=1, pady=15, padx=30)
label_detail = Label(detailframe, text="Détails :", font=("Catamaran Medium","14" ))
label_detail.grid(row=2, column=3, pady=15, padx=10)
entry_detail= Entry(detailframe, width=50,borderwidth='2px',cursor='bottom_side', font=("Catamaran Medium","14"))  #pressepapier -> exportselection=0
entry_detail.grid(row=2, column=5, pady=15, padx=20)

    #radiobutton
radiobuttonframe = LabelFrame(app, text='[Genre]',font=("Comic Sans MS","10","italic" ))
radiobuttonframe.grid(row=6, column=1, pady=15, padx=30)

radio_widget = Radiobutton(radiobuttonframe, text='Mlle',variable=var, value=1, font=("Catamaran Medium","15" ), borderwidth='2px',cursor='circle')#state=DISABLED
radio2_widget = Radiobutton(radiobuttonframe, text='Mme',variable=var, value=2, font=("Catamaran Medium","15" ), borderwidth='2px',cursor='circle')
radio3_widget = Radiobutton(radiobuttonframe, text='Mr',variable=var, value=3, font=("Catamaran Medium","15" ), borderwidth='2px',cursor='circle')
radio4_widget = Radiobutton(radiobuttonframe, text='none',variable=var, value=0, font=("Catamaran Medium","15" ), borderwidth='2px',cursor='circle')

radio4_widget.grid(row=6, column=4)
radio_widget.grid(row=7, column=4, pady=15, padx=30)
radio2_widget.grid(row=6, column=5)
radio3_widget.grid(row=7, column=5, pady=15, padx=30)

    #Bouton
buttonframe = LabelFrame(app, text='[SendMail]',font=("Comic Sans MS","10","italic" ))
buttonframe.grid(row=8, column=1, pady=15, padx=30)
valid_btn = Button(buttonframe, text=" Envoyer ", command=mail,font=("Comic Sans MS","15" ), borderwidth='5px',cursor='iron_cross')
valid_btn.grid(row=8, column=3, pady=15, padx=30)

app.mainloop()
################################################
