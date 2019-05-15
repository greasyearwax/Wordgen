import random
deci = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',' ']

length = int(input("how long would you like the generated word to be?\n"))
f = open("word.txt","w+")

def main():
    word = ''
    while (len(word) < length):
       word = word + random.choice(deci) 
       f.write(word)
    print(word + '\n')
    f.close() 
main()
