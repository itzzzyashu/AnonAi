# Project Anon Ai
# developed by @itzzzyashu
# Update 4.0.1

# Packages
#   speech_recognition as sr 
#   datetime
#   wikipedia
#   pyttsx3
#   webbrowser
#   random
#   os

ainame = "Anon"
__version__ = "4.0.1" 


# Importing packages and config variables
import os
import html
import time
import pyjokes
import random
import requests
import pyttsx3
import datetime
# import *
import wikipedia
import webbrowser
import speech_recognition as sr 
from datetime import datetime, date

from config import Config
NAME = Config.NAME
CLASS = Config.CLASS
AGE = Config.AGE
CNT = Config.CNT
AIAPI = Config.AIAPI
# TFT
anon_path = Config.anon_path
music_dir = Config.music_dir
pics_dir = Config.pics_dir
video_dir = Config.video_dir
hidden_dir = Config.hidden_dir
xsearch = Config.xsearch


# Activate Speech Recognition & Voice Reply.
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    #info = wikipedia.summary(person,1)

# Late Night is now dependent on user's age
if AGE >= 13:
    LATE_NIGHT = True
else:
    LATE_NIGHT = False

# Time Importing
hour = int(datetime.now().hour)
minute = int(datetime.now().minute)
second = int(datetime.now().second)
datetime.now().strftime('%I : %M : %p')
'''
if TFT == 24:
    tym = '{}:{}:{}'.format(hour, minute, second)
elif TFT == 12:
    if hour > 12:
        hrs = hour-12
        tym = "{}:{}:{} PM {}".format(hrs, minute, second, CNT)
    elif hour < 12:
        tym = "{}:{}:{} AM {}".format(hour, minute, second, CNT)
    else:
        tym = "⚠ ERROR IN 12 HOUR FORMAT"
else:
    tym = "⚠ ERROR IN 24 HOUR FORMAT"
'''

# Date Importing
if CNT == 'UTC':
    date = "%d %m %Y, %A UTC"
    date_fmt = datetime.utcnow().strftime(date)
elif CNT == 'IST':
    date = date.today()
    date_fmt = date.strftime("%d %b %Y, %A")
else:
    print("⚠ ERROR IN COUNTRY DATE")
    talk("⚠ ERROR IN COUNTRY DATE")

dttm=f'''\n
||                                     ||
{time.strftime("%H:%M:%S - %d/%m/%Y", time.localtime(time.time()))} {CNT}
||                                     ||
'''

# Wishing message
print(f"\n|| =============== Started {ainame} AI {__version__} =============== ||")
print(dttm)
talk(dttm)
if hour >= 6 and hour<12:
    print(f"\n{ainame}:\nGood Morning {NAME} 😄")
    talk(f"\nGood Morning {NAME}")

elif hour >= 12 and hour < 16 :
    print(f"\n{ainame}:\nGood Afternoon {NAME} 😄")
    talk(f"\nGood Afternoon {NAME}")

elif hour >= 16 and hour < 22:
    print(f"\n{ainame}:\nGood Evening {NAME} 😄")
    talk(f"\nGood Evening {NAME}")

elif hour >= 22 or (hour >= 0 and hour < 6):
    if LATE_NIGHT == False:
        print(f"{ainame}:\nTime is {datetime.now().strftime('%I : %M %p')} yet, you should sleep now. 💤")
        talk(f"Time is {datetime.now().strftime('%I : %M %p')} yet, you should sleep now.")
        if CLASS < 10:
            print("also you have to study for your exams.\nClosing programs & PC. 😁")
            talk("also you have to study for your exams.\nClosing programs & PC.")
            os.startfile('shutdown -p')
            time.sleep(10)
            exit()
    elif LATE_NIGHT == True:
        print(f"\n{ainame}:\nGood Night {NAME} 😄")
        talk(f"\nGood Night {NAME}")

# STARTS AI WORK
def run_anon():
    #command = take_command()
    command = input("⪼  ⪼  ")
    command=command.lower()
    if "help" in command:
        help_section=f'''
Hey {NAME} I'm {ainame} 💁🏻‍♂️,
I can help you with these commands,


0. google/assistance/x - Open Google.

1. github/git/coding - Open GitHub.

2. heroku - Open Heroku website.

3. youtube/yt/online videos - Open YouTube.

4. pip install - Install a python module.

5. prompt/cmd - Open Command Prompt.

6. shutdown/turn off - Shutdown device with different functions.

7. musics/audio - Play Musics saved in directory of 'music_dir'.

8. videos/vids/video - Play Videos saved in directory of 'video_dir'.

9. photos/pics/photographs/images - Open photographs saved in directory of 'pics_dir'.

10. goodbye/bye/tata - End the Program.

11. Random command - Gives you result at Google.

12. date/time - date or time respectively.

13. insta/instagram - Open Instagram.

14. fb/facebook/meta - Open Facebook/Meta.

15. tweet/twitter - Open Twitter.

16. path/directory - Opens given path/directory.

17. hidden - Open help related to hidden files.

18. chat - chat with me...I use Itel Ai for Chatbot.
           visit - https://pypi.project.org/kukiapipy

19.  Wanna know about:
       > my developer?, send 'who made you'.
       > myself?, send 'wabout you'.
'''
        print(f'{ainame}:\n'+help_section)
        talk(f"Hey {NAME} I'm {ainame}, I can help you with these commands")

    elif "google" in command or 'assistance' in command :
        ans='Opening Google...'
        print(f'{ainame}:\n'+ans)
        talk(ans)
        webbrowser.open("https://www.google.com")

    elif "insta" in command or 'instagram' in command or 'ig' in command :
        ans = 'Opening Instagram...'
        print(f'{ainame}:\n'+ans)
        talk(ans)
        webbrowser.open("https://www.instagram.com")

    elif 'joke' in command :
        a = pyjokes.get_joke(language='en', category='all')
        #pyjokes.get_jokes
        print(a)
        talk(a)

    elif 'fb' in command or 'facebook' in command or 'meta' in command :
        ans = 'Opening Meta/Facebook...'
        print(f'{ainame}:\n'+ans)
        talk(ans)
        webbrowser.open("https://www.facebook.com")

    elif 'tweet' in command or 'twitter' in command:
        ans = 'Opening Twitter...'
        print(f'{ainame}:\n'+ans)
        talk(ans)
        webbrowser.open("https://www.twitter.com")
    
    elif "github" in command or 'git' in command or 'coding' in command :
        ans = 'Opening Github...'
        print(f'{ainame}:\n'+ans)
        talk(ans)
        webbrowser.open("https://www.github.com")
    
    elif 'youtube' in command or 'yt' in command or 'online videos' in command :
        ans = 'Opening YouTube...'
        print(f'{ainame}:\n'+ans)
        talk(ans)
        webbrowser.open("https://www.youtube.com")

    elif 'time' in command :
        ans = f" Time is {datetime.now().strftime('%I : %M %p')}"
        print(f'{ainame}:\n🕒'+ans)
        talk(ans)

    elif 'date' in command :
        ans = f' Date is {date_fmt}'
        print(f'{ainame}:\n🔅'+ans)
        talk(ans)

    elif 'echo' in command :
        echo=input(f'{ainame}:\nWhat I have to say?\n ⪼  ')
        talk(echo)

    elif "pip install" in command :
        mod=input(f"{ainame}:\nEnter python module name that you wanna install : ")
        talk("Enter python module name that you wanna install : ")
        os.system("pip install {}".format(mod))
    
    elif "prompt" in command or 'cmd' in command :
        prompt_cmd=input(f"{ainame}:\n▷ Enter prompt command : ")
        talk("Enter prompt command : ")
        if prompt_cmd == "shutdown":
            print(f"{ainame}: You should enter `shutdown` directly")
            talk("You should enter `shutdown` directly")
        else:
            print(f"{ainame}: '"+prompt_cmd+"' command executed")
            talk("'"+prompt_cmd+"' command executed")
            os.system(prompt_cmd)
        
    elif "shutdown" in command or 'turn off' in command :
        print(f"{ainame}:\nPlease choose which type of Shutdown you want :-"
          "\n⪼  Shutdown",
          "\n.......................................................... : s"
          "\n⪼  Restart",
          "\n.......................................................... : r"
          "\n⪼  Log off",
          "\n.......................................................... : l"
          "\n⪼  Restart after Reboot",
          "\n.......................................................... : g"
         "\n⪼   Shutdown without any warning",
          "\n.......................................................... : p"
         "\n⪼  Sleep / Hibernate",
          "\n.......................................................... : h"
          "\n\nYou can Abort shutdown once if you selected 'No'.")
        talk("Please choose which type of Shutdown you want.")
        sdc = input("Enter the symbol : ")
        # sdc.lower()
        if sdc in ['s','r','l','g','p','h']:
            confirmation_text = f"""{ainame}:\nConfirmation
            ⭕ Shutdown Process : SD CODE ACCEPTED
            ✅ Shutting down system with `shutdown -{sdc}` command.
            
            ⚠ Please confirm by entering:
            'Yes' : I want to shutdown.
            'No'  : I don't want to shutdown or maybe I had mistaken."""
            print(confirmation_text)
            confirmation_text = confirmation_text.replace('⭕','')
            confirmation_text = confirmation_text.replace('✅','')
            confirmation_text = confirmation_text.replace('⚠','')
            confirmation_text = confirmation_text.replace(f'{ainame}','')
            talk(confirmation_text)
            confirm_s = input(f"{ainame}:\n▷ Enter : ")
            talk("\nEnter !")
            if confirm_s == "Yes":
                ans=f"Attempting Shutdown by {ainame} AI {__version__}"
                print(f'{ainame}:\n'+ans)
                talk(ans)
                os.system(f'shutdown -{sdc}')
            elif confirm_s == "No":
                ans = 'OK! Aborted Shutdown, please be sure next time'
                print(f'{ainame}:\n'+ans+' 😅')
                talk(ans)
                # os.startfile(f"python -u "+anon_path+"")
            else:
                ans = '❌ Wrong choice\n✔ Please Enter \'Yes\' or \'No\''
                print(f'{ainame}:\n'+ans)
                ans=ans.replace('❌', '')
                ans=ans.replace('✔', '')
                talk(ans)
        else:
            ans=f'⭕ Shutdown Process : SD CODE NOT ACCEPTED\nI\'m sorry, \'{sdc}\' code of shutdown isn\'t correct or it\'s not in my database.'
            print(f'{ainame}:\n'+ans)
            ans=ans.replace('⭕', '')
            talk(ans)

    elif "what\'s up" in command or 'how are you' in command :
        stMsgs = ['Just doing my thing!, How are you?', 'I am fine!, How\'s you?', 'it\s all Nice!, How are you?', 'I am nice and full of energy, How are you?','i am okey! How are you?']
        ans_q = random.choice(stMsgs)
        print(f'{ainame}:\n' + ans_q)
        talk(ans_q)
        ans_take_from_user_how_are_you = input()
        if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'ok' in ans_take_from_user_how_are_you:
            ans = 'okey... Any command for me?'
            print(f'{ainame}:\n' + ans)
            talk(ans)
        elif 'idk' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
            ans = 'oh I\'m sorry...'
            print(f'{ainame}:\n' + ans)
            talk(ans)

    elif 'make you' in command or 'made you' in command or 'created you' in command or 'developed you' in command :
        ans = """
        ⊛For your information,
        I was developed by @itzzzyashu.
        Lots of Thanks to Him.
        
        you can contact him by
        Instagram - @itzzzyashu
        Telegram - @itzzzyashu
        Gmail - itzzzyashu@gmail.com
        
        He's most active on Github, Telegram ( @itzzzzyashu, @itzzzyashu respectively ).
        I'm an AI python program for basic lifestyles made by
        https://telegram.me/SanatanRakshaNetwork.
        that's all I knew about my sexy developer.
        
"""
        print(f'{ainame}:\n' + ans)
        talk(ans)

    elif "who are you" in command or "about you" in command or "your details" in command :
        ans = f'''
        I am {ainame} an Ai based python program,
        I'm running on version {__version__}.
        And I can help you lot like your smart assistant !
        send "help" to know about my commands !
        like playing music or video from your directory (edit your config.py first.)
        I can also play video and song from web or online !
        I can also entertain you...
        I think you've Understood basics about me.
        ohk Lets Start(send 'help' or a command.)...'''
        print(f'{ainame}:\n' + ans)
        talk(ans)

    elif 'goodbye' in command or 'bye' in command or 'tata' in command :
        stMsgs = ['byeee cutie!',
              "Goodbye {}! ".format(NAME),
              "Ok {}! we'll talk later.. ".format(NAME),
              "it's Nice to meet you {}! ".format(NAME),
              "Have a Good day {}! ".format(NAME)]
        ans_bye = random.choice(stMsgs)
        print(f'{ainame}:\n' + ans_bye)
        talk(ans_bye)
        time.sleep(4)
        exit()

    elif 'hidden' in command or 'secret' in xsearch :
        os.startfile(hidden_dir)
        ans = f'''{ainame}:\nEnter any keyword that is in `xsearch` keywords in `config.py` file.
              This will open your directory that is saved in `hidden_dir`
              Example enter `movu` if it is in `xsearch` keyword collection!'''
        print(f'{ainame}:\n😁' + ans)
        talk(ans)

    elif 'hello' in command or 'hi' in command or 'hii' in command or 'hola' in command or 'halo' in command :
        hello_Msgs = ['Hii cutie!',
              "Umm I was thinking about you.. {}! ".format(NAME),
              "Hii {}".format(NAME),
              "Hey {}! Any command for me? ".format(NAME),
              "it's Nice to meet you {}! ".format(NAME),
              "So {}, tell me what I've to do now!".format(NAME)]
        ans = random.choice(hello_Msgs)
        print(f'{ainame}:\n' + ans)
        talk(ans)
    
    elif 'photo' in command or 'photograph' in command or 'images' in command or 'pics' in command :
        ans = 'opening pictures...'
        print(f'{ainame}:\n' + ans)
        talk(ans)
        pics = os.listdir(pics_dir)
        os.startfile(os.path.join(pics_dir, pics[10]))

    elif 'music' in command or 'audio' in command or 'song' in command :
        ans = 'ok i am playing music...'
        print(f'{ainame}:\n' + ans)
        talk(ans)
        musics = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, musics[0]))

    elif 'file' in command or 'dir' in command :
        path_i=input(r'Enter directory path : ')
        ans = 'finding given path...'
        print(f'{ainame}:\n' + ans)
        talk(ans)
        time.sleep(2)
        os.startfile(path_i)

    elif 'restart' in command:
        ans = 'Restarting...'
        print(f'{ainame}:\n' + ans)
        talk(ans)
        time.sleep(1)
        os.system('python -u '+anon_path)
    
    elif 'vids' in command or 'video' in command :
        ans = 'ok i am playing videos...'
        print(f'{ainame}:\n' + ans)
        talk(ans)
        videos = os.listdir(video_dir)
        os.startfile(os.path.join(video_dir, videos[0]))

    elif command in xsearch :
        ans = 'ok playing hidden media! xD'
        print(f'{ainame}:\n' + ans)
        talk(ans)
        hidden = os.listdir(hidden_dir)
        os.startfile(os.path.join(hidden_dir,hidden[0]))

    elif 'face' in command:
        fc='face recognition '
        print(f'{ainame}:\n' + fc + 'started !')
        talk(fc + 'started !')
        # face recognition code.
        print(f'{ainame}:\n' + fc + 'ended !')
        talk(fc + 'ended !')
        
    elif 'chat' in command:
        if ConnectionError:
            ans = f'{ainame}:\n404: please check your internet connection.\nI can only chat with you if You\'re system is connected to the Internet.\nTry Reconnecting or using Ethernet.'
            print(f'{ainame}:\n' + ans)
            ans = ans.replace('404','')
            talk(ans)
        else:
            print(f'{ainame}:\nAI Chatbot: Active')
            msg = input(f'{ainame}:\nHello What\'s up?\n ')
            talk('Hello What\'s up?')
            if 'bye' in msg :
                pass
            else:
                for i in range(1,1000):
                    # https://www.kukiapi.xyz/api/apikey=Xxxx/bot/owner/message=
                    Kuki = requests.get(f"https://kukiapi.xyz/api/apikey={AIAPI}/{ainame}/itzzzyashu/message="+msg)
                    kuki_reply = f"{Kuki['reply']}"
                    print(f'{ainame}:\n' + kuki_reply)
                    talk(kuki_reply)
    else:
        err=f'''Sorry {NAME}, I'm still learning and I don't have any correct answer for your query.....
Just press ENTER if you want me to search `{command}` on browser;\nEnter anything to skip searching on browser.
'''
        print(f'{ainame}:\n😓' + err)
        talk(err)
        ggl_it=input()
        if ggl_it == '':
            if ConnectionError:
                ice = 'Please check your internet connection.'
                print(f'{ainame}:\n' + ice)
                talk(ice)
            else:
                webs = f"Pushing your search to Web browser\nShowing you the results for `{command}`."
                print(f"{ainame}:\n" + webs)
                talk(webs)
                search = command.replace(' ', '+')
                webbrowser.open('https://www.google.com/search?q=' + search)


while True:
    run_anon()

# Anon Update 4.0.1
