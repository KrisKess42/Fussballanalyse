def get_valid_number(prompt, min_value=0, max_value=999):
    """Hilfsfunktion für sichere Zahlen-Eingabe"""
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                print(f"Fehler: Zahl muss zwischen {min_value} und {max_value} liegen!")
                continue
            return value
        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Zahl ein!")
        except KeyboardInterrupt:
            print("\nVorgang abgebrochen.")
            return None
