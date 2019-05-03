deci = ['a','b','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',' ']
word = ""
preword = ""
digi = 0
lngthofwrd = 1

lenth = input("how long would you like the generated word to be?\n")
wordlength = int(lenth)
f= open("wgl.txt","w+")


def main():
    global digi
    while (lngthofwrd < wordlength + 1):
        for i in range(36):
            preword = deci[digi]
            f.write("word \n")
            word = preword
            digi = digi + 1
        lngthofwrd = lngthofwrd + 1
        

        
    f.close() 
        

main()
