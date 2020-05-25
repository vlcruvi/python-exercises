#!/usr/bin/env python3

import sys
import requests
import json
import ast

def printing(url):
	#headers = {"accept" : "*/*", 
	#"accept-encoding": "gzip, deflate", 
	#"accept-Language" : "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7", 
	#"Cookie": connect.headers["Set-Cookie"], 
	#"Host": "blackjack.runcode.ninja", 
	#"Origin" : "http://blackjack.runcode.ninja", 
	#"Referer": "http://blackjack.runcode.ninja/",
	#"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36", 
	#"X-Requested-With": "XMLHttpRequest"
	#}
	url  = url + "/bj.php"
	#Creating a session
	session = requests.get(url)

	
	with requests.Session() as sess:
		
		print(sess)
		words = ["deal", "hit", "stay"]
		n = 0
		while n < 5:
			for word in words:
				response = sess.post(url, data={"do_what" : word})
				flag = {}
				if "flag" in response.text:
					flag = ast.literal_eval(response.text)
					print(flag["flag"])
					break
			n += 1




def main():
	url = sys.argv[1]
	printing(url)


main()