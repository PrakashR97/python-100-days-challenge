import os

auction_bid=[
{
    "name":"Prakash",
    "bid":[100]
},
{
        "name": "Angela",
        "bid": []
},
{
    "name":"Emma",
    "bid":[]
}
]


import os



yes_no=True
from art import logo

print(logo)
def max_bid(param):
    _max=0
    for i in param:
        if i>_max:
            _max=i
    return _max

while yes_no:
 print("hi jimmy")
 _name=input("What is your name?").lower()
 _bid=int(input("What's your bid?"))

 for name in auction_bid:
     if name["name"].lower()==_name:
        name["bid"].append(_bid)
        print(f" bid {name['bid']}")
 print(auction_bid)
 type=input("Are there any other bidders? Yes or No").lower()
 kk=[]
 final_bid = {}
 final_bidder_amount=0
 final_bidder_name=""
 if type=='no':
     yes_no=False
     for i in auction_bid:
         k=i["bid"]
         v=max_bid(k)
         if final_bidder_amount<v:
             final_bidder_amount=v
             final_bidder_name=i["name"]
 print(f"The winner is { final_bidder_name} with a bid of {final_bidder_amount}")



