import random
import time
import csv


#----------------Executions---------------------------





puna ="\nIt was a long and laborious trial, but eventually {0} was found guilty!\nExecution: Wringing the Turkey\n\n{0} was hung with barbed wire by the throat. Monokuma spun the barbed wire until their head was decapitated.\n\nEnd of punishment."
punb ="\nThe class voted at the end of a difficult trial and successfully found the killer, aka {0}!\nExecution: Swimming With the Wild\n\n{0} was thrown into a pool. They started swimming for the surface when they were overcome with a hoard of hungry piranhas!\n\nEnd of punishment."
punc ="\nThe killer, who was successfully voted in the trial, was {0}.\nExecution: Toss of Luck\n\n{0} had 10 throwing knives thrown at them, piercing them. But they managed to break free! Fortunately, on their escape, an ambulance struck them, killing them instantly.\n\nEnd of punishment."
pund ="\n{0} was found guilty! They were strapped to an electric chair and was slowly electrocuted, however moments before death the generator exploded, leaving {0} to bleed to death, strapped to a chair with shards of metal stabbing them.\n\nEnd of punishment."
pune ="\nThe killer, {0} was voted correctly! They screamed as they were dragged towards their punishment.\nExecution: Race to the Finish Line\n\nWhen {0} heard the gun, they ran towards the finishing line. Reach it, and they'd be able to leave Hope's Peak. Unfortunately, they turned to see hundreds of over-sized, feral Monokumas running towards them. They were trampled to death.\n\nEnd of punishment."
punf ="\nThe class voted in silence for {0} and weren't surprised when they were correct.\nExecution: The Newest Monokuma\n\n{0} was shoved into a Monokuma costume. All was silent until blood started dripping out. When the costume opened, all the students could see was {0}'s body pierced with thousands of needles and burnt from acid.\n\nEnd of punishment."
pung ="\n...And the killer, who was voted correctly, was {0}!.\nExecution: You Spin Me Right Round, Baby\n\nFor punishment {0} was put into a contraption that slowly rotated their head until it broke off.\n\nEnd of punishment."
punh ="\nThe killer, who had already fallen into intense despair, was {0}.\nExecution: Ye Olde Health\n\nFor punishment, {0} had heart surgery performed on them with no extra blood, no anaesthetic and no clean equiptment. They died from blood loss.\n\nEnd of punishment. "
puni ="\nThe class voted in sync for the killer. They were correct, the killer was {0}.\nExecution: Burn, Baby, Burn!\n\n{0} was dancing at a fire festival when Monokumas in the crowd got rowdy, throwing alcohol around. A drunk one pushed {0} into the flames and they burnt to death.\n\nEnd of punishment."
punj = "\n`I did it,` admitted {0} in complete despair. ``I killed them``. That was all the class needed to vote for {0}.\nExecution: Aquarium Admirers\n\n{0} was locked in a glass barrel full of water. They drowned slowly.\n\nEnd of punishment."
punk = "\n{0}, the very defensive murderer, was voted guilty.\nExecution: {0} was placed in a random room with nothing to do. They were quite bored until they noticed that slowly two walls were getting closer and closer. They were crushed between the walls.\n\nEnd of punishment."
punl = "\n{0}, the killer, wouldn't stop laughing at their crimes. The students voted them in disgust.\nExecution: {0}rib.\n\n{0} was sprawled out on a bed and tied down when Monokuma hovered above them with medical appliances and began to cut into them. Monokuma plucked out {0}'s ribs, puncturing the aorta. {0} haemorrhaged to death.\n\nEnd of punishment."
punm = "\nWith heavy hearts, the class voted for {0}, knowing they'd killed by accident.\nExecution: One Final Sport\n\n{0} was lifted into a plane which hovered and flew over Japan. `I can see the world from here!` Exclaimed {0}. They were still smiling when they were pushed from the plane without a parachute.\n\nEnd of punishment."
punn ="\nThe class happily voted for {0}, the psychopath who'd killed their friend. They wanted to watch them suffer.\nExecution: Can You Beat The Heat?\n\n{0} was elevated and dropped into a pot. They sat there while it heated and they melted. {0} gave the class one last cruel smile.\n\nEnd of punishment."

punish = [puna,punb,punc,pund,pune,punf,pung,punh,puni,punj,punk,punl,punm,punn]




#---------------Motives--------------------------------



mot1 = "The motive chosen was no sleep until a murder. Any student who dared to sleep would be punished by hanging."
mot2 = "The motive chosen was everyone has a student they are not allowed to lose sight of, with no exceptions. Once a murder occurred, students could be with whoever they want."
mot3 ="The motive chosen was removal of one item important to each person until someone died."
mot4 ="The motive chosen was everyone had a virus that could only be cured by a murder. It will result in death in 24 hours."
mot5 ="The motive was that an Ultimate Assassin was said to be amongst the group and if nobody killed in 24 hours, the assassin would, leaving no evidence."
mot6 ="The motive selected was a Russian Roulette game; for every hour that no one died, a random student's relative was tortured to death and all students forced to watch."
mot7 ="The motive was that if someone gets away with murder they are able to make a call infront of the class, if they refuse to let the class listen they forfeit the call."
mot8 ="The motive was every hour the temprature will drop by 5 degrees until everyone freezes, unless someone dies."
mot9 ="The motive selected was each student has a target however they do not know who their target is. If they manage to kill the target they leave without trial."
mot10 ="The motive selected was that dead memes will blast through the monitors until someone dies."
mot11 ="The motive was no food until a murder occurred."
mot12 ="The motive was everyone is forced to wear a Monokuma wristband. Every hour it would shock students getting stronger and stronger until someone dies or it begins to stop students' hearts."
mot13 ="The motive was everyone lost a random sense until someone died."
mot14 ="The motive was every day that nobody died, a random student would be punished."
mot15 ="The motive was that each student was told things about another student to make them hate eachother."
mot16 ="The motive was students recive a skill or item that another student wants and are told about someone who recived a skill or item that they want."
mot17 ="The motive was everyone recives someone else's secret but they do not know who it belongs to. If no one died in 24 hours, students are told whos secret they recived and have to choose between telling everyone or reciving punishment."
mot18 ="The motive was every hour, water would flood the school increasing the water level by an inch until everyone drowned or someone was murdered."
mot19 ="The motive was if no one died in 24 hours, all students must face their worst fear. If the student has no fears they recive punishment."


motlist = [mot1,mot2,mot3,mot4,mot5,mot6,mot7,mot8,mot9,mot10,mot11,mot12,mot13,mot14,mot15,mot16,mot17,mot18,mot19]



#------------------Random Names----------------------------




name = ['Kazuichi','Akari','Akane','Byakuya','Mukuro','Chiaki','Hama','Hiroshi','Saburo','Sachi','Namiko','Etsuko','Denji','Emiko','Ginjiro','Jiro','Hanae','Junko','Kaede','Kaito','Kaida','Kioko','Makiko','Makaira','Michi','Miu','Nao','Rikuto','Royoko','Sada','Sayaka','Taemon','Taka','Taro','Yumi','Cherry','Sakura','Kokoro','Xing-Ji']
namel = 39

ult = ['Tailor','Mechanic','Genetics Researcher','Footballer','Childrens Author','Actor','Puzzle Solver','Vocalist','Pop Idol','Wrestler','Spy','Sniper','Detective','Army Sergeant','Gamer','Programmer','Charleston Dancer','Tap Dancer','Unlucky Student','Lucky Student','Doctor','Trainer','Breeder','Instructor','Swimmer','Spraypaint Artist','Speedcuber','Activist','Sculptor','Collector','Biologist', 'Voice Actor','Logo Designer','Handcrafter','Translator','Portrait Artist','Landscaper','Poisoner','Graffiti Artist','Abstract Artist','Theorist','Doctor','Dentist','Photo Editor','Athlete','Dreamer']

ultl = 46










#-------------------SIM START---------------------













print("DANGANRONPA SIMULATOR - UPDATED 04/01/21")
print("Welcome to this Danganronpa Simulator!\nHope's Peak Academy greets you with open arms!\nBut first, lets get to know a bit about your cast.\n \n \n")
pre = input("Do you want to use randomly generated names or custom?\nPress R for random names, P for preset names or C to create a custom cast\n\n>")
if pre in ["p","P",]:
        drvo = input("What danganronpa do you want to use, 1 for Trigger Happy Havoc, 2 for Goodbye Despair, 3 for Killing Harmony\n\n>")
        if drvo == '1':
                a = 'Makoto Naegi'
                ab ='Lucky Student'
                b = 'Sayaka Maizono'
                bb = 'Pop Idol'
                c = 'Leon Kuwata'
                cb ='Baseballer'
                d ='Chihiro Fujisaki'
                db ='Programmer'
                e='Mondo Owada'
                eb='Biker'
                f='Kiyotaka Ishimaru'
                fb='Hall Monitor'
                g='Hifumi Yamada'
                gb='Fanfic Creator'
                h='Celestia Ludenberg'
                hb='Gambler'
                i='Sakura Ogami'
                ib='Martial Artist'
                j='Mukuro Ikusaba'
                jb='Soldier'
                k='Kyoko Kirigiri'
                kb='Detective'
                l='Byakuya Togami'
                lb='Affluent Prodigy'
                m='Aoi Asahina'
                mb='Swimmer'
                n='Toko Fukawa'
                nb='Literary All Star'
                o ='Junko Enoshima'
                ob ='Fashionista'
                p ='Yasuhiro Hagakure'
                pb ='Fortune Teller'
        elif drvo == '2':
                a = 'Hajime Hinata'
                ab ='Reserve Course Student'
                b = 'Byakuya Togami'
                bb = 'Affluent Prodigy'
                c = 'Teruteru Hanamura'
                cb ='Chef'
                d ='Mahiru Koizumi'
                db ='Photographer'
                e='Peko Pekoyama'
                eb='Swordswoman'
                f='Ibuki Mioda'
                fb='Singer'
                g='Hiyoko Saionji'
                gb='Dancer'
                h='Mikan Tsumiki'
                hb='Nurse'
                i='Nekomaru Nidai'
                ib='Team manager'
                j='Gundham Tanaka'
                jb='Breeder'
                k='Nagito Komaeda'
                kb='Lucky Student'
                l='Chiaki Nanami'
                lb='Gamer'
                m='Akane Owari'
                mb='Gymnast'
                n='Fuyihiko Kuzuryu'
                nb='Yakuza'
                o ='Kazuichi Soda'
                ob ='Mechanic'
                p ='Sonia Nevermind'
                pb ='Princess'
        elif drvo == '3' :
                a = 'Shuichi Saihara'
                ab ='Detective'
                b = 'Rantaro Amami'
                bb = 'Survivor'
                c = 'Kaede Akamatsu'
                cb ='Pianist'
                d ='Ryoma Hoshi'
                db ='Tennis Pro'
                e='Kirumi Tojo'
                eb='Maid'
                f='Angie Yonaga'
                fb='Artist'
                g='Tenko Chabashia'
                gb='Neo-Akido Master'
                h='Korekiyo Shinguji'
                hb='Anthropologist'
                i='Miu Iruma'
                ib='Inventor'
                j='Gonta Gokuhara'
                jb='Entomologist'
                k='Kokichi Oma'
                kb='Supreme leader'
                l='Kaito Momota'
                lb='Astronaut'
                m='Tsumugi Shirogane'
                mb='Cosplayer'
                n='K11B0'
                nb='Robot'
                o ='Maki Harukawa'
                ob ='Assasin'
                p ='Himiko Yumeno'
                pb ='Magician'
elif pre in ['R','r']:
        na = random.randint(1,35)
        a = name[na-1]
        del name [na-1]
        ul = random.randint(1,29)
        ab =ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,34)
        b =name[na-1]
        del name [na-1]
        ul = random.randint(1,28)
        bb =ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,33)
        c=name[na-1]
        del name [na-1]
        ul = random.randint(1,27)
        cb=ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,32)
        d=name[na-1]
        del name [na-1]
        ul = random.randint(1,26)
        db=ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,31)
        e=name[na-1]
        del name [na-1]
        ul = random.randint(1,25)
        eb=ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,30)
        f=name[na-1]
        del name [na-1]
        ul = random.randint(1,24)
        fb = ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,29)
        g=name[na-1]
        del name [na-1]
        ul = random.randint(1,23)
        gb=ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,28)
        h=name[na-1]
        del name [na-1]
        ul = random.randint(1,22)
        hb=ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,27)
        i=name[na-1]
        del name [na-1]
        ul = random.randint(1,21)
        ib=ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,26)
        j=name[na-1]
        del name [na-1]
        ul = random.randint(1,20)
        jb=ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,25)
        k=name[na-1]
        del name [na-1]
        ul = random.randint(1,19)
        kb=ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,24)
        l=name[na-1]
        del name [na-1]
        ul = random.randint(1,18)
        lb=ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,23)
        m=name[na-1]
        del name [na-1]
        ul = random.randint(1,17)
        mb=ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,22)
        n=name[na-1]
        del name [na-1]
        ul = random.randint(1,16)
        nb=ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,21)
        o=name[na-1]
        del name [na-1]
        ul = random.randint(1,15)
        ob=ult[ul-1]
        del ult[ul-1]
        na = random.randint(1,20)
        p=name[na-1]
        del name [na-1]
        ul = random.randint(1,14)
        pb=ult[ul-1]
        del ult[ul-1]

else:
        a = input("\n \n \nEnter the character's name > ")
        ab = input("They are the Ultimate ")
        b = input("Enter the character's name > ")
        bb = input("They are the Ultimate ")
        c = input("Enter the character's name > ")
        cb = input("They are the Ultimate ")
        d = input("Enter the character's name > ")
        db = input("They are the Ultimate ")
        e = input("Enter the character's name > ")
        eb = input("They are the Ultimate ")
        f = input("Enter the character's name > ")
        fb = input("They are the Ultimate ")
        g = input("Enter the character's name > ")
        gb = input("They are the Ultimate ")
        h = input("Enter the character's name > ")
        hb = input("They are the Ultimate ")
        i = input("Enter the character's name > ")
        ib = input("They are the Ultimate ")
        j = input("Enter the character's name > ")
        jb = input("They are the Ultimate ")
        k = input("Enter the character's name > ")
        kb = input("They are the Ultimate ")
        l = input("Enter the character's name > ")
        lb = input("They are the Ultimate ")
        m = input("Enter the character's name > ")
        mb = input("They are the Ultimate ")
        n = input("Enter the character's name > ")
        nb = input("They are the Ultimate ")
        o = input("Enter the character's name > ")
        ob = input("They are the Ultimate ")
        p = input("Enter the character's name > ")
        pb = input("They are the Ultimate ")



        
        
        
chara = a + " Ultimate  " + ab
charb = b + " Ultimate  " + bb
charc = c + " Ultimate  " + cb
chard = d + " Ultimate  " + db
chare = e + " Ultimate  " + eb
charf = f + " Ultimate  " + fb
charg = g + " Ultimate  " + gb
charh = h + " Ultimate  " + hb
chari = i + " Ultimate  " + ib
charj = j + " Ultimate  " + jb
chark = k + " Ultimate  " + kb
charl = l + " Ultimate  " + lb
charm = m + " Ultimate  " + mb
charn = n + " Ultimate  " + nb
charo = o + " Ultimate  " + ob
charp = p + " Ultimate  " + pb


studentlist = [chara,charb,charc,chard,chare,charf,charg,charh,chari,charj,chark,charl,charm,charn,charo,charp]

print ("\nThese are the newest 16 students of Hope's Peak Academy:")

for item in studentlist:
        print(item)

go = input("\n \n \nPress Enter to continue...\n \n \n")
time.sleep(1)


print("\nChapter 1\n ")












#THIS IS THE START OF THE STORY!!!!







go = input("\n \n \nPress Enter to continue...\n \n \n")



print("One by one the students awoke, realising they were trapped inside Hope's Peak. They looked around for others.\nEventually, everyone gathered in the gym where Monokuma appeared. He told the students that they were trapped in Hope's Peak indefinitely and that the only way out was to commit a murder and get away with it.\nThe students left the gym in shock, all refusing to believe the truth and horror of their situation.")

go = input("\n \n \nPress Enter to continue...\n \n \n")



amount = random.randint(1,3)
if amount == 1:
        eve = random.randint(1,6)
        stu = random.randint(1,16)
        stu1 = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,15)
        stu2 = studentlist[stuu-1]
        del studentlist[stuu-1]
        if eve == 1:
                print("{0} and {1} watched a movie together in the av studio.".format(stu1,stu2))
        if eve == 2:
                print("{0} and {1} had dinner together in the dining hall.".format(stu1,stu2))
        if eve == 3:
                print("{0} and {1} went to explore the school.".format(stu1,stu2))
        if eve == 4:
                print("{0} and {1} hung out in the gym.".format(stu1,stu2))
        if eve == 5:
                print("{0} and {1} chatted in {1}'s room.".format(stu1,stu2))
        if eve == 6:
                print("{0} and {1} made food for the other students.".format(stu1,stu2))

        studentlist.append(stu1)
        studentlist.append(stu2)
if amount == 2:
        eve = random.randint(1,6)
        stu = random.randint(1,16)
        stu1 = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,15)
        stu2 = studentlist[stuu-1]
        del studentlist[stuu-1]
        stuuu = random.randint(1,14)
        stu3 = studentlist[stuuu-1]
        del studentlist[stuuu-1]
        if eve == 1:
                print("{0}, {1} and {2} had a tea party in the dining hall.".format(stu1,stu2,stu3))
        if eve == 2:
                print("{0}, {1} and {2} tried to find a way out of Hope's Peak.".format(stu1,stu2,stu3))
        if eve == 3:
                print("{0}, {1} and {2} watched anime in the AV room.".format(stu1,stu2,stu3))
        if eve == 4:
                print("{0}, {1} and {2} explored the school.".format(stu1,stu2,stu3))
        if eve == 5:
                print("{0}, {1} and {2} chatted in the gym.".format(stu1,stu2,stu3))
        if eve == 6:
                print("{0}, {1} and {2} had a sleepover.".format(stu1,stu2,stu3))
        studentlist.append(stu1)
        studentlist.append(stu2)
        studentlist.append(stu3)



if amount == 3:
        eve = random.randint(1,6)
        if eve == 1:
                print("The whole class attempted to find a way out of Hope's Peak.")
        if eve == 2:
                print("The whole class explored Hope's Peak.")
        if eve == 3:
                print("The whole class chatted in the gym.")
        if eve == 4:
                print("The whole class dined together in the dining hall.")
        if eve == 5:
                print("The whole class plotted to kill Monokuma, even though it failed.")
        if eve == 6:
                print("The whole class played tag inside Hope's Peak.")

go = input("\n \n \nPress Enter to continue...\n \n \n")



amount = random.randint(1,3)
if amount == 1:
        eve = random.randint(1,6)
        stu = random.randint(1,16)
        stua = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,15)
        stub = studentlist[stuu-1]
        del studentlist[stuu-1]
        if eve == 1:
                print("{0} and {1} watched a horror movie together in the av studio.".format(stua,stub))
        if eve == 2:
                print("{0} and {1} make medicines in the chem lab.".format(stua,stub))
        if eve == 3:
                print("{0} and {1} went to explore the school.".format(stua,stub))
        if eve == 4:
                print("{0} and {1} hung out in the gym.".format(stua,stub))
        if eve == 5:
                print("{0} and {1} chatted in {1}'s room.".format(stua,stub))
        if eve == 6:
                print("{0} and {1} made food for the other students.".format(stua,stub))

        studentlist.append(stua)
        studentlist.append(stub)
if amount == 2:
        eve = random.randint(1,6)
        stu = random.randint(1,16)
        stua = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,15)
        stub = studentlist[stuu-1]
        del studentlist[stuu-1]
        stuuu = random.randint(1,14)
        stuc = studentlist[stuuu-1]
        del studentlist[stuuu-1]
        if eve == 1:
                print("{0}, {1} and {2} had a food fight in the dining hall.".format(stua,stub,stuc))
        if eve == 2:
                print("{0}, {1} and {2} tried to find a way out of Hope's Peak.".format(stua,stub,stuc))
        if eve == 3:
                print("{0}, {1} and {2} watched anime in the av room.".format(stua,stub,stub))
        if eve == 4:
                print("{0}, {1} and {2} explored the school.".format(stua,stub,stuc))
        if eve == 5:
                print("{0}, {1} and {2} chatted in the gym.".format(stua,stub,stuc))
        if eve == 6:
                print("{0}, {1} and {2} had a sleepover.".format(stua,stub,stuc))
        studentlist.append(stua)
        studentlist.append(stub)
        studentlist.append(stuc)



if amount == 3:
        eve = random.randint(1,6)
        if eve == 1:
                print("The whole class attempted to find a way out of Hope's Peak.")
        if eve == 2:
                print("The whole class explored Hope's Peak.")
        if eve == 3:
                print("The whole class chatted in the gym.")
        if eve == 4:
                print("The whole class dined together in the dining hall.")
        if eve == 5:
                print("The whole class plotted to kill Monokuma.")
        if eve == 6:
                print("The whole class played tag inside Hope's Peak.")


go = input("\n \n \nPress Enter to continue\n \n \n")

reel = random.randint(1,4)
rel = random.randint(1,16)
rela = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,15)
relb = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(rela,relb))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(rela,relb))
if reel == 3:
        print("{0} and {1} love eachother.".format(rela,relb))
if reel == 4:
        print("{0} and {1} hate eachother.".format(rela,relb))
studentlist.append(rela)
studentlist.append(relb)
go = input("\n \n \nPress Enter to continue...\n \n \n")

mot = random.randint(1,19)
motive = motlist[mot-1]
print(motive)
del motlist[mot-1]
go = input("\n \n \npress enter to continue\n \n \n")


















kill = random.randint(1,16)
deada = studentlist[kill-1]
deadlist = [deada]
del studentlist[kill-1]
choice = random.randint(1,10)
if choice == 1:
        print(deada,"was found in their room, stabbed to death with a kitchen knife.")
if choice == 2:
        print(deada,"was found hung in the gym.")
if choice == 3:
        print(deada,"was found with their throat slit in the nurses office.")
if choice == 4:
        print(deada,"was found dismembered in their bathroom.")
if choice == 5:
        print(deada,"was found with their skull crushed in the av room.")
if choice == 6:
        print(deada,"was found burnt to death in the stove.")
if choice == 7:
        print(deada,"was found in pieces within the food.")
if choice == 8:
        print(deada,"was found strangled in class 1-A.")
if choice == 9:
        print(deada,"was found decapitated in the dining hall.")
if choice == 10:
        print(deada,"was found motionless in the corridor after having glass forced down their throat.")
go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,15)
relc = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,14)
reld = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(relc,reld))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(relc,reld))
if reel == 3:
        print("{0} and {1} love eachother.".format(relc,reld))
if reel == 4:
        print("{0} and {1} hate eachother.".format(relc,reld))
studentlist.append(relc)
studentlist.append(reld)
go = input("\n \n \nPress Enter to continue...\n \n \n")
print("\n15 remaining students")
for item in studentlist:
        print(item)

print("\n1 deceased student")
for item in deadlist:
        print(item)
        
go = input("\n \n \nPress Enter to continue...\n \n \n")



print("\nThe remaining students began an investigation...")
go = input("\n \n \nPress Enter to continue...\n \n \n")



trial = random.randint(1,25)
killer = random.randint(1,15)
blackeneda = studentlist[killer-1]
tri = random.randint(1,10)
if trial == 1:
        tri = random.randint(1,5)
        if tri == 1:
                print("\nThe students voted incorrectly, they were so sure they found the killer, the whole class was gassed in the courtroom. {0} had a gas mask that they wore as they left Hope's Peak and their dying classmates behind.".format(blackeneda))
        if tri == 2:
                print("\nNo matter how hard the class tried they couldnt come to a verdict, {0} was put into a glass elevator that left the Hope's Peak as the courtroom filled with water.".format(blackeneda))
        if tri == 3:
                print("\nThe students voted who they thought was the killer. It was a close vote, but the class lost by one vote. Because of that {0} walked out of hopes peak as it burned to the ground.".format(blackeneda))
        if tri == 4:
                print("\nThe killer was not voted guilty,because the class refused to vote- only the killer did. {0}, the killer, walked out of hopes peak as the courtroom filled with acid".format(blackeneda))
        if tri == 5:
                print("\n{0} managed to avoid being voted. They left hopes peak as it exploded, killing all the students inside".format(blackeneda))
        print("\n{0} survived".format(blackeneda))
        del studentlist[killer-1]
        deadlist = deadlist + studentlist
        studentlist = blackeneda
        surv = open("surv.txt","a",newline = "")
        writer = csv.writer(surv)
        writer.writerow([studentlist])
        surv.close()
        dead = open("dead.txt","a",newline="")
        write= csv.writer(dead)
        write.writerow([deadlist])
        dead.close()
        exit()
else:
        execu = random.randint(1,14)
        execution = punish[execu-1]
        del punish[execu-1]
        print(execution.format(blackeneda))
        del studentlist[killer-1]
        deadlist = [deada,blackeneda]
go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,14)
rele = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,13)
relf = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(rele,relf))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(rele,relf))
if reel == 3:
        print("{0} and {1} love eachother.".format(rele,relf))
if reel == 4:
        print("{0} and {1} hate eachother.".format(rele,relf))
studentlist.append(rele)
studentlist.append(relf)
go = input("\n \n \nPress Enter to continue...\n \n \n")

print("\n14 remaining students")
for item in studentlist:
        print(item)


print("\n2 deceased students")
for item in deadlist:
        print(item)




go = input("\n \n \nPress Enter to continue\n \n \n")
time.sleep(1)
print("\nChapter 2\n ")


























go = input("\n \n \nPress Enter to continue...\n \n \n")

amount = random.randint(1,3)
if amount == 1:
        eve = random.randint(1,6)
        stu = random.randint(1,14)
        stu4 = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,13)
        stu5 = studentlist[stuu-1]
        del studentlist[stuu-1]
        if eve == 1:
                print("{0} and {1} watched a comedy movie together in the av studio.".format(stu4,stu5))
        if eve == 2:
                print("{0} and {1} went swimming in the pool.".format(stu4,stu5))
        if eve == 3:
                print("{0} and {1} went to explore the school.".format(stu4,stu5))
        if eve == 4:
                print("{0} and {1} hung out in the libary.".format(stu4,stu5))
        if eve == 5:
                print("{0} and {1} chatted in {1}'s room.".format(stu4,stu5))
        if eve == 6:
                print("{0} and {1} made food for the other students.".format(stu4,stu5))

        studentlist.append(stu4)
        studentlist.append(stu5)
if amount == 2:
        eve = random.randint(1,6)
        stu = random.randint(1,14)
        stu4 = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,13)
        stu5 = studentlist[stuu-1]
        del studentlist[stuu-1]
        stuuu = random.randint(1,12)
        stu6 = studentlist[stuuu-1]
        del studentlist[stuuu-1]
        if eve == 1:
                print("{0}, {1} and {2} celebrated the birthday of {2}.".format(stu4,stu5,stu6))
        if eve == 2:
                print("{0}, {1} and {2} tried to find a way out of Hope's Peak.".format(stu4,stu5,stu6))
        if eve == 3:
                print("{0}, {1} and {2} watched anime in the av room.".format(stu4,stu5,stu6))
        if eve == 4:
                print("{0}, {1} and {2} explored the school.".format(stu4,stu5,stu6))
        if eve == 5:
                print("{0}, {1} and {2} did a book club in the libary.".format(stu4,stu5,stu6))
        if eve == 6:
                print("{0}, {1} and {2} had a swimming race".format(stu4,stu5,stu6))
        studentlist.append(stu4)
        studentlist.append(stu5)
        studentlist.append(stu6)



if amount == 3:
        eve = random.randint(1,6)
        if eve == 1:
                print("The whole class attempted to find a way out of Hope's Peak.")
        if eve == 2:
                print("The whole class explored Hope's Peak.")
        if eve == 3:
                print("The whole class had a swimming competition.")
        if eve == 4:
                print("The whole class dined together in the dining hall.")
        if eve == 5:
                print("The whole class plotted to kill Monokuma.")
        if eve == 6:
                print("The whole class chatted in the libary.")

go = input("\n \n \nPress Enter to continue...\n \n \n")



amount = random.randint(1,3)
if amount == 1:
        eve = random.randint(1,6)
        stu = random.randint(1,14)
        stud = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,13)
        stue = studentlist[stuu-1]
        del studentlist[stuu-1]
        if eve == 1:
                print("{0} and {1} watched an action movie together in the av studio.".format(stud,stue))
        if eve == 2:
                print("{0} and {1} play beer pong in the dining room.".format(stud,stue))
        if eve == 3:
                print("{0} and {1} went swimming.".format(stud,stue))
        if eve == 4:
                print("{0} and {1} hung out in the gym.".format(stud,stue))
        if eve == 5:
                print("{0} and {1} chatted in {0}'s room.".format(stud,stue))
        if eve == 6:
                print("{0} and {1} did some exersise in the gym.".format(stud,stue))

        studentlist.append(stud)
        studentlist.append(stue)
if amount == 2:
        eve = random.randint(1,6)
        stu = random.randint(1,14)
        stud = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,13)
        stue = studentlist[stuu-1]
        del studentlist[stuu-1]
        stuuu = random.randint(1,12)
        stuf = studentlist[stuuu-1]
        del studentlist[stuuu-1]
        if eve == 1:
                print("{0}, {1} and {2} planted some magnolias in the garden.".format(stud,stue,stuf))
        if eve == 2:
                print("{0}, {1} and {2} tried to find a way out of Hope's Peak.".format(stud,stue,stuf))
        if eve == 3:
                print("{0}, {1} and {2} went swimming.".format(stud,stue,stuf))
        if eve == 4:
                print("{0}, {1} and {2} explored the school.".format(stud,stue,stuf))
        if eve == 5:
                print("{0}, {1} and {2} chatted in the gym.".format(stud,stue,stuf))
        if eve == 6:
                print("{0}, {1} and {2} had a sleepover.".format(stud,stue,stuf))
        studentlist.append(stud)
        studentlist.append(stue)
        studentlist.append(stuf)



if amount == 3:
        eve = random.randint(1,6)
        if eve == 1:
                print("The whole class attempted to find a way out of Hope's Peak.")
        if eve == 2:
                print("The whole class explored Hope's Peak.")
        if eve == 3:
                print("The whole class chatted in the gym.")
        if eve == 4:
                print("The whole class dined together in the dining hall.")
        if eve == 5:
                print("The whole class plotted to kill Monokuma.")
        if eve == 6:
                print("The whole class played hide and seek inside Hope's Peak.")





go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,14)
relg = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,13)
relh = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(relg,relh))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(relg,relh))
if reel == 3:
        print("{0} and {1} love eachother.".format(relg,relh))
if reel == 4:
        print("{0} and {1} hate eachother.".format(relg,relh))
studentlist.append(relg)
studentlist.append(relh)
go = input("\n \n \nPress Enter to continue...\n \n \n")
mot = random.randint(1,18)
motive = motlist[mot-1]
print(motive)
del motlist[mot-1]
go = input("\n \n \nPress Enter to continue...\n \n \n")




kill = random.randint(1,14)
deadb = studentlist[kill-1]
deadlist = [deada,blackeneda,deadb]
del studentlist[kill-1]
choice = random.randint(1,10)
if choice == 1:
        print(deadb,"was found choked to death in the stairwell.")
if choice == 2:
        print(deadb,"was found suffocated to death on smoke.")
if choice == 3:
        print(deadb,"was found dissected in the nurse's office with their organs in labelled glass jars.")
if choice == 4:
        print(deadb,"was found dismembered in the warehouse.")
if choice == 5:
        print(deadb,"was found after suffering a drug overdose.")
if choice == 6:
        print(deadb,"was found drowned in the bathhouse.")
if choice == 7:
        print(deadb,"was found dead in the cafe pinned to the wall with knives.")
if choice == 8:
        print(deadb,"was found electrocuted in their bathroom.")
if choice == 9:
        print(deadb,"was found decapitated in the libary.")
if choice == 10:
        print(deadb,"was found poisoned in the nurse's office after digesting out-of-date antibiotics.")
go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,13)
reli = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,12)
relj = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(reli,relj))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(reli,relj))
if reel == 3:
        print("{0} and {1} love eachother.".format(reli,relj))
if reel == 4:
        print("{0} and {1} hate eachother.".format(reli,relj))
studentlist.append(reli)
studentlist.append(relj)
go = input("\n \n \nPress Enter to continue\n \n \n")
print("\n13 remaining students")
for item in studentlist:
        print(item)

print("\n3 deceased student")
for item in deadlist:
        print(item)
        

go = input("\n \n \nPress Enter to continue...\n \n \n")

print("\nThe remaining students began an investigation...")
go = input("\n \n \npress enter to continue\n \n \n")
trial = random.randint(1,25)
killer = random.randint(1,13)
blackenedb = studentlist[killer-1]
if trial == 1:
        tri = random.randint(1,5)
        if tri == 1:
                print("\nThe stuents voted incorectly- they were so sure they found the killer. The whole class was gassed in the courtroom, but {0}, the killer, had a gas mask that they wore as they left hopes peak and their dying classmates behind".format(blackenedb))
        if tri == 2:
                print("\nNo matter how hard the class tried they couldnt come to a verdict. {0}, the killer, was put into a glass elevator that left Hope's Peak as the courtroom filled with water".format(blackenedb))
        if tri == 3:
                print("\nThey voted who they thought was the killer. It was a close vote, but the class lost by one vote. Because of that {0}, the killer, walked out of hopes peak as it burned down to the ground".format(blackenedb))
        if tri == 4:
                print("\nThe killer was not voted guilty,because the class did not vote- only the killer did. {0}, the killer, walked out of hopes peak as the courtroom filled with acid".format(blackenedb))
        if tri == 5:
                print("\n{0} managed to avoid being voted. They left hopes peak as it exploded, killing all the students inside".format(blackenedb))
        print("\n{0} survived".format(blackenedb))
        del studentlist[killer-1]
        deadlist = deadlist + studentlist
        studentlist = blackenedb
        surv = open("surv.txt","a",newline = "")
        writer = csv.writer(surv)
        writer.writerow([studentlist])
        surv.close()
        dead = open("dead.txt","a",newline="")
        write= csv.writer(dead)
        write.writerow([deadlist])
        dead.close()
        exit()

else:
        execu = random.randint(1,13)
        execution = punish[execu-1]
        del punish[execu-1]
        print(execution.format(blackenedb))
        del studentlist[killer-1]
        deadlist = [deada,blackeneda,deadb,blackenedb]
go = input("\n \n \npress enter to continue\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,12)
relk = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,11)
rell = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(relk,rell))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(relk,rell))
if reel == 3:
        print("{0} and {1} love eachother.".format(relk,rell))
if reel == 4:
        print("{0} and {1} hate eachother.".format(relk,rell))
studentlist.append(relk)
studentlist.append(rell)
go = input("\n \n \nPress Enter to Continue\n \n \n")
print("\n12 remaining students")
for item in studentlist:
        print(item)

print("\n4 deceased students")
for item in deadlist:
        print(item)


go = input("\n \n \nPress Enter to continue...\n \n \n")
time.sleep(1)
print("\nchapter 3\n ")
























go = input("\n \n \nPress Enter to continue...\n \n \n")

amount = random.randint(1,3)
if amount == 1:
        eve = random.randint(1,6)
        stu = random.randint(1,12)
        stu7 = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,11)
        stu8 = studentlist[stuu-1]
        del studentlist[stuu-1]
        if eve == 1:
                print("{0} and {1} watched a thriller together in the av studio.".format(stu7,stu8))
        if eve == 2:
                print("{0} and {1} had lunch together in the dining hall.".format(stu7,stu8))
        if eve == 3:
                print("{0} and {1} went to explore the school.".format(stu7,stu8))
        if eve == 4:
                print("{0} and {1} hung out in the rec room.".format(stu7,stu8))
        if eve == 5:
                print("{0} and {1} chatted in {1}'s room.".format(stu7,stu8))
        if eve == 6:
                print("{0} and {1} looked around the physics lab.".format(stu7,stu8))

        studentlist.append(stu7)
        studentlist.append(stu8)
if amount == 2:
        eve = random.randint(1,6)
        stu = random.randint(1,12)
        stu7 = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,11)
        stu8 = studentlist[stuu-1]
        del studentlist[stuu-1]
        stuuu = random.randint(1,10)
        stu9 = studentlist[stuuu-1]
        del studentlist[stuuu-1]
        if eve == 1:
                print("{0}, {1} and {2} did some art together in the art studio.".format(stu7,stu8,stu9))
        if eve == 2:
                print("{0}, {1} and {2} tried to find a way out of Hope's Peak.".format(stu7,stu8,stu9))
        if eve == 3:
                print("{0}, {1} and {2} watched anime in the av room.".format(stu7,stu8,stu9))
        if eve == 4:
                print("{0}, {1} and {2} explored the school.".format(stu7,stu8,stu9))
        if eve == 5:
                print("{0}, {1} and {2} chatted in the rec room.".format(stu7,stu8,stu9))
        if eve == 6:
                print("{0}, {1} and {2} had a sleepover.".format(stu7,stu8,stu9))
        studentlist.append(stu7)
        studentlist.append(stu8)
        studentlist.append(stu9)



if amount == 3:
        eve = random.randint(1,6)
        if eve == 1:
                print("The whole class attempted to find a way out of Hope's Peak.")
        if eve == 2:
                print("The whole class explored Hope's Peak.")
        if eve == 3:
                print("The whole class chatted in the rec room.")
        if eve == 4:
                print("The whole class had an art session in the art studio.")
        if eve == 5:
                print("The whole class plotted to kill Monokuma.")
        if eve == 6:
                print("The whole class played tag inside Hope's Peak.")

go = input("\n \n \nPress Enter to continue...\n \n \n")



amount = random.randint(1,3)
if amount == 1:
        eve = random.randint(1,6)
        stu = random.randint(1,12)
        stug = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,11)
        stuh = studentlist[stuu-1]
        del studentlist[stuu-1]
        if eve == 1:
                print("{0} and {1} watched a documentary together in the av studio.".format(stug,stuh))
        if eve == 2:
                print("{0} and {1} celebrate {0}'s birthday.".format(stug,stuh))
        if eve == 3:
                print("{0} and {1} went to explore the school.".format(stug,stuh))
        if eve == 4:
                print("{0} and {1} played chess in the rec room.".format(stug,stuh))
        if eve == 5:
                print("{0} and {1} chatted in {0}'s room.".format(stug,stuh))
        if eve == 6:
                print("{0} and {1} made food for the other students.".format(stug,stuh))

        studentlist.append(stug)
        studentlist.append(stuh)
if amount == 2:
        eve = random.randint(1,6)
        stu = random.randint(1,12)
        stug = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,11)
        stuh = studentlist[stuu-1]
        del studentlist[stuu-1]
        stuuu = random.randint(1,10)
        stui = studentlist[stuuu-1]
        del studentlist[stuuu-1]
        if eve == 1:
                print("{0}, {1} and {2} played some party games in the rec room".format(stug,stuh,stui))
        if eve == 2:
                print("{0}, {1} and {2} tried to find a way out of Hope's Peak.".format(stug,stuh,stui))
        if eve == 3:
                print("{0}, {1} and {2} watched anime in the av room.".format(stug,stuh,stui))
        if eve == 4:
                print("{0}, {1} and {2} explored the school.".format(stug,stuh,stui))
        if eve == 5:
                print("{0}, {1} and {2} chatted in the gym.".format(stug,stuh,stui))
        if eve == 6:
                print("{0}, {1} and {2} had a chess tornament in the rec room.".format(stug,stuh,stui))
        studentlist.append(stug)
        studentlist.append(stuh)
        studentlist.append(stui)



if amount == 3:
        eve = random.randint(1,6)
        if eve == 1:
                print("The whole class attempted to find a way out of Hope's Peak.")
        if eve == 2:
                print("The whole class explored Hope's Peak.")
        if eve == 3:
                print("The whole class chatted in the gym.")
        if eve == 4:
                print("The whole class dined together in the dining hall.")
        if eve == 5:
                print("The whole class plotted to kill Monokuma.")
        if eve == 6:
                print("The whole class played tag inside Hope's Peak.")


go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,12)
relm = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,11)
reln = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(relm,reln))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(relm,reln))
if reel == 3:
        print("{0} and {1} love eachother.".format(relm,reln))
if reel == 4:
        print("{0} and {1} hate eachother.".format(relm,reln))
studentlist.append(relm)
studentlist.append(reln)
go = input("\n \n \nPress Enter to continue...\n \n \n")

mot = random.randint(1,17)
motive = motlist[mot-1]
print(motive)
del motlist[mot-1]
go = input("\n \n \nPress Enter to continue...\n \n \n")


kill = random.randint(1,12)
deadc = studentlist[kill-1]



del studentlist[kill-1]
killb = random.randint(1,11)
deadd = studentlist[killb - 1]
del studentlist[killb -1]
choice = random.randint(1,10)       
if choice == 1:
        print("{0} was found in the rec room, stabbed to death and {1} was found crushed in the art room repository.".format(deadc,deadd))
if choice == 2:
        print("{0} was found drowned in the pool and {1} was found with a crushed head in the changing room.".format(deadc,deadd))
if choice == 3:
        print("{0} was found stabbed in the physics lab alongside {1}.".format(deadc,deadd))
if choice == 4:
        print("{0} was found dismembered in the rec room and {1} was hung in the gym.".format(deadc,deadd))
if choice == 5:
        print("{0} and {1} were found beaten to death in their rooms.".format(deadc,deadd))
if choice == 6:
        print("{0} was found with a katana piercing their chest in the nurses office and {1} was found stabbed in the back of their neck outside the nurses office.".format(deadc,deadd))
if choice == 7:
        print("{0} was found with slit wrists in their bathroom and {1} was found stabbed in the room belonging to {0}.".format(deadc,deadd))
if choice == 8:
        print("{0} was found with a crushed head in the floor 1 corridor and {1} was found in the same way on floor 2".format(deadc,deadd))
if choice == 9:
        print("{0} was found decapitated in the pool and {1} was found drowned at the bottom of the pool".format(deadc,deadd))
if choice == 10:
        print("{0} was found dissected in the nurses office and {1} was found chocked to death in the nurses office".format(deadc,deadd))

go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,10)
relo = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,9)
relp = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(relo,relp))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(relo,relp))
if reel == 3:
        print("{0} and {1} love eachother.".format(relo,relp))
if reel == 4:
        print("{0} and {1} hate eachother.".format(relo,relp))
studentlist.append(relo)
studentlist.append(relp)
go = input("\n \n \nPress Enter to continue...\n \n \n")
print("\n10 remaining students")

for item in studentlist:
        print(item)

deadlist = [deada,blackeneda,deadb,blackenedb,deadc,deadd]
print("\n6 deceased students")
for item in deadlist:
        print(item)
        
go = input("\n \n \nPress Enter to continue...\n \n \n")

print("\nThe remaining students began an investigation.")
go = input("\n \n \nPress Enter to continue...\n \n \n")
trial = random.randint(1,25)
killer = random.randint(1,10)
blackenedc = studentlist[killer-1]
if trial == 1:
        tri = random.randint(1,5)
        if tri == 1:
                print("\nThe stuents voted incorectly- they were so sure they found the killer. The whole class was gassed in the courtroom. {0} had a gas mask that they wore as they left Hope's Peak and their dying classmates behind.".format(blackenedc))
        if tri == 2:
                print("\nNo matter how hard the class tried they couldnt come to a verdict. {0} was put into a glass elevator that left Hope's Peak as the courtroom filled with water.".format(blackenedc))
        if tri == 3:
                print("\nThe class voted who they thought was the killer. It was a close vote; the class lost by one vote. Because of that, {0} walked out of hopes peak as it burned to the ground.".format(blackenedc))
        if tri == 4:
                print("\nThe killer was not voted guilty because the class did not vote- only the killer did. {0} walked out of Hope's Peak as the courtroom filled with acid".format(blackenedc))
        if tri == 5:
                print("\n{0} managed to avoid being voted. They left Hope's Peak as it exploded, killing all the students inside".format(blackenedc))
        print("\n{0} survived".format(blackenedc))
        del studentlist[killer-1]
        deadlist = deadlist + studentlist
        studentlist = blackenedc
        surv = open("surv.txt","a",newline = "")
        writer = csv.writer(surv)
        writer.writerow([studentlist])
        surv.close()
        dead = open("dead.txt","a",newline="")
        write= csv.writer(dead)
        write.writerow([deadlist])
        dead.close()
        exit()
else:
        execu = random.randint(1,12)
        execution = punish[execu-1]
        del punish[execu-1]
        print(execution.format(blackenedc))
        del studentlist[killer-1]
        deadlist = [deada,blackeneda,deadb,blackenedb,deadc,deadd,blackenedc]
        go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,9)
relq = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,8)
relr = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(relq,relr))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(relq,relr))
if reel == 3:
        print("{0} and {1} love eachother.".format(relq,relr))
if reel == 4:
        print("{0} and {1} hate eachother.".format(relq,relr))
studentlist.append(relq)
studentlist.append(relr)
go = input("\n \n \nPress Enter to continue...\n \n \n")
print("\n9 remaining students")
for item in studentlist:
        print(item)

print("\n7 deceased students")
for item in deadlist:
        print(item)


go = input("\n \n \nPress Enter to continue...\n \n \n")



time.sleep(1)
print("\nChapter 4\n")






















go = input("\n \n \nPress Enter to continue...\n \n \n")
amount = random.randint(1,3)
if amount == 1:
        eve = random.randint(1,6)
        stu = random.randint(1,9)
        stu10 = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,8)
        stu11 = studentlist[stuu-1]
        del studentlist[stuu-1]
        if eve == 1:
                print("{0} and {1} looked for clues about the game in the library.".format(stu10,stu11))
        if eve == 2:
                print("{0} and {1} had lunch together in the dining hall.".format(stu10,stu11))
        if eve == 3:
                print("{0} and {1} went to explore the school.".format(stu10,stu11))
        if eve == 4:
                print("{0} and {1} hung out in the rec room.".format(stu10,stu11))
        if eve == 5:
                print("{0} and {1} chatted in {1}'s room.".format(stu10,stu11))
        if eve == 6:
                print("{0} and {1} looked around the physics lab.".format(stu10,stu11))

        studentlist.append(stu10)
        studentlist.append(stu11)
if amount == 2:
        eve = random.randint(1,6)
        stu = random.randint(1,9)
        stu10 = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,8)
        stu11 = studentlist[stuu-1]
        del studentlist[stuu-1]
        stuuu = random.randint(1,7)
        stu12 = studentlist[stuuu-1]
        del studentlist[stuuu-1]
        if eve == 1:
                print("{0}, {1} and {2} did some art together in the art studio.".format(stu10,stu11,stu12))
        if eve == 2:
                print("{0}, {1} and {2} tried to find a way out of Hope's Peak.".format(stu10,stu11,stu12))
        if eve == 3:
                print("{0}, {1} and {2} watched anime in the av room.".format(stu10,stu11,stu12))
        if eve == 4:
                print("{0}, {1} and {2} explored the school.".format(stu10,stu11,stu12))
        if eve == 5:
                print("{0}, {1} and {2} chatted in the rec room.".format(stu10,stu11,stu12))
        if eve == 6:
                print("{0}, {1} and {2} had a sleepover.".format(stu10,stu11,stu12))
        studentlist.append(stu10)
        studentlist.append(stu11)
        studentlist.append(stu12)



if amount == 3:
        eve = random.randint(1,6)
        if eve == 1:
                print("The whole class attempted to find a way out of Hope's Peak.")
        if eve == 2:
                print("The whole class explored Hope's Peak.")
        if eve == 3:
                print("The whole class chatted in the rec room.")
        if eve == 4:
                print("The whole class had an art session in the art studio.")
        if eve == 5:
                print("The whole class plotted to kill Monokuma.")
        if eve == 6:
                print("The whole class played tag inside Hope's Peak.")

go = input("\n \n \nPress Enter to continue...\n \n \n")



amount = random.randint(1,3)
if amount == 1:
        eve = random.randint(1,6)
        stu = random.randint(1,9)
        stuj = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,8)
        stuk = studentlist[stuu-1]
        del studentlist[stuu-1]
        if eve == 1:
                print("{0} and {1} plotted to kill another student together.".format(stuj,stuk))
        if eve == 2:
                print("{0} and {1} made cakes in the kitchen.".format(stuj,stuk))
        if eve == 3:
                print("{0} and {1} went to explore the school.".format(stuj,stuk))
        if eve == 4:
                print("{0} and {1} played chess in the rec room.".format(stuj,stuk))
        if eve == 5:
                print("{0} and {1} chatted in {0}'s room.".format(stuj,stuk))
        if eve == 6:
                print("{0} and {1} made food for the other students.".format(stuj,stuk))

        studentlist.append(stuj)
        studentlist.append(stuk)
if amount == 2:
        eve = random.randint(1,6)
        stu = random.randint(1,9)
        stuj = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,8)
        stuk = studentlist[stuu-1]
        del studentlist[stuu-1]
        stuuu = random.randint(1,7)
        stul = studentlist[stuuu-1]
        del studentlist[stuuu-1]
        if eve == 1:
                print("{0}, {1} and {2} made pizzas in the kitchen.".format(stuj,stuk,stul))
        if eve == 2:
                print("{0}, {1} and {2} tried to find a way out of Hope's Peak.".format(stuj,stuk,stul))
        if eve == 3:
                print("{0}, {1} and {2} watched anime in the av room.".format(stuj,stuk,stul))
        if eve == 4:
                print("{0}, {1} and {2} explored the school.".format(stuj,stuk,stul))
        if eve == 5:
                print("{0}, {1} and {2} chatted in the gym.".format(stuj,stuk,stul))
        if eve == 6:
                print("{0}, {1} and {2} had a sleepover.".format(stuj,stuk,stul))
        studentlist.append(stuj)
        studentlist.append(stuk)
        studentlist.append(stul)



if amount == 3:
        eve = random.randint(1,6)
        if eve == 1:
                print("The whole class attempted to find a way out of Hope's Peak.")
        if eve == 2:
                print("The whole class explored Hope's Peak.")
        if eve == 3:
                print("The whole class chatted in the gym.")
        if eve == 4:
                print("The whole class dined together in the dining hall.")
        if eve == 5:
                print("The whole class plotted to kill Monokuma.")
        if eve == 6:
                print("The whole class played tag inside Hope's Peak.")


go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,9)
rels = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,8)
relt = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(rels,relt))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(rels,relt))
if reel == 3:
        print("{0} and {1} love eachother.".format(rels,relt))
if reel == 4:
        print("{0} and {1} hate eachother.".format(rels,relt))
studentlist.append(rels)
studentlist.append(relt)
go = input("\n \n \nPress Enter to continue...\n \n \n")
mot = random.randint(1,16)
motive = motlist[mot-1]
print(motive)
del motlist[mot-1]

go = input("\n \n \nPress Enter to continue...\n \n \n")





kill = random.randint(1,9)
deade = studentlist[kill-1]
deadlist = [deada,blackeneda,deadb,blackenedb,deadc,deadd,blackenedc,deade]
del studentlist[kill-1]
choice = random.randint(1,10)
if choice == 1:
        print(deade,"was found in the dining room after injesting superglue.")
if choice == 2:
        print(deade,"was found hung in the stairwell to floor 2.")
if choice == 3:
        print(deade,"was found skinned in the nurses office.")
if choice == 4:
        print(deade,"was found tortured in the warehouse.")
if choice == 5:
        print(deade,"was found with their skull smashed on the stairwell.")
if choice == 6:
        print(deade,"was found dead in the bathhouse.")
if choice == 7:
        print(deade,"was found stabbed in the chest in their bathroom.")
if choice == 8:
        print(deade,"was found strangled in the rec room.")
if choice == 9:
        print(deade,"was found decapitated in the art repository.")
if choice == 10:
        print(deade,"was found poisoned in the chem lab.")
go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,8)
relu = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,7)
relv = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(relu,relv))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(relu,relv))
if reel == 3:
        print("{0} and {1} love eachother.".format(relu,relv))
if reel == 4:
        print("{0} and {1} hate eachother.".format(relu,relv))
studentlist.append(relu)
studentlist.append(relv)
go = input("\n \n \nPress Enter to continue...\n \n \n")
print("\n8 remaining students")
for item in studentlist:
        print(item)

print("\n8 deceased students")
for item in deadlist:
        print(item)
        

go = input("\n \n \nPress Enter to continue...\n \n \n")
print("\nThe remaining students began an investigation.")
go = input("\n \n \nPress Enter to continue...\n \n \n")
trial = random.randint(1,25)
killer = random.randint(1,8)
blackenede = studentlist[killer-1]
if trial == 1:
        tri = random.randint(1,5)
        if tri == 1:
                print("\nThe stuents voted incorectly- they were so sure that they'd found the killer. The whole class was gassed in the courtroom. {0} had a gas mask that they wore as they left Hope's Peak and their dying classmates behind.".format(blackenede))
        if tri == 2:
                print("\nNo matter how hard the class tried they couldnt come to a verdict. {0} was put into a glass elevator that left Hope's Peak as the courtroom filled with water.".format(blackenede))
        if tri == 3:
                print("\nThe students voted who they thought was the killer. It was a close vote, but the class lost by one vote. Because of that {0} walked out of Hope's Peak as it burned down to the ground.".format(blackenede))
        if tri == 4:
                print("\nThe killer was not voted guilty because the class did not vote- only the killer did. {0} walked out of Hope's Peak as the courtroom filled with acid.".format(blackenede))
        if tri == 5:
                print("\n{0} managed to avoid being voted. They left Hope's Peak as it exploded, killing all the students inside.".format(blackenede))
        print("\n{0} survived".format(blackenede))
        del studentlist[killer-1]
        deadlist = deadlist + studentlist
        studentlist = blackenede
        surv = open("surv.txt","a",newline = "")
        writer = csv.writer(surv)
        writer.writerow([studentlist])
        surv.close()
        dead = open("dead.txt","a",newline="")
        write= csv.writer(dead)
        write.writerow([deadlist])
        dead.close()
        exit()
else:
        execu = random.randint(1,11)
        execution = punish[execu-1]
        del punish[execu-1]
        print(execution.format(blackenede))
        del studentlist[killer-1]
        deadlist = [deada,blackeneda,deadb,blackenedb,deadc,deadd,blackenedc,deade,blackenede]
        go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,7)
relw = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,6)
relx = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(relw,relx))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(relw,relx))
if reel == 3:
        print("{0} and {1} love eachother.".format(relw,relx))
if reel == 4:
        print("{0} and {1} hate eachother.".format(relw,relx))
studentlist.append(relw)
studentlist.append(relx)
go = input("\n \n \nPress Enter to continue...\n \n \n")
print("\n7 remaining students")
for item in studentlist:
        print(item)

print("\n9 deceased students")
for item in deadlist:
        print(item)



go = input("\n \n \nPress Enter to continue...\n \n \n")
time.sleep(1)
print("\nChapter 5\n ")




















go = input("\n \n \nPress Enter to continue...\n \n \n")
amount = random.randint(1,3)
if amount == 1:
        eve = random.randint(1,6)
        stu = random.randint(1,7)
        stu13 = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,6)
        stu14 = studentlist[stuu-1]
        del studentlist[stuu-1]
        if eve == 1:
                print("{0} and {1} watched a musical together in the av studio.".format(stu13,stu14))
        if eve == 2:
                print("{0} and {1} played football in the garden.".format(stu13,stu14))
        if eve == 3:
                print("{0} and {1} went to explore the school.".format(stu13,stu14))
        if eve == 4:
                print("{0} and {1} hung out in the gym.".format(stu13,stu14))
        if eve == 5:
                print("{0} and {1} chatted in {1}'s room.".format(stu13,stu14))
        if eve == 6:
                print("{0} and {1} made food for the other students.".format(stu13,stu14))

        studentlist.append(stu13)
        studentlist.append(stu14)
if amount == 2:
        eve = random.randint(1,6)
        stu = random.randint(1,7)
        stu13 = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,6)
        stu14 = studentlist[stuu-1]
        del studentlist[stuu-1]
        stuuu = random.randint(1,5)
        stu15 = studentlist[stuuu-1]
        del studentlist[stuuu-1]
        if eve == 1:
                print("{0}, {1} and {2} played Chubby Bunnies in the dining hall.".format(stu13,stu14,stu15))
        if eve == 2:
                print("{0}, {1} and {2} tried to find a way out of Hope's Peak.".format(stu13,stu14,stu15))
        if eve == 3:
                print("{0}, {1} and {2} watched anime in the av room.".format(stu13,stu14,stu15))
        if eve == 4:
                print("{0}, {1} and {2} explored the school.".format(stu13,stu14,stu15))
        if eve == 5:
                print("{0}, {1} and {2} chatted in the gym.".format(stu13,stu14,stu15))
        if eve == 6:
                print("{0}, {1} and {2} had a sleepover.".format(stu13,stu14,stu15))
        studentlist.append(stu13)
        studentlist.append(stu14)
        studentlist.append(stu15)



if amount == 3:
        eve = random.randint(1,6)
        if eve == 1:
                print("The whole class attempted to find a way out of Hope's Peak.")
        if eve == 2:
                print("The whole class explored Hope's Peak.")
        if eve == 3:
                print("The whole class chatted in the gym.")
        if eve == 4:
                print("The whole class dined together in the dining hall.")
        if eve == 5:
                print("The whole class plotted to kill Monokuma.")
        if eve == 6:
                print("The whole class played tag inside Hope's Peak.")

go = input("\n \n \nPress Enter to continue...\n \n \n")



amount = random.randint(1,3)
if amount == 1:
        eve = random.randint(1,6)
        stu = random.randint(1,7)
        stum = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,6)
        stun = studentlist[stuu-1]
        del studentlist[stuu-1]
        if eve == 1:
                print("{0} and {1} watched a romance together in the av studio.".format(stum,stun))
        if eve == 2:
                print("{0} and {1} played party games in the school.".format(stum,stun))
        if eve == 3:
                print("{0} and {1} went to explore the school.".format(stum,stun))
        if eve == 4:
                print("{0} and {1} hung out in the gym.".format(stum,stun))
        if eve == 5:
                print("{0} and {1} chatted in {1}'s room.".format(stum,stun))
        if eve == 6:
                print("{0} and {1} made food for the other students.".format(stum,stun))

        studentlist.append(stum)
        studentlist.append(stun)
if amount == 2:
        eve = random.randint(1,6)
        stu = random.randint(1,7)
        stum = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,6)
        stun = studentlist[stuu-1]
        del studentlist[stuu-1]
        stuuu = random.randint(1,5)
        stuo = studentlist[stuuu-1]
        del studentlist[stuuu-1]
        if eve == 1:
                print("{0}, {1} and {2} had a danceoff in the gym.".format(stum,stun,stuo))
        if eve == 2:
                print("{0}, {1} and {2} tried to find a way out of Hope's Peak.".format(stum,stun,stuo))
        if eve == 3:
                print("{0}, {1} and {2} watched anime in the av room.".format(stum,stun,stuo))
        if eve == 4:
                print("{0}, {1} and {2} explored the school.".format(stum,stun,stuo))
        if eve == 5:
                print("{0} sung for {1} and {2} in the music room.".format(stum,stun,stuo))
        if eve == 6:
                print("{0}, {1} and {2} had a sleepover.".format(stum,stun,stuo))
        studentlist.append(stum)
        studentlist.append(stun)
        studentlist.append(stuo)



if amount == 3:
        eve = random.randint(1,6)
        if eve == 1:
                print("The whole class attempted to find a way out of Hope's Peak.")
        if eve == 2:
                print("The whole class explored Hope's Peak.")
        if eve == 3:
                print("The whole class chatted in the rec room.")
        if eve == 4:
                print("The whole class had a swimming race.")
        if eve == 5:
                print("The whole class made a meal for each other but someone spiked the food with chemicals from the chem lab in an attempted murder.")
        if eve == 6:
                print("The whole class did an archery competition in the dojo.")


go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,7)
rely = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,6)
relz = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(rely,relz))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(rely,relz))
if reel == 3:
        print("{0} and {1} love eachother.".format(rely,relz))
if reel == 4:
        print("{0} and {1} hate eachother.".format(rely,relz))
studentlist.append(rely)
studentlist.append(relz)
go = input("\n \n \nPress Enter to continue...\n \n \n")


mot = random.randint(1,15)
motive = motlist[mot-1]
print(motive)
del motlist[mot-1]
go = input("\n \n \nPress Enter to continue...\n \n \n")
        



kill = random.randint(1,7)
deadf = studentlist[kill-1]
deadlist = [deada,blackeneda,deadb,blackenedb,deadc,deadd,blackenedc,deade,deadf]
del studentlist[kill-1]
choice = random.randint(1,10)
if choice == 1:
        print(deadf,"was found in the music room, stabbed to death with a kitchen knife.")
if choice == 2:
        print(deadf,"was found hung in the stairwell to floor 2.")
if choice == 3:
        print(deadf,"was found with their throat slit in the nurses office.")
if choice == 4:
        print(deadf,"was found dismembered in the greenhouse.")
if choice == 5:
        print(deadf,"was found shot with arrows in the dojo.")
if choice == 6:
        print(deadf,"was found dead in the bathhouse.")
if choice == 7:
        print(deadf,"was found stabbed in the chest in their bathroom.")
if choice == 8:
        print(deadf,"was found strangled in the rec room.")
if choice == 9:
        print(deadf,"was found decapitated in the art repository.")
if choice == 10:
        print(deadf,"was found poisoned in the chem lab.")
go = input("\n \n \nPress Enter to continue...\n \n \n")
print("\n6 remaining students")
for item in studentlist:
        print(item)

print("\n10 deceased students")
for item in deadlist:
        print(item)

go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,6)
rel1 = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,5)
rel2 = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(rel1,rel2))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(rel1,rel2))
if reel == 3:
        print("{0} and {1} love eachother.".format(rel1,rel2))
if reel == 4:
        print("{0} and {1} hate eachother.".format(rel1,rel2))
studentlist.append(rel1)
studentlist.append(rel2)
go = input("\n \n \nPress Enter to continue...\n \n \n")
print("\nThe remaining students began an investigation.")
go = input("\n \n \nPress Enter to continue...\n \n \n")
trial = random.randint(1,25)
killer = random.randint(1,6)
blackenedf = studentlist[killer-1]
if trial == 1:
        tri = random.randint(1,5)
        if tri == 1:
                print("\nThe stuents voted incorectly- they were so sure that they'd found the killer. The whole class was gassed in the courtroom. {0} had a gas mask that they wore as they left Hope's Peak and their dying classmates behind.".format(blackenedf))
        if tri == 2:
                print("\nNo matter how hard the class tried they couldnt come to a verdict, {0} was put into a glass elevator that left Hope's Peak as the courtroom filled with water.".format(blackenedf))
        if tri == 3:
                print("\nThe students voted who they thought was the killer. It was a close vote but the class lost by one vote. Because of that, {0} walked out of Hope's Peak as it burned down to the ground.".format(blackenedf))
        if tri == 4:
                print("\nThe killer was not voted guilty since the class refused the vote. vote. {0} walked out of Hope's Peak as the courtroom filled with acid.".format(blackenedf))
        if tri == 5:
                print("\n{0} managed to avoid being voted. They left Hope's Peak as it exploded, killing all the students inside.".format(blackenedf))
        print("\n{0} survived".format(blackenedf))
        del studentlist[killer-1]
        deadlist = deadlist + studentlist
        studentlist = blackenedf
        surv = open("surv.txt","a",newline = "")
        writer = csv.writer(surv)
        writer.writerow([studentlist])
        surv.close()
        dead = open("dead.txt","a",newline="")
        write= csv.writer(dead)
        write.writerow([deadlist])
        dead.close()
        exit()
else:
        execu = random.randint(1,10)
        execution = punish[execu-1]
        del punish[execu-1]
        print(execution.format(blackenedf))
        del studentlist[killer-1]
        deadlist = [deada,blackeneda,deadb,blackenedb,deadc,deadd,blackenedc,deade,blackenede,deadf,blackenedf]
go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,5)
rel3 = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,4)
rel4 = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(rel3,rel4))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(rel3,rel4))
if reel == 3:
        print("{0} and {1} love eachother.".format(rel3,rel4))
if reel == 4:
        print("{0} and {1} hate eachother.".format(rel3,rel4))
studentlist.append(rel3)
studentlist.append(rel4)
go = input("\n \n \nPress Enter to continue...\n \n \n")
print("\n5 remaining students")
for item in studentlist:
        print(item)

print("\n11 deceased students")
for item in deadlist:
        print(item)












go = input("\n \n \nPress Enter to continue...\n \n \n")



time.sleep(1)
print("\nChapter 6\n ")
















go = input("\n \n \nPress Enter to continue...\n \n \n")


uprise = random.randint(1,10)
if uprise == 1:
        print("The class had an uprising against the killing game. Monokuma ordered a final trial and the students begin a final investigation...")
        trial = random.randint(1,10)
        go = input("\n \n \nPress Enter to continue...\n \n \n")
        if trial == 1:
                print("\nThe class refused to vote. They refused to choose between hope and despair, between freedom and continuing; they realised that by voting, the killing game will happen again. As a result they were all punished.\n\nNo survivors.")
                deadlist = deadlist + studentlist
                surv = open("surv.txt","a",newline = "")
                writer = csv.writer(surv)
                writer.writerow(["No survivors"])
                surv.close()
                dead = open("dead.txt","a",newline="")
                write= csv.writer(dead)
                write.writerow([deadlist])
                dead.close()
                exit()
                exit()
        elif trial == 2:
                print("\nThey voted despair- they voted to continue the killing game.")
                go = input("\n \n \nPress Enter to continue...\n \n \n")
        else:   
                themast = random.randint(1,5)
                killer = themast
                master = studentlist[killer-1]
                deadlist = [deada,blackeneda,deadb,blackenedb,deadc,deadd,blackenedc,deade,deadf,master]
                del studentlist[killer-1]
                print("\nThey voted hope and {0} was executed for being the mastermind. The students keenly left Hope's Peak and ventured into the new world outside...".format(master))
                print("\n4 students survived:")
                for item in studentlist:
                        print(item)
                surv = open("surv.txt","a",newline = "")
                writer = csv.writer(surv)
                writer.writerow([studentlist])
                surv.close()
                dead = open("dead.txt","a",newline="")
                write= csv.writer(dead)
                write.writerow([deadlist])
                dead.close()
                exit()



amount = random.randint(1,3)
if amount == 1:
        eve = random.randint(1,6)
        stu = random.randint(1,5)
        stu16 = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,4)
        stu17 = studentlist[stuu-1]
        del studentlist[stuu-1]
        if eve == 1:
                print("{0} and {1} watched a musical together in the av studio.".format(stu16,stu17))
        if eve == 2:
                print("{0} and {1} plotted a murder suicide.".format(stu16,stu17))
        if eve == 3:
                print("{0} and {1} went to explore the school.".format(stu16,stu17))
        if eve == 4:
                print("{0} and {1} hung out in the gym.".format(stu16,stu17))
        if eve == 5:
                print("{0} and {1} chatted in {1}'s room.".format(stu16,stu17))
        if eve == 6:
                print("{0} and {1} made food for the other students.".format(stu16,stu17))

        studentlist.append(stu16)
        studentlist.append(stu17)
if amount == 2:
        eve = random.randint(1,6)
        stu = random.randint(1,5)
        stu16 = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,4)
        stu17 = studentlist[stuu-1]
        del studentlist[stuu-1]
        stuuu = random.randint(1,3)
        stu18 = studentlist[stuuu-1]
        del studentlist[stuuu-1]
        if eve == 1:
                print("{0}, {1} and {2} made fudge in the kitchen.".format(stu16,stu17,stu18))
        if eve == 2:
                print("{0}, {1} and {2} tried to find a way out of Hope's Peak.".format(stu16,stu17,stu18))
        if eve == 3:
                print("{0}, {1} and {2} watched anime in the av room.".format(stu16,stu17,stu18))
        if eve == 4:
                print("{0}, {1} and {2} explored the school.".format(stu16,stu17,stu18))
        if eve == 5:
                print("{0}, {1} and {2} chatted in the gym.".format(stu16,stu17,stu18))
        if eve == 6:
                print("{0}, {1} and {2} had a sleepover.".format(stu16,stu17,stu18))
        studentlist.append(stu16)
        studentlist.append(stu17)
        studentlist.append(stu18)



if amount == 3:
        eve = random.randint(1,6)
        if eve == 1:
                print("The whole class attempted to find a way out of Hope's Peak.")
        if eve == 2:
                print("The whole class explored Hope's Peak.")
        if eve == 3:
                print("The whole class chatted in the garden.")
        if eve == 4:
                print("The whole class dined together in the dining hall.")
        if eve == 5:
                print("The whole class plotted to kill Monokuma.")
        if eve == 6:
                print("The whole class played tag inside Hope's Peak.")

go = input("\n \n \nPress Enter to continue...\n \n \n")



amount = random.randint(1,3)
if amount == 1:
        eve = random.randint(1,6)
        stu = random.randint(1,7)
        stup = studentlist[stu-1]
        del studentlist[stu-1]
        stuq = random.randint(1,6)
        stuq = studentlist[stuu-1]
        del studentlist[stuu-1]
        if eve == 1:
                print("{0} and {1} watched The Emoji Movie together in the av studio.".format(stup,stuq))
        if eve == 2:
                print("{0} and {1} ".format(stup,stuq))
        if eve == 3:
                print("{0} and {1} went to explore the school.".format(stup,stuq))
        if eve == 4:
                print("{0} and {1} hung out in the gym.".format(stup,stuq))
        if eve == 5:
                print("{0} and {1} chatted in {1}'s room.".format(stup,stuq))
        if eve == 6:
                print("{0} and {1} made food for the other students.".format(stup,stuq))

        studentlist.append(stup)
        studentlist.append(stuq)
if amount == 2:
        eve = random.randint(1,6)
        stu = random.randint(1,5)
        stup = studentlist[stu-1]
        del studentlist[stu-1]
        stuu = random.randint(1,4)
        stuq = studentlist[stuu-1]
        del studentlist[stuu-1]
        stuuu = random.randint(1,3)
        stur = studentlist[stuuu-1]
        del studentlist[stuuu-1]
        if eve == 1:
                print("{0}, {1} and {2} chatted about how to prevent more murders.".format(stup,stuq,stur))
        if eve == 2:
                print("{0}, {1} and {2} tried to find a way out of Hope's Peak.".format(stup,stuq,stur))
        if eve == 3:
                print("{0}, {1} and {2} watched anime in the av room.".format(stup,stuq,stur))
        if eve == 4:
                print("{0}, {1} and {2} explored the school.".format(stup,stuq,stur))
        if eve == 5:
                print("{0} sung for {1} and {2} in the music room.".format(stup,stuq,stur))
        if eve == 6:
                print("{0}, {1} and {2} had a sleepover.".format(stup,stuq,stur))
        studentlist.append(stup)
        studentlist.append(stuq)
        studentlist.append(stur)



if amount == 3:
        eve = random.randint(1,6)
        if eve == 1:
                print("The whole class attempted to find a way out of Hope's Peak.")
        if eve == 2:
                print("The whole class explored Hope's Peak.")
        if eve == 3:
                print("The whole class chatted in the rec room.")
        if eve == 4:
                print("The whole class had a swiming race.")
        if eve == 5:
                print("The whole class made a meal for each other but someone spiked the food with a chemical from the chem lab in an attempted murder.")
        if eve == 6:
                print("The whole class did an archery competition in the dojo.")
go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,5)
rel6 = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,4)
rel5 = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(rel6,rel5))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(rel6,rel5))
if reel == 3:
        print("{0} and {1} love eachother.".format(rel6,rel5))
if reel == 4:
        print("{0} and {1} hate eachother.".format(rel6,rel5))
studentlist.append(rel6)
studentlist.append(rel5)
go = input("\n \n \nPress Enter to continue...\n \n \n")

mot = random.randint(1,14)
motive = motlist[mot-1]
print(motive)
del motlist[mot-1]
go = input("\n \n \nPress Enter to continue...\n \n \n")



kill = random.randint(1,5)
deadg = studentlist[kill-1]
deadlist = [deada,blackeneda,deadb,blackenedb,deadc,deadd,blackenedc,deade,deadf,blackenedf,deadg]
del studentlist[kill-1]
choice = random.randint(1,10)
if choice == 1:
        print(deadg,"was found in the music room, stabbed to death with a kitchen knife.")
if choice == 2:
        print(deadg,"was found gutted in the nurses office.")
if choice == 3:
        print(deadg,"was found with their throat slit in the nurses office.")
if choice == 4:
        print(deadg,"was found dismembered in the greenhouse.")
if choice == 5:
        print(deadg,"was found shot with arrows in the dojo.")
if choice == 6:
        print(deadg,"was found dead in the bathhouse.")
if choice == 7:
        print(deadg,"was found stabbed in the chest in their bathroom.")
if choice == 8:
        print(deadg,"was found strangled in the rec room.")
if choice == 9:
        print(deadg,"was found decapitated in the art repository.")
if choice == 10:
        print(deadg,"was found poisoned in the chem lab.")
go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,4)
rel7 = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,3)
rel8 = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(rel7,rel8))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(rel7,rel8))
if reel == 3:
        print("{0} and {1} love eachother.".format(rel7,rel8))
if reel == 4:
        print("{0} and {1} hate eachother.".format(rel7,rel8))
studentlist.append(rel7)
studentlist.append(rel8)
go = input("\n \n \nPress Enter to continue...\n \n \n")
print("\n4 remaining students")
for item in studentlist:
        print(item)

print("\n12 deceased students")
for item in deadlist:
        print(item)
        

go = input("\n \n \nPress Enter to continue...\n \n \n")
print("\nThe remaining students began an investigation.")
go = input("\n \n \nPress Enter to continue...\n \n \n")
trial = random.randint(1,25)
killer = random.randint(1,4)
blackenedg = studentlist[killer-1]
if trial == 1:
        tri = random.randint(1,5)
        if tri == 1:
                print("\nThe stuents voted incorrectly- they were so sure they found the killer. The whole class was gassed in the courtroom. {0} had a gas mask that they wore as they left Hope's Peak and their dying classmates behind.".format(blackenedg))
        if tri == 2:
                print("\nNo matter how hard the class tried they couldnt come to a verdict. {0} was put into a glass elevator that left Hope's Peak as the courtroom filled with water.".format(blackenedg))
        if tri == 3:
                print("\nThe students voted who they thought was the killer. It was a close vote but the class lost by one vote. Because of that, {0} walked out of Hope's Peak as it burned down to the ground.".format(blackenedg))
        if tri == 4:
                print("\nThe killer was not voted guilty since the class did not vote. {0} walked out of Hope's Peak as the courtroom filled with acid.".format(blackenedg))
        if tri == 5:
                print("\n{0} managed to avoid being voted. They left Hope's Peak as it exploded, killing all the students inside.".format(blackenedg))
        print("\n{0} survived".format(blackenedg))
        del studentlist[killer-1]
        deadlist = deadlist + studentlist
        studentlist = blackenedg
        surv = open("surv.txt","a",newline = "")
        writer = csv.writer(surv)
        writer.writerow([studentlist])
        surv.close()
        dead = open("dead.txt","a",newline="")
        write= csv.writer(dead)
        write.writerow([deadlist])
        dead.close()
        exit()
else:
        execu = random.randint(1,9)
        execution = punish[execu-1]
        del punish[execu-1]
        print(execution.format(blackenedg))
        del studentlist[killer-1]
        deadlist = [deada,blackeneda,deadb,blackenedb,deadc,deadd,blackenedc,deade,deadf,blackenedf,deadg,blackenedg]
go = input("\n \n \nPress Enter to continue...\n \n \n")


reel = random.randint(1,4)
rel = random.randint(1,3)
rel9 = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,2)
rel10 = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(rel9,rel10))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(rel9,rel10))
if reel == 3:
        print("{0} and {1} love eachother.".format(rel9,rel10))
if reel == 4:
        print("{0} and {1} hate eachother.".format(rel9,rel10))
studentlist.append(rel9)
studentlist.append(rel10)
go = input("\n \n \nPress Enter to continue...\n \n \n")
print("\n3 remaining students")
for item in studentlist:
        print(item)

print("\n13 deceased students")
for item in deadlist:
        print(item)








go = input("\n \n \nPress Enter to continue...\n \n \n")

time.sleep(1)





print("\nChapter 7\n ")












eve = random.randint(1,6)
if eve == 1:
        print("The whole class did a swimming race.")
if eve == 2:
        print("The whole class explored Hope's Peak.")
if eve == 3:
        print("The whole class chatted in the garden.")
if eve == 4:
        print("The whole class dined together in the dining hall.")
if eve == 5:
        print("The whole class plotted to kill Monokuma.")
if eve == 6:
        print("The whole class had a competition in the dojo.")





go = input("\n \n \nPress Enter to continue...\n \n \n")



mot = random.randint(1,13)
motive = motlist[mot-1]
print(motive)
del motlist[mot-1]
go = input("\n \n \nPress Enter to continue...\n \n \n")
reel = random.randint(1,4)
rel = random.randint(1,3)
rel11 = studentlist[rel-1]
del studentlist[rel-1]
rel = random.randint(1,2)
rel12 = studentlist[rel-1]
del studentlist[rel-1]
if reel == 1:
        print("{0} and {1} like eachother.".format(rel11,rel12))
if reel == 2:
        print("{0} and {1} dislike eachother.".format(rel11,rel12))
if reel == 3:
        print("{0} and {1} love eachother.".format(rel11,rel12))
if reel == 4:
        print("{0} and {1} hate eachother.".format(rel11,rel12))
studentlist.append(rel11)
studentlist.append(rel12)
go = input("\n \n \nPress Enter to continue...\n \n \n")

print("With only three remaining students, the Killing Game cannot go on!")
print("Monokuma issues a final class trial...")
trial = 0
trial = random.randint(1,10)
go = input("\n \n \nPress Enter to continue...\n \n \n")
if trial == 1:
  print("\nThe class refused to vote. They refused to choose between hope and despair, between freedom and continuing; they realised that by voting, the killing game will happen again. As a result they were all punished\n\nNo survivors.")
  deadlist = deadlist + studentlist
  surv = open("surv.txt","a",newline = "")
  writer = csv.writer(surv)
  writer.writerow(["no survivors"])
  surv.close()
  dead = open("dead.txt","a",newline="")
  write= csv.writer(dead)
  write.writerow([deadlist])
  dead.close()
  exit()
elif trial == 2:
  print("\nThey voted despair and for the game to continue.\nAs time went by, the three remaining students learnt to live with each other.")
  go = input("\n \n \nPress Enter to end...\n \n \n")
  exit()
else:
  kill = random.randint(1,3)
  deadxa = studentlist[kill-1]
  deadlist = [deada,blackeneda,deadb,blackenedb,deadc,deadd,blackenedc,deade,deadf,deadxa]
  del studentlist[kill-1]
  print("\nThey voted hope and {0} was executed for being the mastermind. They students left Hope's Peak and ventured into the new world outside...".format(deadxa))
  print("\n2 students survived:")
  for item in studentlist:
    print(item)
  surv = open("surv.txt","a",newline = "")
  writer = csv.writer(surv)
  writer.writerow([studentlist])
  surv.close()
  dead = open("dead.txt","a",newline="")
  write= csv.writer(dead)
  write.writerow([deadlist])
  dead.close()
  exit()





