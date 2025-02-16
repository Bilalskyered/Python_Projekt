
# Funktion, um eine Aufgabe hinzuzufügen
def add_task():
    task = input("Geben Sie eine neue Aufgabe ein: ")  # Benutzer gibt eine neue Aufgabe ein
    with open("todo_list.txt", "a") as file:  # Öffne die Datei im Anhängemodus
        file.write(task + "\n")  # Schreibe die Aufgabe in die Datei
    print("Die Aufgabe wurde hinzugefügt!")  # Bestätigung für den Benutzer

# Funktion, um alle Aufgaben anzuzeigen
def show_tasks():
    try:
        with open("todo_list.txt", "r") as file:  # Öffne die Datei im Lesemodus
            tasks = file.readlines()  # Lese alle Zeilen der Datei
        if tasks:
            print("Ihre Aufgaben sind:")  # Ausgabe der Aufgaben
            for i, task in enumerate(tasks, 1):  # Nummeriere die Aufgaben
                print(f"{i}. {task.strip()}")  # Zeige jede Aufgabe an
        else:
            print("Es gibt keine Aufgaben.")  # Keine Aufgaben vorhanden
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden. Es sind keine Aufgaben vorhanden.")  # Datei nicht gefunden

# Funktion, um eine Aufgabe als erledigt zu markieren
def mark_task_done():
    try:
        with open("todo_list.txt", "r") as file:  # Öffne die Datei im Lesemodus
            tasks = file.readlines()  # Lese alle Zeilen der Datei
        if tasks:
            print("Welche Aufgabe möchten Sie als erledigt markieren?")
            task_number = int(input("Geben Sie die Nummer der Aufgabe ein: "))  # Benutzer gibt die Nummer der Aufgabe ein
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1] = "X " + tasks[task_number - 1].strip() + "\n"  # Markiere die Aufgabe als erledigt
                with open("todo_list.txt", "w") as file:  # Öffne die Datei im Schreibmodus
                    file.writelines(tasks)  # Schreibe die aktualisierten Aufgaben in die Datei
                print("Die Aufgabe wurde als erledigt markiert!")  # Bestätigung für den Benutzer
            else:
                print("Ungültige Aufgabennummer.")  # Ungültige Nummer
        else:
            print("Es gibt keine Aufgaben zum Markieren.")  # Keine Aufgaben vorhanden
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")  # Ungültige Eingabe

# Funktion, um eine erledigte Aufgabe zu löschen
def delete_task():
    try:
        with open("todo_list.txt", "r") as file:  # Öffne die Datei im Lesemodus
            tasks = file.readlines()  # Lese alle Zeilen der Datei
        if tasks:
            print("Welche erledigte Aufgabe möchten Sie löschen?")
            task_number = int(input("Geben Sie die Nummer der Aufgabe ein: "))  # Benutzer gibt die Nummer der Aufgabe ein
            if 1 <= task_number <= len(tasks):
                task = tasks[task_number - 1]
                if task.startswith("X "):  # Überprüfe, ob die Aufgabe erledigt ist
                    tasks.pop(task_number - 1)  # Lösche die Aufgabe
                    with open("todo_list.txt", "w") as file:  # Öffne die Datei im Schreibmodus
                        file.writelines(tasks)  # Schreibe die aktualisierten Aufgaben in die Datei
                    print("Die erledigte Aufgabe wurde gelöscht!")  # Bestätigung für den Benutzer
                else:
                    print("Diese Aufgabe ist noch nicht erledigt.")  # Aufgabe nicht erledigt
            else:
                print("Ungültige Aufgabennummer.")  # Ungültige Nummer
        else:
            print("Es gibt keine Aufgaben zum Löschen.")  # Keine Aufgaben vorhanden
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")  # Ungültige Eingabe

# Funktion für das Menü
def main_menu():
    while True:
        print("\n--- To-Do Liste ---")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe als erledigt markieren")
        print("4. Erledigte Aufgabe löschen")
        print("5. Beenden")
        
        choice = input("Wählen Sie eine Zahl (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl. Wählen Sie eine Zahl von 1 bis 5.")  # Ungültige Auswahl

# Start der Anwendung
if __name__ == "__main__":
    main_menu()