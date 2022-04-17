import discord
import random
import os
from keep_alive import keep_alive
client = discord.Client( )
d=False
d1=False
d2=False
d3=False
d4=False
d5=False
d6=False
iα=12
jα=0
P=0
Q=0
lα=''
c2α=0
pα=0
c1α=0
c11α=1
b1α=0
c=0
y=0
o=0
o1=0
o2=0
s='0'
sc='0'
k=0
a=' '
c1=0
l=[]
l2=[]
l3=[]
l4=[]
sp=0
dic={}
b=''
k1=0
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Games. Don^t DM me'))
    print('We have logged in as {0.user}'.format(client))
    P=13
@client.event
async def on_message(message):
    global d
    global k1
    global c
    global y
    global s
    global sc
    global k
    global a
    global c1
    global d1
    global d2
    global o
    global b
    global o1
    global o2
    global Q
    global d3
    global d4
    global d5
    global d6
    global iα
    global jα
    global c2α
    global c1α
    global c11α
    global b1α
    global lα
    global pα
    global P
    global l2
    global l3
    global l4
    global sp
    global new1
    global p1
    global wrong1
    global count1
    global star1
    global l31
    global z1
    global y1
    global pl1
    global a
    global l111
    global l21
    global word1
    #Games
    if message.content==('#start') and o>1 :
        sc='plesae wait! '+b+' is playing now'
        await message.channel.send(sc)
    if message.content==('#start') and o<1 and P<10 and Q<1:
        d4=True
        o=10
        a=message.author
        b=message.author.name
        await message.channel.send('Choose Game: A)Handcricket B)Guess the number')
    if message.author==a and message.content==('#stop') and o>1 and Q<1 :
        await message.channel.send('ok! ')
        Q=10
        d3=False
        d6=False
    if message.author==a and message.content==('#resume') and o>1 and Q>1 :
        await message.channel.send('resuming......... ')
        Q=0
        d3=True
        d6=True
    if message.author==a and o>1 and Q<1 and P<10:
            await message.delete()
    if d4 and message.author==a and message.content==('B') and P<10 and Q<1:
                           await message.channel.send('Choose digits as d-x,x=no.of digits')
                           d5=True
                           iα=12
                           jα=0
    if message.author==a and d5 and  message.content.startswith('d-') and P<10 and Q<1:
              x=message.content[2:]
              try:
                 c1α=int(x)
                 if c1α<1 or c1α>10:
                     o=c1α+'a'
                 sc='you are playing '+str(c1α)+' digits game , '+message.author.name
                 while iα>=6:
                          kα=random.randint(10**(c1α-1),10**c1α)
                          lα=str(kα)
                          for x in lα:
                              pα=lα.count(x)
                              jα=jα+pα
                          if jα>=c1α+1:
                                         iα=12 
                                         jα=0
                          else :
                                         iα=2
                                         jα=0
                 await message.channel.send(sc)
                 print(lα+' '+b)
              except:
                  await message.channel.send('digits should be integers and should lie in[1,10]')
              if c1α>0 and c1α<11:
                  d6=True
                  c2α=0
                  c11α=0
    if message.author==a and  d5 and d6 and c11α<c1α and P<10 and Q<1:
            o=5
            try:
               m=int(message.content)
               if m<10**(c1α-1) or m>=10**c1α:
                   o=c1+'a'
               dα=str(m)
               jα=0
               for x in dα:
                 pα=dα.count(x)
                 jα=jα+pα
               if jα>=c1α+1:
                   o=c1+'a'
               c11α=0
               b1α=0
               c2α=c2α+1
               for x in dα:
                   for y in lα:
                             x1α=dα.index(x)
                             y1α=lα.index(y)
                             if x==y and x1α==y1α:
                                          c11α=c11α+1
                             if x==y and x1α!=y1α:
                                            b1α=b1α+1
               sc=dα+' Numbers which are right and in correct place :- '+str(c11α)+' Numbers which are right but not in their place :- '+str(b1α)
               await message.channel.send(sc) 
            except:
              if message.content.startswith('d-') or message.content==('#resume') or message.content==('#end') or message.content==('off') or message.content==('on') :
                  pass
              else:
                await message.channel.send('invalid input')
                await message.channel.send(message.content)
    if message.author==a and  d5 and d6 and c11α==c1α:
        sc='You have guessed the number in '+str(c2α)+' chances'
        await message.channel.send(sc)
        d5=False
        d6=False
        o=0
        a=''        
    if d4 and message.author==a and message.content==('A') and P<10 and Q<1:
        d=True
        await message.channel.send('choose wickets as w-x,x=no.of wickets')
        k=0
        c=0
        c1=0
        y=0
        s=''
        sc=''
        k1=0
        o2=0
        d1=False
        d2=False
        d3=False
        d4=False
    if message.author==a and d and  message.content.startswith('w-') and P<10 and Q<1:
              x=message.content[2:]
              try:
                 c1=int(x)
                 if c1<1 or c1>10:
                     o=c1+'a'
                 sc='you are playing '+str(c1)+' wickets game , '+message.author.name
                 await message.channel.send(sc)
                 await message.channel.send('Heads or Tails')
              except:
                  await message.channel.send('wickets should be integers and should lie in[1,10]')
              if c1>0 and c1<11:
                  d1=True
                  k=0
                  c=0
                  y=0
                  s=''
                  sc=''
                  k1=0
                  o2=0
                  d2=False
                  d3=False
    if message.author==a and  d and d1 and P<10 and Q<1:
        if message.content=='Heads' or  message.content=='Tails':
            i=random.randint(1,2)
            if i==1:
                await message.channel.send('You have won the toss')
                await message.channel.send('Bat or Bowl')
                d2 =True
            if i==2:
                await message.channel.send('I have won the toss')
                j=random.randint(1,2)
                d3=True
                if j==1:
                    await message.channel.send('I am batting first')
                    o1=1
                if j==2:
                     await message.channel.send('I am bowling first')
                     o1=3
        if d2 and message.content=='Bat':
            await message.channel.send('You are batting first')
            o1=3
            d3=True
        if d2 and message.content=='Bowl':
            await message.channel.send('You are bowling first')
            o1=1
            d3=True
    if message.author==a and  d and d1 and d3 and o1>2 and c<=c1 and P<10 and Q<1:
            try:
                 m = int(message.content)
                 if o2 >3 and m <11 and m > -1 and k<=k1:
                                   i=random.randint(0,10)
                                   if i==m:
                                       await message.channel.send('it is a wicket')
                                       c=c+1
                                   if m!=0 and i==0:
                                       k=k+m
                                       sc='My score is '+str(k)+' / '+str(c)
                                       await message.channel.send(sc)
                                   if i!=m and i!=0:
                                       k=k+i
                                       sc='My score is '+str(k)+' / '+str(c)
                                       await message.channel.send(sc)
                                   if c==c1 :
                                       await message.channel.send('You have won the game')
                                       sc='Scorecard:-  '+ message.author.name+' - '+str(k1)+' / '+str(c1)+' , Bot- '+str(k)+' / '+str(c1)
                                       await message.channel.send(sc)
                                       await message.channel.send('https://tenor.com/view/crying-sad-raining-gif-3518394')
                                       l.append(sc)
                                       print(l)
                                       k1=0
                                       k=0
                                       a=''
                                       d=False
                                       d1=False
                                       d2=False
                                       o=0
                 if o2 <3 and m <11 and m > -1:
                                   i=random.randint(0,10)
                                   if i==m:
                                       await message.channel.send('it is a wicket')
                                       c=c+1
                                   if i!=0 and m==0:
                                       k=k+i
                                       sc='Your score is '+str(k)+' / '+str(c)
                                       await message.channel.send(sc)
                                   if i!=m and m!=0:
                                       k=k+m
                                       sc='Your score is '+str(k)+' / '+str(c)
                                       await message.channel.send(sc)
                                   if c==c1:
                                       k1=k
                                       o2=5
                                       await message.channel.send('Your batting was finished')     
                                       sc='Your final score was  '+str(k1)
                                       await message.channel.send(sc)
                                       await message.channel.send('My batting has started')
                                       c=0
                                       k=0
                 if o2>3 and k>k1 :
                     await message.channel.send('You have lost the game')
                     sc='Scorecard:-  '+ message.author.name+' - '+str(k1)+' / '+str(c1)+' , Bot- '+str(k)+' / '+str(c)
                     l.append(sc)
                     print(l)
                     await message.channel.send(sc)
                     await message.channel.send('https://cdn.discordapp.com/emojis/766178885213487124.gif?v=1')
                     d=False
                     d1=False
                     d2=False
                     o=0
                     a=''
            except:
                 if message.content=='Heads' or message.content=='Tails' or message.content=='Bat' or message.content=='Bowl' or message.content=='#start' or message.content=='#end' or message.content==('#resume') or message.content==('on')  or message.content==('off'):
                     pass
                 else: 
                      await message.channel.send('invalid input')
                      await message.channel.send(message.content)
    if message.author==a and  d and d1 and d3 and o1<2 and c<=c1 and P<10 and Q<1:
            try:
                 m = int(message.content)
                 if o2 >3 and m <11 and m > -1 and k<=k1:
                                   i=random.randint(0,10)
                                   if i==m:
                                       await message.channel.send('it is a wicket')
                                       c=c+1
                                   if i!=0 and m==0:
                                       k=k+i
                                       sc='Your score is '+str(k)+' / '+str(c)
                                       await message.channel.send(sc)
                                   if i!=m and m!=0:
                                       k=k+m
                                       sc='Your score is '+str(k)+' / '+str(c)
                                       await message.channel.send(sc)
                                   if c==c1 :
                                       await message.channel.send('You have lost the game')
                                       sc='Scorecard:-  '+ message.author.name+' - '+str(k)+' / '+str(c1)+' , Bot- '+str(k1)+' / '+str(c1)
                                       await message.channel.send(sc)
                                       l.append(sc)
                                       await message.channel.send('https://cdn.discordapp.com/emojis/766178885213487124.gif?v=1')
                                       print(l)
                                       k1=0
                                       k=0
                                       d=False
                                       d1=False
                                       d2=False
                                       o=0
                                       a=''
                 if o2 <3 and m <11 and m > -1:
                                   i=random.randint(0,10)
                                   if i==m:
                                       await message.channel.send('it is a wicket')
                                       c=c+1
                                   if m!=0 and i==0:
                                       k=k+m
                                       sc='My score is '+str(k)+' / '+str(c)
                                       await message.channel.send(sc)
                                   if i!=m and i!=0:
                                       k=k+i
                                       sc='My score is '+str(k)+' / '+str(c)
                                       await message.channel.send(sc)
                                   if c==c1 :
                                       k1=k
                                       o2=5
                                       await message.channel.send('My batting was finished')     
                                       sc='My final score was  '+str(k1)
                                       await message.channel.send(sc)
                                       await message.channel.send('Your batting has started')
                                       c=0
                                       k=0
                 if o2>3 and k>k1 :
                     await message.channel.send('You have won the game')
                     sc='Scorecard:-  '+ message.author.name+' - '+str(k)+' / '+str(c)+' , Bot- '+str(k1)+' / '+str(c1)
                     l.append(sc)
                     print(l)
                     await message.channel.send(sc)
                     await message.channel.send('https://tenor.com/view/crying-sad-raining-gif-3518394')
                     d=False
                     d1=False
                     d2=False
                     o=0
                     a=''
            except:
                if message.content=='Heads' or message.content=='Tails' or message.content=='Bat' or message.content=='Bowl' or message.content=='#start' or message.content=='#stop' or message.content==('#resume'):
                     pass
                else:
                 await message.channel.send('invalid input')
                 await message.channel.send(message.content)
    if message.author==a and message.content=='#end' :
        d=False
        d1=False
        d2=False
        d5=False
        d6=False
        o=0
        a=' '
        await message.channel.send('game over')    
    if message.author.name=='player' and message.content.startswith('Your score is'):
              await message.delete()
    if message.author.name=='player' and message.content.startswith('My score is'):
              await message.delete()
    if message.author.name=='player' and message.content.startswith('it is a wicket'):
              await message.delete()
    if message.author.name=='player' and message.content.startswith('invalid input'):
        await message.delete()
    if message.guild == None and   message.author.name!='player':
           P=1
keep_alive()
my_secret = os.environ['TOKEN1']
client.run(my_secret)

