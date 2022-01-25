import pyshorteners
print("""
█▀ █░█ █▀█ █▀█ ▀█▀ █▀▀ █▄░█ █▀▀ █▀█
▄█ █▀█ █▄█ █▀▄ ░█░ ██▄ █░▀█ ██▄ █▀▄                      """)
print("""            created by Anon_d46kph4tom""")

link=input(" Enter your link: ")
print("*******************please wait******")
cont=input("press enter to continue:")
shortener=pyshorteners.Shortener()
final=shortener.tinyurl.short(link)
print(" Your url is  :"+final)
