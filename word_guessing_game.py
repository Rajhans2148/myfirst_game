import random as r
print("welcom to word guessing game!")
print("arrange the word in a correct meaning")
print("let's enjjoy the game")
def start():
    list=["java","ruby","python","html","javascript","game",]
    item=r.choice(list)
    return step2(item)
def step2(item):
    l=list(item)
    r.shuffle(l)
    string="".join(l)
    print(string)
    return step3(item,0)

def step3(item,i):
    n=input("arrange the jumbled word = ")
    if n==item:
        print("you win!")
        n2=input("for continue playing? (yes/no) = ")
        if n2!="yes":
            print("Thankyou for Playing ")
        else:
            return start()
    else:
        return step4(item,i)
def step4(item,i):
    
    if i>=4:
        print("you have no more chance left for playing")
        print("better luck for next time")
        print("thankyou")
    else:
        print(f"you have {4-i} chance left to play a game ")
        return step3(item,i+1)
start()