import os
import smtplib
import optparse
from getpass import  getpass

p = optparse.OptionParser()
p.add_option("-m", dest="message",help="Message")
p.add_option("-t", dest="to", help="recipient's mail")
p.add_option("-n", dest="number",help="Number of mails")
p.add_option("-c", dest="config",help="-c do/check")
(options, arguments) = p.parse_args()
con = options.config

def confc():
    if(os.path.exists("config.txt") == 0):
        conftext = open("config.txt","w")
        conftext.close()
    if(os.stat("config.txt").st_size == 0):
        print ("\033[0;31;47mYour config file is empty!\033[0m")
    else:
        print("\033[1;32;40mYour bomber0 is already configured!\033[0m")

def confd():
    if(os.path.exists('config.txt') == 0 ):
        conftext = open("config.txt","w")
        conftext.close()
    if(os.stat("config.txt").st_size == 0):
        print ("\033[0;31;47mYour config file is empty!\033[0m")
    else:
        print("\033[1;32;40mYour bomber0 is already configured!\033[0m")

    smtp = raw_input("SMTP Server : ")
    port = raw_input("Port : ")
    Uname = raw_input("Username : ")
    Pwd = getpass("Password : ")
    context = open("config.txt","w")
    context.write(smtp+','+port+','+Uname+','+Pwd)
    context.close()

def send(m,to,num):
    with open("config.txt","r") as c:
        for x in c:
            config = x.strip().split(",")
    mail = smtplib.SMTP(config[0],config[1])
    mail.ehlo()
    mail.starttls()
    mail.login(config[2],config[3])
    for x in range (1, int(num) + 1 ):
        mail.sendmail(config[2],to,m)
        print('\033[92m'"[+] "+str(x)+" mail sent out of "+str(num)+" !"'\033[0m')

if(con == 'do'):
    confd()

if(con == 'check'):
    confc()

if(options.to > 0):
    if(os.path.exists("config.txt") == 0):
        confile = open("config.txt","w")
        confile.close()
    if(os.stat("config.txt").st_size==0):
        print ("\033[0;31;47mConfig the bomber first!\033[0m")
    else:
        send(options.message,options.to,options.number)
