from bs4 import BeautifulSoup
import mechanicalsoup
import time
import re
import sys

def writeln (f, s):
    f.write(s + "\n")
    
def submit_application (course_nr, user_id, password):
    br = mechanicalsoup.StatefulBrowser()
    # br.set_handle_robots(False)
    br.open("https://www.szsb.uni-saarland.de/sprachkurse/Anmelden.asp?KursNr={0}".format(course_nr))
    br.select_form('form[name="FrontPage_Form1"]')
    br["BenutzerID"] = user_id
    br["Kennwort"] = password
    res = br.submit_selected()

    # the html says it's latin1 but actually it's utf-8 encoded
    soup = BeautifulSoup(res.content, "lxml", from_encoding="utf-8")
    return soup

def find_string(soup, string):
    return soup.find(string=re.compile(string, re.IGNORECASE))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("szsbot kursnummer benutzer_id passwort")
        print("Example: szsbot SZJPS1804 72913 passw0rd")
        print("Man findet die Kursnummer auf der jeweiligen Seite des Kurses.")
        sys.exit(1)

    strange = False
    course_nr = sys.argv[1]
    
    while True:
        soup = submit_application(*sys.argv[1:])

        with open(f"/home/adrian/programming/szsbot/szsbot{course_nr}.log", "a") as f:
            # if we are too early try again in 10 seconds
            if find_string(soup, u'Frühanmeldungen nicht möglich!'):
                writeln(f, "Zu frueh...")
            # Checking for Erfolgreich has worked so far
            elif find_string(soup, "Erfolgreich"):
                writeln(f, "ERFOLGREICH!")
                writeln(f, soup.text)
                break
            elif find_string(soup, "Anmeldung Fehlgeschlagen") \
                 and soup.find("form", attrs={"name":"KursBearbeiten"}) \
                 and find_string(soup.find("form", attrs={"name":"KursBearbeiten"}), course_nr):
                writeln(f, "Bin wohl schon angemeldet.")
                writeln(f, soup.text)
                break
            else:
                writeln(f, "What happened?")
                if not strange:
                    writeln(f, soup.text)
                strange = True

        time.sleep(10)


                
        
    


