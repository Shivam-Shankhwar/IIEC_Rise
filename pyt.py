import os

dont_run = ['dont', 'do not', 'donot', 'don\'t', 'not']

print('Good Morning/Evening, what would you like me to do sir ?')
print('1. Notepad ')
print('2. Paint')
print('3. Cmd')
print('4. Calculator')
print('5. Exit\n')

while True:
    print('Tell me your requirement : ', end = '')
    p = input()
    
    if(('notepad' in p) or ('Notepad' in p)) and not(any(i in p.split() for i in dont_run)):
        os.system('notepad')
        print('Excellent, tell me more to do ...\n')
     
    elif(('paint' in p) or ('Paint' in p)) and not(any(i in p.split() for i in dont_run)):
        os.system('mspaint')
        print('Cool, tell me more ...\n') 
    
    elif(('calculator' in p) or ('Calculator' in p)) and not(any(i in p.split() for i in dont_run)):
        os.system('calc')
        print('Done, want more ...\n')
        
    elif(('cmd' in p) or ('Cmd' in p)) and not(any(i in p.split() for i in dont_run)):
        os.system('cmd')
        print('Excellent, tell me more to do ...\n')
    
    elif('Exit' in p) or ('exit' in p):
        print('')
        break
        
    else:
        print('\nSorry, can\'t do it !')
        break
print('So Long, good day.')        
    


