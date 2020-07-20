import wikipedia
import webbrowser

def wiki():
    wikipage=wikipedia.random(1)
    wikiload=wikipedia.page(wikipage)
    s=wikipedia.summary(wikipage)
    url=wikiload.url
    print("\n\nArticle name: {} \n".format(wikipage))

    choose=input("Are you okay with {}? (y/n/q):".format(wikipage)).lower().strip()
    if(choose=='y' or choose=='yes'):
        print(".........................Summary............................\n")
        print(s)
        it=input("Do you want to see it in webpage? y/n:")
        if(it=='y' or choose=='yes'):
            webbrowser.open(url)
        elif(it=='n' or it=='no'):
            wiki()
    elif(choose=='n' or choose=='no'):
        wiki()
    elif(choose=='q' or choose=='quit'):
        exit(0)
wiki()