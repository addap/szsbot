# Szsbot

Szsbot is ein kleines Programm, dass sich automatisch und möglichst früh für euch an einem Kurs des Sprachenzentrums der UdS anmeldet.

Dazu gibt man ihm einfach die Kursnummer, SZSB id und Passwort:
```
szsbot SZJPS1804 72913 passw0rd
```

Das Programm läuft bis es eine erfolgreiche Rückmeldung bekommt, andernfalls probiert es die Anfrage in 10 Sekunden erneut.

## Installation

Einfach das git repository klonen.
Ich benutze ein virtualenv namens "env", was in dem szsbot bash script aktiviert wird. 
Die dependencies in der requirements.txt installieren, am besten in das virtualenv.
```
pip install -r requirements.txt
```

## License

Das Programm ist mit der Unlicense unlizensiert. Näheres in UNLICENSE.txt

## Generelles

Ich habe das Programm geschrieben, da die ersten beiden Stufen des Japanisch Kurses wohl immmer hoffnungslos überlaufen sind. Die Anmeldung ist ab 8:00 morgens möglich und schon 1-2 Minuten später ist der Kurs voll. Ich habe es 10 Minuten vorher per cron job starten lassen und konnte dadurch beruhigt länger schlafen.

