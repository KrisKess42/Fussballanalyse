from classes import Tipper, Tipp
from utils import get_valid_number
from data import teams, season_matches

# Globale Listen für Tipper und Tipps
tipper_list = []
tipps_list = []

def show_menu():
    """Hauptmenü mit Auswahl zwischen Tipper und Admin"""
    while True:
        print("\n" + "="*50)
        print("           FUSSBALL-TIPPSPIEL")
        print("="*50)
        print("1. Als Tipper spielen")
        print("2. Als Admin Ergebnisse eingeben")
        print("3. Rangliste anzeigen")
        print("4. Programm beenden")
        print("="*50)
        
        choice = get_valid_number("Wähle eine Option (1-4): ", 1, 4)
        if choice is None:
            continue
            
        if choice == 1:
            tipper_mode()
        elif choice == 2:
            admin_mode()
        elif choice == 3:
            show_ranking()
        elif choice == 4:
            print("Auf Wiedersehen!")
            break

def tipper_mode():
    """Tipper-Modus: Tipper erstellen und Tipps eingeben"""
    while True:
        print("\n--- TIPPER-MODUS ---")
        
        # Prüfe ob Tipper existieren
        if len(tipper_list) == 0:
            print("Keine Tipper vorhanden. Erstelle zuerst einen Tipper.")
            create_tipper()
            continue
        
        # Zeige verfügbare Tipper oder erstelle neuen
        print("\nVerfügbare Aktionen:")
        print("1. Neuen Tipper erstellen")
        print("2. Tipps für bestehenden Tipper eingeben")
        print("3. Zurück zum Hauptmenü")
        
        choice = get_valid_number("Wähle Option (1-3): ", 1, 3)
        if choice is None:
            continue
            
        if choice == 1:
            create_tipper()
        elif choice == 2:
            enter_tipp()
        elif choice == 3:
            return

def admin_mode():
    """Admin-Modus: Spieleergebnisse eingeben"""
    print("\n--- ADMIN-MODUS ---")
    print("Hier können Sie die tatsächlichen Spieleergebnisse eingeben.")
    
    # Optional: Passwort-Abfrage
    password = input("Admin-Passwort (Enter für Skip, 'exit' zum Beenden): ")
    if password.lower() == 'exit':
        print("Admin-Modus abgebrochen.")
        return
    if password and password != "admin123":  # Einfaches Beispiel-Passwort
        print("Falsches Passwort!")
        return
    
    eingabe_ergebnis()
    print("Alle Ergebnisse wurden gespeichert!")

def show_ranking():
    """Rangliste anzeigen"""
    while True:
        print("\n--- RANGLISTE ---")
        if len(tipper_list) == 0:
            print("Keine Tipper vorhanden.")
        else:
            # Sortiere nach Punkten (absteigend)
            sorted_tipper = sorted(tipper_list, key=lambda x: x.points, reverse=True)
            
            print("Rang | Name | Punkte")
            print("-" * 20)
            for i, tipper in enumerate(sorted_tipper, 1):
                print(f"{i:3d} | {tipper.name:15s} | {tipper.points:3d}")
        
        print("\n1. Zurück zum Hauptmenü")
        choice = get_valid_number("Wähle Option (1): ", 1, 1)
        if choice == 1:
            return

def create_tipper():
    while True:
        try:
            tipper_name = input("Enter your name (oder 'exit' zum Beenden): ").strip()
            if tipper_name.lower() == 'exit':
                print("Tipper-Erstellung abgebrochen.")
                return
            if not tipper_name:
                print("Fehler: Name darf nicht leer sein!")
                continue
                
            tipper_email = input("Enter your email (oder 'exit' zum Beenden): ").strip()
            if tipper_email.lower() == 'exit':
                print("Tipper-Erstellung abgebrochen.")
                return
            if tipper_email and "@" not in tipper_email:
                print("Fehler: Ungültige E-Mail-Adresse!")
                continue
                
            # Prüfe auf Duplikate
            for existing_tipper in tipper_list:
                if existing_tipper.name.lower() == tipper_name.lower():
                    print("Fehler: Ein Tipper mit diesem Namen existiert bereits!")
                    continue
                    
            tipper_index = len(tipper_list) + 1
            tipper_list.append(Tipper(tipper_index=tipper_index, name=tipper_name, email=tipper_email))
            print(f"Tipper '{tipper_name}' erfolgreich erstellt!")
            break
            
        except KeyboardInterrupt:
            print("\nVorgang abgebrochen.")
            break
        except Exception as e:
            print(f"Unerwarteter Fehler: {e}")

def enter_tipp():
    if len(tipper_list) == 0:
        print("Keine Tipper vorhanden! Erstelle zuerst einen Tipper.")
        return
    
    print("\nVerfügbare Tipper:")
    for tipper in tipper_list:
        print(f"{tipper.tipper_index}. {tipper.name}")
    
    while True:
        try:
            tipper_input = input("Wähle Tipper (Nummer) oder 'exit' zum Beenden: ")
            if tipper_input.lower() == 'exit':
                print("Tipp-Eingabe abgebrochen.")
                return
            tipper_choice = int(tipper_input) - 1
            
            if tipper_choice < 0 or tipper_choice >= len(tipper_list):
                print("Fehler: Ungültige Tipper-Nummer!")
                continue
            break
        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Nummer ein oder 'exit' zum Beenden!")
        except KeyboardInterrupt:
            print("\nVorgang abgebrochen.")
            return
    
    selected_tipper = tipper_list[tipper_choice]
    
    print(f"\nTipps für {selected_tipper.name}:")
    print("(Gib 'exit' ein, um die Tipp-Eingabe abzubrechen)")
    
    for match in season_matches:
        print(f"\nSpiel {match.match_index}: {match.team_home.clubname} vs. {match.team_away.clubname}")
        
        # Exit-Option für Heimtore
        tipp_home_input = input(f"Tipp für {match.team_home.clubname} (oder 'exit' zum Beenden): ")
        if tipp_home_input.lower() == 'exit':
            print("Tipp-Eingabe abgebrochen.")
            return
        try:
            tipp_home = int(tipp_home_input)
        except ValueError:
            print("Ungültige Eingabe! Bitte eine Zahl eingeben oder 'exit' zum Beenden.")
            continue
            
        # Exit-Option für Auswärtstore
        tipp_away_input = input(f"Tipp für {match.team_away.clubname} (oder 'exit' zum Beenden): ")
        if tipp_away_input.lower() == 'exit':
            print("Tipp-Eingabe abgebrochen.")
            return
        try:
            tipp_away = int(tipp_away_input)
        except ValueError:
            print("Ungültige Eingabe! Bitte eine Zahl eingeben oder 'exit' zum Beenden.")
            continue
        
        tipp = Tipp(
            tipper=selected_tipper,
            match=match,
            tipp_goals_home=tipp_home,
            tipp_goals_away=tipp_away
        )
        tipps_list.append(tipp)
    
    print(f"Alle Tipps für {selected_tipper.name} wurden gespeichert!")
    
    # Rückfrage für weitere Aktionen
    while True:
        print("\nWas möchten Sie als nächstes tun?")
        print("1. Weitere Tipps eingeben")
        print("2. Zurück zum Tipper-Menü")
        print("3. Programm beenden")
        
        choice_input = input("Wähle Option (1-3) oder 'exit' zum Beenden: ")
        if choice_input.lower() == 'exit':
            print("Programm wird beendet.")
            exit()
        try:
            choice = int(choice_input)
            if choice == 1:
                # Rekursiver Aufruf für weitere Tipps
                enter_tipp()
                return
            elif choice == 2:
                return
            elif choice == 3:
                print("Programm wird beendet.")
                exit()
            else:
                print("Fehler: Ungültige Option! Bitte 1, 2 oder 3 wählen.")
        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Zahl ein oder 'exit' zum Beenden!")

def eingabe_ergebnis():
    print("(Gib 'exit' ein, um die Ergebnis-Eingabe abzubrechen)")
    
    for match in season_matches:
        print("Match No. ", match.match_index, " --> ", match.team_home.clubname, " vs. ", match.team_away.clubname)
        
        # Exit-Option für Heimtore
        goals_home_input = input("Goals for " + match.team_home.clubname + " (oder 'exit' zum Beenden): ")
        if goals_home_input.lower() == 'exit':
            print("Ergebnis-Eingabe abgebrochen.")
            return
        try:
            goals_home = int(goals_home_input)
        except ValueError:
            print("Ungültige Eingabe! Bitte eine Zahl eingeben oder 'exit' zum Beenden.")
            continue
            
        # Exit-Option für Auswärtstore
        goals_away_input = input("Goals for " + match.team_away.clubname + " (oder 'exit' zum Beenden): ")
        if goals_away_input.lower() == 'exit':
            print("Ergebnis-Eingabe abgebrochen.")
            return
        try:
            goals_away = int(goals_away_input)
        except ValueError:
            print("Ungültige Eingabe! Bitte eine Zahl eingeben oder 'exit' zum Beenden.")
            continue
            
        match.goals_home = goals_home
        match.goals_away = goals_away
