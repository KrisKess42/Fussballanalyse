#Stand: 20.09.2025 [12:19 Uhr]


"""
Hauptprogramm für das Fußball-Tippspiel
"""

class Teilnehmer:
    def __init__(self, name, alter, email):
        self.name = name    
        self.alter = alter
        self.email = email

    @classmethod
    def neu_anlegen(cls):
        name = input("Name: ")
        alter = int(input("Alter: "))
        email = input("E-Mail: ")
        return cls(name, alter, email)  # cls() erzeugt eine neue Instanz
   
    # Instanzmethode zum Ändern des Namens
    def name_aendern(self, neuer_name):
        self.name = neuer_name


t = Teilnehmer.neu_anlegen()

print(t.name)

name_aendern("Enrico")

print(t.name)