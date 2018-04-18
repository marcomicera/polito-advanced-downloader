import os
from polito_web import PolitoWeb

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__=="__main__":
    sess=PolitoWeb()
    sess.setInterval(0, 350)
    sess.setDumpName("crawled.bin")
    sess.setDlFolder("C:\\users\\Luca\\Videos\\video_lezioni")

    print("PoliTo Advanced Downloader - v 0.1.1", end ="\n\n")

    print("Credenziali di accesso per http://didattica.polito.it")
    while not sess.login():
        print("Impossibile effettuare il login, riprovare!")

    sess.checkForUpdates()
    sess.crawl()
    #clear()
    while sess.menu():
        clear()
