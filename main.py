#!/usr/bin/env python3
"""
Hauptprogramm für das Fußball-Tippspiel
"""

from data import teams, season_matches
from menu import show_menu, tipper_list, tipps_list

def main():
    print("=== Fußball-Tippspiel ===")
    print("Willkommen zum Fußball-Tippspiel!")
    
    # Starte das Hauptmenü
    show_menu()

if __name__ == "__main__":
    main()
# TODO:
# - Tipper hinzufügen
# - Tipper löschen
# - Tipper bearbeiten
# - Tipper anzeigen
# - Tipper sortieren
# - Tipper filtern
# - Tipper exportieren
# - Tipper importieren