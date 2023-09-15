############### Blackjack Project #####################
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def pickRandomCards(card):
 _computer=[]
 for i in range(0,2):
  _=random.randint(0,len(cards)-1)
  _computer.append(cards[_])
 return _computer

def add_Scores(cards):
 sum=0
 for i in cards:
  sum+=i
 return sum



user=pickRandomCards(cards)
computer=pickRandomCards(cards)


def draw_Card(user):
 for i in range(0, 1):
  _ = random.randint(0, len(cards) - 1)
  user.append(cards[_])
 return user
fail=True

while fail:
  print(f"User card {user}")
  print(f"Computer card {computer}")
  if add_Scores(user)==add_Scores(computer):
   print("Draw")
   fail = False
  elif add_Scores(user)==21:
   if len(user)==2:
    print("Black Jack")
    fail = False
   else:
    print("You Win")
    fail=False
  elif add_Scores(computer)==21:
   print("You Loose")
   fail=False
  elif add_Scores(user)>21:
   if 11 in user:
    user[user.index(11)]=1
   if 11 not in user:
       print("You Loose")
       fail = False
   yes_or_no=input("Do you want to draw another card?").lower()
   if yes_or_no=='yes':
     _d=draw_Card(user)
     print(_d)
   elif yes_or_no=="no":
     while fail:
       if add_Scores(computer) <= 17:
               fail = False
       draw_Card(computer)
       print("Computer Card:",computer)
       print("User Card:",user)
       print("Computer Score",add_Scores(computer))

       if add_Scores(computer)>21:
           print("You Win")
           fail=False
       elif add_Scores(computer)==add_Scores(user):
           print("Draw")
           fail=False
       elif add_Scores(computer)<add_Scores(user):
           print("You Win")
           fail=False
       else:
           print("You Loose")
           fail=False
  elif fail and add_Scores(user)<21:
     yes_or_no=input("Do you want to draw another card?").lower()
     if yes_or_no=='yes':
      draw_Card(user)
     elif yes_or_no == "no":
         while fail:
             if add_Scores(computer) <= 17:
                 fail=False
             draw_Card(computer)
             print("Computer Card:", computer)
             print("User Card:", user)
             print("Computer Score",add_Scores(computer))
             if add_Scores(computer) > 21:
                 print("You Win")
                 fail = False
             elif add_Scores(computer) == add_Scores(user):
                 print("Draw")
                 fail = False
             elif add_Scores(computer) < add_Scores(user):
                 print("You Win")
                 fail = False
             else:
                 print("You Loose")
                 fail = False



























