import telebot,os
import re,json
import requests
import telebot,time,random
import random
import sys
import string
from telebot import types
from gatet import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
GREEN = '\033[92m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
stopuser = {}
token = '6209431758:AAG6NEYSynGGhmiN70AIZ6wt_fcCcT3lGrw'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin=1076515841
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
			keyboard.add(contact_button)
			random_number = random.randint(33, 82)
			video_url = f'https://t.me/all_nas/80'
			bot.send_video(chat_id=message.chat.id, video=video_url, caption=f'''<b>𝘩𝘪 𝘣𝘢𝘣𝘺 : {name} 🧸.
𝘤𝘰𝘮𝘮𝘢𝘯𝘥 𝘤𝘩𝘦𝘤𝘬: /cmds ⚙.
𝘣𝘺 : iiiiZZi.t.me 💸 .{BL}</b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="🔺 𝘩𝘦𝘳𝘦 🔻", url="https://t.me/diyxar")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(33, 82)
		video_url = f'https://t.me/all_nas/80'
		bot.send_video(chat_id=message.chat.id, video=video_url, caption='''𝘴𝘦𝘯𝘥 /𝘤𝘮𝘥𝘴 𝘵𝘰 𝘴𝘩𝘰𝘸 𝘢𝘭𝘭 𝘤𝘰𝘮𝘮𝘢𝘯𝘥 𝘰𝘳 𝘴𝘦𝘯𝘥 𝘧𝘪𝘭𝘦 𝘳𝘶𝘯𝘯𝘪𝘯𝘨 𝘤𝘩𝘦𝘤𝘬 .
𝘣𝘺 : iiiiZZi.t.me 💸. ''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"🇮🇶 {BL}  🇮🇶",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
𝘵𝘩𝘦𝘴𝘦 𝘢𝘳𝘦 𝘵𝘩𝘦 𝘣𝘰𝘵,𝘴 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴 

~ 𝘣𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦 𝘢𝘶𝘵𝘩 - /chk 𝘯𝘶𝘮|𝘮𝘮|𝘺𝘺|𝘤𝘷𝘤
~ 𝘴𝘵𝘢𝘵𝘶𝘴 𝘰𝘯 ✅ .

~ 3𝘥𝘴 𝘭𝘰𝘰𝘬𝘶𝘱 - /vbv 𝘯𝘶𝘮|𝘮𝘮|𝘺𝘺|𝘤𝘷𝘤
~ 𝘰𝘯 𝘳𝘶𝘯𝘯𝘪𝘯𝘨 ✅.

𝘣𝘺 : iiiiZZi.t.me 💸 .</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶'
		if BL == '🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘩𝘪 𝘣𝘢𝘣𝘺 : {name} 🧸.
𝘤𝘰𝘮𝘮𝘢𝘯𝘥 𝘤𝘩𝘦𝘤𝘬: /cmds ⚙.
𝘣𝘺 : iiiiZZi.t.me 💸 .{BL}</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘩𝘪 𝘣𝘢𝘣𝘺 : {name} 🧸.
𝘤𝘰𝘮𝘮𝘢𝘯𝘥 𝘤𝘩𝘦𝘤𝘬: /cmds ⚙.
𝘣𝘺 : iiiiZZi.t.me 💸 . {BL}</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘺𝘰𝘶 𝘤𝘢𝘯𝘯𝘰𝘵 𝘶𝘴𝘦 𝘵𝘩𝘦 𝘣𝘰𝘵 𝘣𝘦𝘤𝘢𝘶𝘴𝘦 𝘺𝘰𝘶𝘳 𝘴𝘶𝘣𝘴𝘤𝘳𝘪𝘱𝘵𝘪𝘰𝘯 𝘩𝘢𝘴 𝘦𝘹𝘱𝘪𝘳𝘦𝘥 ⌛️🪫 .

𝘳𝘦𝘴𝘶𝘣𝘴𝘤𝘳𝘪𝘣𝘦. 𝘤𝘰𝘯𝘵𝘢𝘤𝘵 𝘵𝘩𝘦 𝘥𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 : iiiiZZi.t.me 💸 .</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"🔱 𝘣𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦 𝘢𝘶𝘵𝘩 🔱",callback_data='br')
		#sw = types.InlineKeyboardButton(text=f" 𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 🪽",callback_data='str')
		keyboard.add(contact_button)
		#keyboard.add(sw)
		bot.reply_to(message, text=f'𝘤𝘩𝘰𝘰𝘴𝘦 𝘸𝘩𝘢𝘵 𝘺𝘰𝘶 𝘸𝘢𝘯𝘵 𝘩𝘦𝘳𝘦 𝘵𝘰 𝘨𝘦𝘵 𝘴𝘵𝘢𝘳𝘵𝘦𝘥 .\nby : iiiiZZi.t.me 💸 .',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'str')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='stripe charge'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘸𝘢𝘪𝘵 𝘧𝘰𝘳 𝘪𝘵 𝘵𝘰 𝘴𝘵𝘢𝘳𝘵 ... ⏱")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝘵𝘩𝘦 𝘴𝘤𝘢𝘯 𝘩𝘢𝘴 𝘴𝘵𝘰𝘱𝘱𝘦𝘥 ✅/n𝘣𝘺 : iiiiZZi.t.me 💸 .')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(st(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• Status : {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• Charge ✅ ➜ [ {ch} ] •", callback_data='x')
					#ccn = types.InlineKeyboardButton(f"• CCN ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• Declind ❌ ➜ [ {dd} ] •", callback_data='x')
					#risk = types.InlineKeyboardButton(f"• 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• Total : [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"~ Stop ~", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''Please Wait While Your Cards Are Being Check At The Gateway : {gate} ./nby : iiiiZZi.t.me 💸 .''', reply_markup=mes)
					
					msg=f'''<b>CC - ↯  {cc}
Status - ↯ #Gharge ✅  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸. </b>'''
					msgc=f'''<b>CC - ↯  {cc}
Status - ↯ #CCN ✅  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸. </b>'''
					msgf=f'''<b>CC - ↯  {cc}
Status - ↯ #Insufficient Funds ✅  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸.</b>'''
					if 'success' in last:
						ch += 1
						bot.send_message(call.from_user.id, msg)
					elif "funds" in last:
						bot.send_message(call.from_user.id, msgf)
						live+=1
					elif "card's security" in last:
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(15)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='been Completed from  Checked ✅ ./nby : iiiiZZi.t.me 💸.')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘸𝘢𝘪𝘵 𝘧𝘰𝘳 𝘪𝘵 𝘵𝘰 𝘴𝘵𝘢𝘳𝘵 ... ⏱")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝘵𝘩𝘦 𝘴𝘤𝘢𝘯 𝘩𝘢𝘴 𝘴𝘵𝘰𝘱𝘱𝘦𝘥 ✅./n𝘣𝘺 : iiiiZZi.t.me 💸 .')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• Status : {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• Approved ✅ ➜ [ {live} ] •", callback_data='x')
					#ccn = types.InlineKeyboardButton(f"• CCN ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• Declined ❌ ➜ [ {dd} ] •", callback_data='x')
					#risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• Total : [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"~ Stop ~", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''Please Wait While Your Cards Are Being Check At The Gateway : {gate} ./nby : iiiiZZi.t.me 💸 .''', reply_markup=mes)
					
					msg=f'''<b>CC - ↯  {cc}
Status - ↯ #Approved ✅  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸. </b>'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(4)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='been Completed from  Checked ✅ ./nby : iiiiZZi.t.me 💸.')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.au') or message.text.lower().startswith('/au'))
def respond_to_vbv(message):
	gate='stripe Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶'
	if BL == '🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘩𝘪 𝘣𝘢𝘣𝘺 : {name} 🧸.
𝘤𝘰𝘮𝘮𝘢𝘯𝘥 𝘤𝘩𝘦𝘤𝘬: /cmds ⚙.
𝘣𝘺 : iiiiZZi.t.me 💸 . {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘩𝘪 𝘣𝘢𝘣𝘺 : {name} 🧸.
𝘤𝘰𝘮𝘮𝘢𝘯𝘥 𝘤𝘩𝘦𝘤𝘬: /cmds ⚙.
𝘣𝘺 : iiiiZZi.t.me 💸 . {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘺𝘰𝘶 𝘤𝘢𝘯𝘯𝘰𝘵 𝘶𝘴𝘦 𝘵𝘩𝘦 𝘣𝘰𝘵 𝘣𝘦𝘤𝘢𝘶𝘴𝘦 𝘺𝘰𝘶𝘳 𝘴𝘶𝘣𝘴𝘤𝘳𝘪𝘱𝘵𝘪𝘰𝘯 𝘩𝘢𝘴 𝘦𝘹𝘱𝘪𝘳𝘦𝘥 ⌛️🪫 .

𝘳𝘦𝘴𝘶𝘣𝘴𝘤𝘳𝘪𝘣𝘦. 𝘤𝘰𝘯𝘵𝘢𝘤𝘵 𝘵𝘩𝘦 𝘥𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 : iiiiZZi.t.me 💸 .</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘸𝘢𝘪𝘵 𝘧𝘰𝘳 𝘪𝘵 𝘵𝘰 𝘴𝘵𝘢𝘳𝘵 ... ⏱").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(scc(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>CC - ↯  {cc}
Status - ↯ #Approved ✅  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸.</b>'''
	msgd=f'''<b>CC - ↯  {cc}
Status - ↯ #Declind 🚫  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸.</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='Braintree Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶'
	if BL == '🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘩𝘪 𝘣𝘢𝘣𝘺 : {name} 🧸.
𝘤𝘰𝘮𝘮𝘢𝘯𝘥 𝘤𝘩𝘦𝘤𝘬: /cmds ⚙.
𝘣𝘺 : iiiiZZi.t.me 💸 . {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘩𝘪 𝘣𝘢𝘣𝘺 : {name} 🧸.
𝘤𝘰𝘮𝘮𝘢𝘯𝘥 𝘤𝘩𝘦𝘤𝘬: /cmds ⚙.
𝘣𝘺 : iiiiZZi.t.me 💸 . {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘺𝘰𝘶 𝘤𝘢𝘯𝘯𝘰𝘵 𝘶𝘴𝘦 𝘵𝘩𝘦 𝘣𝘰𝘵 𝘣𝘦𝘤𝘢𝘶𝘴𝘦 𝘺𝘰𝘶𝘳 𝘴𝘶𝘣𝘴𝘤𝘳𝘪𝘱𝘵𝘪𝘰𝘯 𝘩𝘢𝘴 𝘦𝘹𝘱𝘪𝘳𝘦𝘥 ⌛️🪫 .

𝘳𝘦𝘴𝘶𝘣𝘴𝘤𝘳𝘪𝘣𝘦. 𝘤𝘰𝘯𝘵𝘢𝘤𝘵 𝘵𝘩𝘦 𝘥𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 : iiiiZZi.t.me 💸 .</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘸𝘢𝘪𝘵 𝘧𝘰𝘳 𝘪𝘵 𝘵𝘰 𝘴𝘵𝘢𝘳𝘵 ... ⏱").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>CC - ↯  {cc}
Status - ↯ #Approved ✅  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸.</b>'''
	msgd=f'''<b>CC - ↯  {cc}
Status - ↯ #Declind 🚫  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸.</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.str') or message.text.lower().startswith('/str'))
def respond_to_vbv(message):
	gate='stripe charge'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶'
	if BL == '🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘩𝘪 𝘣𝘢𝘣𝘺 : {name} 🧸.
𝘤𝘰𝘮𝘮𝘢𝘯𝘥 𝘤𝘩𝘦𝘤𝘬: /cmds ⚙.
𝘣𝘺 : iiiiZZi.t.me 💸 . {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘩𝘪 𝘣𝘢𝘣𝘺 : {name} 🧸.
𝘤𝘰𝘮𝘮𝘢𝘯𝘥 𝘤𝘩𝘦𝘤𝘬: /cmds ⚙.
𝘣𝘺 : iiiiZZi.t.me 💸 . {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘺𝘰𝘶 𝘤𝘢𝘯𝘯𝘰𝘵 𝘶𝘴𝘦 𝘵𝘩𝘦 𝘣𝘰𝘵 𝘣𝘦𝘤𝘢𝘶𝘴𝘦 𝘺𝘰𝘶𝘳 𝘴𝘶𝘣𝘴𝘤𝘳𝘪𝘱𝘵𝘪𝘰𝘯 𝘩𝘢𝘴 𝘦𝘹𝘱𝘪𝘳𝘦𝘥 ⌛️🪫 .

𝘳𝘦𝘴𝘶𝘣𝘴𝘤𝘳𝘪𝘣𝘦. 𝘤𝘰𝘯𝘵𝘢𝘤𝘵 𝘵𝘩𝘦 𝘥𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 : iiiiZZi.t.me 💸 .</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘸𝘢𝘪𝘵 𝘧𝘰𝘳 𝘪𝘵 𝘵𝘰 𝘴𝘵𝘢𝘳𝘵 ... ⏱").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(st(cc))
	except Exception as e:
		last='Error'
		print(e)
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msgd=f'''<b>CC - ↯  {cc}
Status - ↯ #Rejectd 🚫  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸.</b>'''
	msg=f'''<b>CC - ↯  {cc}
Status - ↯ #Gharge ✅  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸.</b>'''
	msgc=f'''<b>CC - ↯  {cc}
Status - ↯ #CCN ✅  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸.</b>'''
	msgf=f'''<b>CC - ↯  {cc}
Status - ↯ #Insufficient Funds ✅  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸.</b>'''
	if 'success' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	elif "funds" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgf)
	elif "card's security" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgc)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>Hi . | 7X Bot - ViP Subscribed ✅ .\n~ Expires in : {timer} .\n~Type : {typ} .\n\nby : iiiiZZi.t.me 💸.</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='7X-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝘱𝘢𝘪𝘥'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>New Key Created ✅ .

~Plan : {plan} . 
~Expires in : {ig} .
~Key : <code>{pas}</code> .
~Use : [ /redeem ] - [ K.Y ] 
by : iiiiZZi.t.me 💸 .</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='3D Lookup'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶",
  "timer": "none",
			}
		}
		BL='🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘩𝘪 𝘣𝘢𝘣𝘺 : {name} 🧸.
𝘤𝘰𝘮𝘮𝘢𝘯𝘥 𝘤𝘩𝘦𝘤𝘬: /cmds ⚙.
𝘣𝘺 : iiiiZZi.t.me 💸 . {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘩𝘪 𝘣𝘢𝘣𝘺 : {name} 🧸.
𝘤𝘰𝘮𝘮𝘢𝘯𝘥 𝘤𝘩𝘦𝘤𝘬: /cmds ⚙.
𝘣𝘺 : iiiiZZi.t.me 💸 . {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚜ 𝘰𝘸𝘯𝘦𝘳 ⚜", url="https://t.me/iiiiZZi")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝘺𝘰𝘶 𝘤𝘢𝘯𝘯𝘰𝘵 𝘶𝘴𝘦 𝘵𝘩𝘦 𝘣𝘰𝘵 𝘣𝘦𝘤𝘢𝘶𝘴𝘦 𝘺𝘰𝘶𝘳 𝘴𝘶𝘣𝘴𝘤𝘳𝘪𝘱𝘵𝘪𝘰𝘯 𝘩𝘢𝘴 𝘦𝘹𝘱𝘪𝘳𝘦𝘥 ⌛️🪫 .

𝘳𝘦𝘴𝘶𝘣𝘴𝘤𝘳𝘪𝘣𝘦. 𝘤𝘰𝘯𝘵𝘢𝘤𝘵 𝘵𝘩𝘦 𝘥𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 : iiiiZZi.t.me 💸 .</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '🇮🇶 𝘧𝘳𝘦𝘦 🇮🇶'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "𝘸𝘢𝘪𝘵 𝘧𝘰𝘳 𝘪𝘵 𝘵𝘰 𝘴𝘵𝘢𝘳𝘵 ... ⏱").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		response = requests.post(
		f'https://rimuruchkbot.alwaysdata.net/vbv.php?bin={cc}')
		last=(response.json()['result'])
		if 'result not found' in last:
			last='Authenticate Frictionless Failed'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>CC - ↯  {cc}
Status - ↯ #Passed ✅  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸.</b>'''
	msgd=f'''<b>CC - ↯  {cc}
Status - ↯ #Rejectd 🚫  
R/s - ↯ {last} .
Gate - ↯ {gate} . ⛈️
info - ↯ {card_type} ~ {brand}
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯ {cc[:6]}
Country - ↯ {country} ~ {country_flag}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Proxy's : [ proxy live ✅ ] 
Power Mode - ↯ [ ON ]
Time : {"{:.1f}".format(execution_time)} .
- - - - - - - - - - - - - - - - - - - - -
By : iiiiZZi.t.me 💸.</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'


#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
#animation = [f"[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

#for i in range(len(animation)):
    #time.sleep(0.2)
    #sys.stdout.write("\r" + animation[i % len(animation)])
    #sys.stdout.flush()

#print("\n")

print(f"{GREEN}Bot Runing Don ~ iiiiZZi.t.me .{GREEN}")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"an error occurred : {e}")
