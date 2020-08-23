#Modules needed
import os
import pyttsx3
import subprocess

#pyttsx3 Engine Setup
engine = pyttsx3.init()
engine.setProperty('rate', 130)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
    
#All the Declarables    
dont_run = ['dont', 'no need', 'noneed', 'donot', 'don\'t', 'not',  'No Need', 'No need', 'no Need', 'do not']

#Options for users
print('Hello, what would you like me to do sir ?')
engine.say('Hello, what would you like me to do sir ?')
engine.runAndWait()
print('- Notepad ')
print('- Paint')
print('- Cmd')
print('- Calculator')
print('- Google')
print('- Vlc')
print('- Exit\n')

#Main driving code
while True:
    print('Tell me your requirement : ', end = '')
    engine.say('Tell me your requirements')
    engine.runAndWait()
    p = input()
    
    if(('notepad' in p) or ('Notepad' in p)) and not(any(i in p.split() for i in dont_run)):
        os.system('notepad')
        print('I see, something important to write...\n')
        engine.say('I see, you have something important to write')
        engine.runAndWait()
     
    elif(('paint' in p) or ('Paint' in p)) and not(any(i in p.split() for i in dont_run)):
        os.system('mspaint')
        print('Unleash your imagination ...\n') 
        engine.say('Unleash your imagination')
        engine.runAndWait()
    
    elif(('calculator' in p) or ('Calculator' in p)) and not(any(i in p.split() for i in dont_run)):
        os.system('calc')
        print('Done, want more ...\n')
        engine.say('Done, want more')
        engine.runAndWait()
        
    elif(('cmd' in p) or ('Cmd' in p)) and not(any(i in p.split() for i in dont_run)):
        os.system('cmd')
        print('Excellent, tell me more to do ...\n')
        engine.say('Excellent, tell me more to do')
        engine.runAndWait()
    
    elif(('Google' in p) or ('google' in p)) and not(any(i in p.split() for i in dont_run)):
        subprocess.Popen([r'C:\Program Files\Internet Explorer\\iexplore.exe', 'www.google.co.in'])
        print('Want something to search ...\n')
        engine.say('Done searching !')
        engine.runAndWait()
        
    elif(('vlc' in p) or ('Vlc' in p)) and not(any(i in p.split() for i in dont_run)):
        subprocess.call([r'C:\Program Files\VideoLAN\VLC\\vlc.exe'])
        print('which movie are you gonna watch ...\n')
        engine.say('Which movie are you gonna watch')
        engine.runAndWait()
        
    elif('Exit' in p) or ('exit' in p):
        print('')
        break
    
    elif(any(i in p.split() for i in dont_run)):
        print('')
        break
        
    else:
        print('\nSorry, can\'t do it !')
        engine.say('Sorry, can\'t do it')
        engine.runAndWait()
        break
    
#GoodBye !    
print('----So Long, see you soon.----')   
engine.say('So Long, see you soon')
engine.runAndWait()



