from tkinter import *
import smtplib
from tkinter import messagebox

# making tkinter window
root = Tk()
root.geometry('500x500')
root.title('Email Sender @vic')
root.resizeable(False, False)
root.config(bg="#ffff")

# variable for entryb box
Email = StringVar()
Password = StringVar()
To = StringVar()
Subject = StringVar()

# layout for sign in form

def email_login():
    f = Frame(root, height=480, width=500, bg='#FFF' )
    Label(f, text="Sign in", font=('Helvetica', 30, "bold"), fg='#2F9DFF', bg='#FFF').place(x=180, y=120)
    Label(f, text="to continue to email", font=('Helvetica', 12, "bold"), fg='#666A6C', bg='#FFF').place(x=170, y=170)

    Label(f, text='Email', font=('Helvetica', 12, "bold"), fg='#4C4A49', bg='#FFF').place(x=140, y=210)
    email = Entry(f, textVariable=Email, font=('calibre', 10, 'normal'), width=30, bg="#E2E2E2")
    email.place(x=140, y=230)

       
    Label(f, text='Password', font=('Helvetica', 12, "bold"), fg='#4C4A49', bg='#FFF').place(x=140, y=280)
    password = Entry(f, textVariable=Password, font=('calibre', 10, 'normal'), width=50, bg="#E2E2E2")
    password.place(x=140, y=300)


    Button(f, text='NEXT', font=('Helvetica', 10, "bold"), bg='#2F9DFF', fg='#FFF', command=mail_verification).place(x=300, y=330)
    f.place(x=1, y=1)   


    Label(f, text='Note: ', font=('Helvetica', 10, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=400)
    Label(f, text='1. Please try another email address.', font=('Helvetica', 8, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=420)
    Label(f, text='2. Remove email authentication for testing.', font=('Helvetica', 8, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=440)
    Label(f, text=' or use a temporary email.', font=('Helvetica', 8, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=460)
    f.place(x=0, y=0)




# design portion
def layout():
    global body
    f = Frame(root, height=480, width=500, bg='#FFF' )
    Label(f, text='New Message', font=('Helvetica', 12, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=20)
   
    Label(f, text='From', font=('Helvetica', 12, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=60)
    Label(f, text=f"<{Email.get()}>", font=("Helvetica", 12, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=80)

       
    Label(f, text='To', font=('Helvetica', 12, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=130)
    to = Entry(f, textVariable=To, font=('calibre', 10, 'normal'), width=50, bg="#E2E2E2")
    to.place(x=20, y=150)

    Label(f, text='Subject', font=('Helvetica', 12, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=170)
    subject = Entry(f, textVariable=Subject, font=('calibre', 10, 'normal'), width=50, bg="#E2E2E2")
    subject.place(x=20, y=190)

    Label(f, text='Body', font=('Helvetica', 12, "bold"), fg='#4C4A49', bg='#FFF').place(x=20, y=210)
    body = Text(f, font=('calibre', 10, 'normal'), width=50, bg="#E2E2E2", height=12)
    body.place(x=20, y=230)

    Button(f, text='Send', font=('Helvetica', 12, "bold"), bg='#2F9DFF', fg='#FFF', command=mail_sending).place(x=20, y=440)
    f.place(x=1, y=1)

# function to verify the email address procided by the user is valid 
def mail_verification():
    global server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.eclo()
    server.starttls()
    server.ehlo()
    try:
        server.login(Email.get(), Password.get())
        layout()
    except Exception:
        messagebox.showerror('Sign in Error!', 'Please check your login information is correct')

#send email after verification
def mail_sending():
    subject = Subject.get()
    body_text = body.get("1.0", "end-1c")
    message = f"Subject : {subject} \n\n {body_text}"
    server.sendmail
    (
        Email.get(), To.get(). message
    )
    messagebox.showinfo('Sucess!', 'Mail has been sent')

if __name__ == '__main__':
    emaillogin()
    root.mainloop()
