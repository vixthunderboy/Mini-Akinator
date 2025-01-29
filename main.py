# 1) f, 2) m
# 1) alive, 2) dead
# 1) non fic, 2) fic
# 1) american, 2) brit, 3) indian, 4) portuguese
# 1) white 2) black 3) Latino 4)East-asian 5)south-asian
# 1) music, 2) sports, 3) tech, 4) acting 5)Entertainer 6)Politician
# music: 1) rap, 2) pop, 3) metal, 4) edm 5)rock
# sports: 1) football, 2) cricket, 3) basketball, 4) mma 5)f1
# tech: 1) social media, 2) automobile, 3) consumer elec
# football: 1) premier league, 2) la liga, 3) ligue 1
# premier league: 1) tottenham hotspur, 2) man utd, 3) arsenal...
# la liga: 1) barca, 2) real
# ligue 1: 1) psg, 2) monaco
#Entertainer: 1)Talk Show Host 2) Model
#acting: 1) Oscar 2)no oscar
#Politician 1)President 2) Other
#President 1) Democratic 2)Republican



chardict = {
    "Mike Pence" : 2111162,
    "Sonia Gandhi" : 11131,
    "Deepika Padukone" : 11135,
    "Kanye West" : 2111211,
    "Steve Jobs" : 221113,
    "Elon Musk" : 211113,
    "Cristiano Ronaldo" : 2114,
    "Oprah Winfrey" : 111125,
    "Kim Kardashian" : 111115,
    "Marilyn Monroe" : 121114,
    "Tom Hanks" : 2111141,
    "Elvis Presley" : 2211115,
    "Jimi Hendrix": 2211215,
    "Johnny Depp" : 2111142,
    "Nicki Minaj" : 1111211,
    "Beyonce" : 1111212,
    "Taylor Swift": 1111112,
    "Abraham Lincoln" : 22111612,
    "John F. Kennedy" : 22111611,
    "Will Smith" : 2111241,
    "David Beckham" : 211212,    
    "Donald Trump" : 21111612,
    "Angelina Jolie" : 111114,
    "Dwayne Johnson" : 2111242,
    "Michael Jackson" : 2211112,
    "Audrey Hepburn" : 121214,
    "Emily Blunt" : 111214,
    "Vasco De Gama" : 2214,
    "Harry Potter" : 2122,
    "Dumbledore" : 2222,
    "Captain America" : 2121,
    "Iron Man" : 2221
    }

found = 0

charnum=int(input("Is this person female? 1 for yes, 2 for no: "))

charnum = charnum*10 + int(input("Is this person alive? 1 for yes, 2 for no: "))

charnum = charnum*10 + int(input("Is this person real (not a fictional character? 1 for yes, 2 for no: "))

def nationality():
    n=1
    x = int (input("Is this person American? 1 for yes, 2 or any other key for no: "))
    if x==1:
        return n
    else:
        n=n+1
        x = int (input("Is this person British? 1 for yes, 2 or any other key for no: "))
        if x==1:
            return n
        else:
            n=n+1
            x=int(input("Is this person Indian? 1 for yes, 2 or any other key for no: "))
            if x==1:
                return n
            else:
                n=n+1
                x=int(input("Is this person Portuguese? 1 for yes, 2 or any other key for no: "))
                if x==1:
                    return n
                else: 
                    print("Sorry this person is not in our database :(")
                    n=0
                    found=2
                
n = nationality()

charnum = charnum*10 + n
    
if charnum in chardict.values():
    found = 1
    
if found == 1:
    personality = (list(chardict.keys())[list(chardict.values()).index(charnum)])
    print("Were you thinking of "+personality+"?")
    quit()

def race():
    n=1
    x = int (input("Is this person White? 1 for yes, 2 or any other key for no: "))
    if x==1:
        return n
    else:
        n=n+1
        x = int (input("Is this person Black? 1 for yes, 2 or any other key for no: "))
        if x==1:
            return n
        else:
            n=n+1
            x=int(input("Is this person Latino? 1 for yes, 2 or any other key for no: "))
            if x==1:
                return n
            else:
                n=n+1
                x=int(input("Is this person's race East Asian? 1 for yes, 2 or any other key for no: "))
                if x==1:
                    return n
                else: 
                    n=n+1
                    x=int(input("Is this person's race South Asian? 1 for yes, 2 or any other key for no: "))
                    if x==1:
                        return n
                    else:
                        print("Sorry this person is not in our database :(")
                        n=0
                        found=2
                        

if found==0:
    n = race()
    charnum = charnum*10 + n
    
valid = 0    

if charnum in chardict.values():
    found = 1
    
if found == 1:
    personality = (list(chardict.keys())[list(chardict.values()).index(charnum)])
    print("Were you thinking of "+personality+"?")
    quit()
    
def industry():
    n=1
    x = int (input("Is this person in the music industry? 1 for yes, 2 or any other key for no: "))
    if x==1:
        return n
    else:
        n=n+1
        x = int (input("Is this a sportsperson? 1 for yes, 2 or any other key for no: "))
        if x==1:
            return n
        else:
            n=n+1
            x=int(input("Is this person in the tech industry? 1 for yes, 2 or any other key for no: "))
            if x==1:
                return n
            else:
                n=n+1
                x=int(input("Does this person act? 1 for yes, 2 or any other key for no: "))
                if x==1:
                    return n
                else: 
                    n=n+1
                    x=int(input("Is this person an entertainer? 1 for yes, 2 or any other key for no: "))
                    if x==1:
                        return n
                    else:
                        n=n+1
                        x=int(input("Is this person a politician? 1 for yes, 2 or any other key for no: "))
                        if x==1:
                            return n
                        else:
                            print("Sorry this person is not in our database :(")
                            n=0
                            found=2


if found==0:
    ind = industry()
    charnum = charnum*10 + ind
    
if ind==2:
    found=1
    
if charnum in chardict.values():
    found = 1

if found==1:
    personality = (list(chardict.keys())[list(chardict.values()).index(charnum)])
    print("Were you thinking of "+personality+"?")
    quit()
    
def music():
    n=1
    x = int (input("Is this person a rapper? 1 for yes, 2 or any other key for no: "))
    if x==1:
        return n
    else:
        n=n+1
        x = int (input("Is this person a popstar? 1 for yes, 2 or any other key for no: "))
        if x==1:
            return n
        else:
            n=n+1
            x=int(input("Is this person a metal artist? 1 for yes, 2 or any other key for no: "))
            if x==1:
                return n
            else:
                n=n+1
                x=int(input("Is this person an EDM artist? 1 for yes, 2 or any other key for no: "))
                if x==1:
                    return n
                else: 
                    n=n+1
                    x=int(input("Is this person a rockstar? 1 for yes, 2 or any other key for no: "))
                    if x==1:
                        return n
                    else:
                        print("Sorry this person is not in our database :(")
                        return 0
    


if ind==1:
    n=music()
    charnum = charnum*10 + n
    if n!=0:
        found=1
        
        
if ind==4:
    n=int(input("Has this person won an Oscar? 1 for yes, 2 for no: "))
    charnum = charnum*10 + n
    if n==1 or n==2:
        found=1
        

 
if charnum in chardict.values():
    found = 1 
 
if found==1:
    personality = (list(chardict.keys())[list(chardict.values()).index(charnum)])
    print("Were you thinking of "+personality+"?")
    quit()
        

if ind==6:
    n=int(input("Was this person ever president? 1 for yes, 2 for no: "))
    charnum = charnum*10 + n
    if n==1:
        found = 1
        charnum = charnum*10 + int(input("Was this person elected as part of the Democratic Party? 1 for yes, 2 for no: "))
    if n==2:
        found = 1
        
 
if found==0:
    print("Sorry, this person is not in our database :(")
    quit()
    
if charnum in chardict.values():
    found = 1
    

 
if found==1:
    personality = (list(chardict.keys())[list(chardict.values()).index(charnum)])
    print("Were you thinking of "+personality+"?")


#print(charnum)








