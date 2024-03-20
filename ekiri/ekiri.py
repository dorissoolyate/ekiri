import email
from http import server
from msilib.schema import File
from tkinter import *
import smtplib,ssl #lja servera po4toovogo i logina
from email.message import EmailMessage
import imghdr
from tkinter import filedialog
from tkinter import messagebox, filedialog
def saada_k():
    kellele=e_box.get()
    kiri=k_box.get("1.0",END)
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="aga70347@gmail.com"
    password="ggnr rojs jcux meiu"
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg["Subject"]="hehe"
    msg["From"]="hehe"
    msg["To"]=kellele
    with open(file,"rb") as fpilt:
        pilt=fpilt.read()
    msg.add_attachment(pilt,maintype="image",subtype=imghdr.what(None,pilt))    
    try:
        server=smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(sender_email,password)
        server.send_message(msg)
        print("Valmis")
        #aruanne et kiri saadetud Messagebox()
    except Exception as e:
        print(e)#tk interis
    finally:
        server.quit()


file="mail1.png"        
def vali_pilt():
    global file
    file=filedialog.askopenfilename()
    return file


root=Tk()
root.geometry("400x300") 
root.title("E-kirja saatmine")
root.iconbitmap("mail.ico")

l_mail=Label(root,text="Email: ",fg="#000000",font="Candara 16",height=1,width=8)
l_kiri=Label(root,text="Kiri: ",fg="#000000",font="Candara 16",height=1,width=8)
e_box=Entry(root,bg="#cfe2f3",fg="#000000",font="Candara 12",width=30,justify=LEFT)
k_box=Text(root,bg="#cfe2f3",fg="#000000",font="Candara 12",height=6,width=30)
b_saada=Button(root,text="Saada",bg="lightblue",font="Candara 16",relief=RAISED,command=saada_k)
b_pilt=Button(root,text="Pilt",bg="lightblue",font="Candara 16",relief=RAISED,command=vali_pilt)


l_mail.grid(row=0,column=0)
e_box.grid(row=0,column=1,columnspan=2)
l_kiri.grid(row=1,column=0)
k_box.grid(row=1,column=1,columnspan=2)
b_saada.grid(row=2,column=2)
b_pilt.grid(row=2,column=1)

root.mainloop()
