
import random

def gameplay(word,r):
        global gressed
        global total
        global missed
        msg=''
        miss=1
        score=26-r
        if score<0:
            score=0
        status=False
        gress=input('Enter your alphabet:')
        while len(gress)>1:
            gress=input('Enter only 1 alphabet:')
        gress=gress.upper()
        if not gress in gressed:
            gressed=gressed+gress   
            for w in word:
                if w.isalpha():
                    if w in gressed:
                        msg=msg+w
                        if gress==w:
                            total=total+score
                            miss=0      
                    else :
                        msg=msg+"_"
                else:
                    msg=msg+w
            missed=miss+missed
            if msg==word:
                status=True
            temp=''
            for x in msg:
                temp=temp+x+' '
            print(temp,'score ', total,'remaining wrong guess ',missed,'guessed:',gressed)
        return status
            
def read_file(filename):
    try:
        file_obiect=str(open(filename,'r').read())
    except FileNotFoundError:
        print("File not found")
        exit()
    else :
        f=file_obiect.splitlines()
        return f
def select_word():
    global word_list
    i=random.randint(0,len(word_list)-1)
    x=word_list[i]
    word_list.remove(word_list[i])
    return x

# main programe
missed=0
life=True
No=''
choice=[]
select=''
total=0
while life:
    gressed=''
    gress=False
    r=0
    category=read_file('category.txt')
    # select category
    for c in range(len(category)):
        print('press ',category[c])
        No=No+(category[c].split(' ')[0])
        choice.append(category[c].split(' ')[1])
    select=input('select :')
    while not select in No:
        select=input('select :')
    # read file
    word_list=read_file(choice[int(select)-1]+'.txt')
    x=select_word().split(' ')
    missed=0
    print('hint:',x[2])
    score=25
    # start game
    while not gress:
        r=r+1
        gress=gameplay(x[1].upper() ,r)
        if missed>=10:
            life=False
            gress=True
            print(x[1])
    # play continus
    if life:
        con=input('play(y/n)')
        if con!='y':
            gress=True
            life=False
