from telethon import TelegramClient, events
import openai
import time
from apis import api_id_,api_hash_,openai_api_key,concept_
concept=concept_   #this is what you tell the ai to do, for example' be a helpfull asistant'
api_id = api_id_     #your telethon api
api_hash = api_hash_    #telethon hash
openai.api_key = openai_api_key #your chatgpt 

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
   
    if 'mani_iu' in event.raw_text:  
        messages = [{'role': 'system', 'content': concept}]    
        user_message = event.raw_text
        if user_message:
            messages.append({'role': 'user', 'content': user_message})
            chat = openai.ChatCompletion.create(model='gpt-4', messages=messages)
            reply = chat.choices[0].message.content
            #time.sleep(2) 
            await event.reply(reply)
            
print('Trying to connect')
client.start()
print('connected!')
client.run_until_disconnected()
