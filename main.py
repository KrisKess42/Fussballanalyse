#Stand: 20.09.2025 [12:19 Uhr]


"""
Hauptprogramm für das Fußball-Tippspiel
"""
# Klasse zur Erstellung von Teilnehmern:

class Teilnehmer:
    def __init__(self, name, alter, email, nummer):
        self.name = name
        self.alter = alter
        self.email = email
        self.nummer = None  # optional, eigene ID
    
    @classmethod
    def neu_anlegen(cls):
        name = input("Name: ")
        alter = int(input("Alter: "))
        email = input("E-Mail: ")
        nummer = len(teilnehmer) + 1  # Nummer = nächster Index in der Liste
        t = cls(name, alter, email, nummer)
        teilnehmer.append(t)  # gleich zur Liste hinzufügen
        return t
   
    # Instanzmethode zum Ändern des Namens
    def name_aendern(self):
        self.name = input("Gib bitte den neuen Namen ein!")

partien = [
    {"heim": "Eintracht Frankfurt", "ausw": "Union Berlin"},
    {"heim": "Bayern München", "ausw": "Borussia Dortmund"},
    {"heim": "RB Leipzig", "ausw": "VfL Wolfsburg"}
]

class Tipp:
    def __init__(self, index, datum, teilnehmernummer):
        self.index = index
        self.datum = datum
        self.teilnehmernummer = teilnehmernummer
        # kopiere die Partien für diese Instanz, um eigene Tore einzugeben
        self.spiele = [dict(spiel, tore_heim=None, tore_ausw=None) for spiel in partien]

    def tippen(self):
        print(f"Tipp {self.index} für Teilnehmer {self.teilnehmernummer}")
        for s in self.spiele:
            s['tore_heim'] = int(input(f"Tore {s['heim']}: "))
            s['tore_ausw'] = int(input(f"Tore {s['ausw']}: "))

    def anzeigen(self):
        print(f"Tipp {self.index} vom {self.datum} für Teilnehmer {self.teilnehmernummer}")
        for s in self.spiele:
            print(f"{s['heim']} {s['tore_heim']} : {s['tore_ausw']} {s['ausw']}")

teilnehmer = []
tippper = Teilnehmer.neu_anlegen()


tipp1 = Tipp(index=1, datum="2025-09-20", teilnehmernummer=1)

# Teilnehmer gibt seine Tipps ein
tipp1.tippen()

# Tipp anzeigen
tipp1.anzeigen()
