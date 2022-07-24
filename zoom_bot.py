'''
Hi!!, Eshu welcome's you. Hope you  are doing well!!..

'''
'''
Usage : first install all requirements using command prompt...
ex : pip install selenium==3.141.0
likewise install all requirements..

'''
'''
Before starting this you have to download chromedriver
To download chromerdriver follow the steps I have given in a steps_to_download_chromedriver.txt file.. check that out
'''

#Let's let started!!...
''' 
Importing all the rerquired libraries..
'''
#from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from discord_webhooks import DiscordWebhooks
import keyboard




''' Interacting with discord..
Ignore this if you face any difficulty
 '''
# this is my webhook url.. You can go through youtube and search for dicord webhook, if you dont know about this
webhook_url = "https://discord.com/api/webhooks/9-------xxxxxxxxxx------7cgmJhLT"#put your webhook url here...

def send_msg():
    WEBHOOK_URL = webhook_url
    webhook = DiscordWebhooks(WEBHOOK_URL)
    webhook.set_footer(text='Eshwar Namala')      #you can give your desire messages..
    webhook.set_content(title='Hey Eshu!!!..\nYour Bot is Joining your Class!!!.....',
                        description="Here you gooooo!!!....\nNow No worries of missing Class\nChill out with your works!!!\n :sunglasses: \U0001F973 \U0001F973 ")
    
    webhook.send()

    print("Sent message to Discord!!...")
#completion of discord webhooks
#you can ignore this ,,its up to you...


''' Here is the code for bot '''

#driver = webdriver.Chrome(chrome_options=opt, service_log_path='NUL')
driver = webdriver.Chrome("C:\\eshu\\chromedriver.exe") #give the path of the chromedriver

#driver = None
#URL = "https://zoom.us/join/"

url = "https://us04web.zoom.us/j/----xxxxxxxxxxx-------xxx----T09/" #Put the link of your class here...
#creds = {'z_id':'your_id' , 'pwd' : 'password'}

driver.get(url)

print("Hey buddy Joined...")

#these below steps for closing the popup
keyboard.send("tab", do_press=True, do_release=True)
keyboard.send("tab", do_press=True, do_release=True)
keyboard.send("enter", do_press=True, do_release=True)
time.sleep(5)

#it will send message to my discord about the class...
send_msg()


driver.quit()

print("You are done Eshu!!!....")

'''
NOTE : You have to set some settings in your zoom 
   i.e., always mute before joining and
    always turnoff video before joining
    connect to audio before joining
   you can find these settings in zoom settings..go through it and and use the bot 
'''
'''
Once execute this bot, after all settings are done,, and check if it is working..
if it's working,, Then Schedule this program using (Task Scheduler) tool which is present in built in windows
or else go through youtube on how to schedule a task using task scheduler..'''

'''
Thank you!!!...
~eshu
Signing off....
'''