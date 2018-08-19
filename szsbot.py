from bs4 import BeautifulSoup
import mechanicalsoup
import time
import re
import sys

def writeln (f, s):
    f.write(s + "\n")
    
def submitApplication (args):
    course_nr, user_id, password = args

    br = mechanicalsoup.StatefulBrowser()
    # br.set_handle_robots(False)
    br.open("https://www.szsb.uni-saarland.de/sprachkurse/Anmelden.asp?KursNr={0}".format(course_nr))
    br.select_form('form[name="FrontPage_Form1"]')
    br["BenutzerID"] = user_id
    br["Kennwort"] = password
    res = br.submit_selected()

    soup = BeautifulSoup(res.content, "lxml")
    return soup


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("szsbot kursnummer benutzer_id passwort")
        print("Example: szsbot SZJPS1804 72913 passw0rd")
        print("Man findet die Kursnummer auf der jeweiligen Seite des Kurses.")
        sys.exit(1)

    strange = False
    
    while True:
        soup = submitApplication(sys.argv[1:])

        with open("/home/adrian/programming/python/szsbot/szsbot.log", "w") as f:
            # if we are too early try again in 10 seconds
            if soup.find_all(string=re.compile(u'Frühanmeldungen nicht möglich!')):
                writeln(f, "Zu frueh...")
            # Checking for Erfolgreich has worked so far
            elif soup.find_all(string=re.compile("Erfolgreich", re.IGNORECASE)):
                writeln(f, "ERFOLGREICH!")
                writeln(f, soup.text)
                sys.exit(0)
            else:
                writeln(f, "What happened?")
                if not strange:
                    writeln(f, soup.text)
                strange = True

        time.sleep(10)


                
        
    


