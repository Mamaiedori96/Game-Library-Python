import json


class Joc:
    def __init__(self, nume, gen, ore, status):
        self.nume = nume
        self.gen = gen
        self.ore = ore
        self.status = status

    def afiseaza(self):
        print(f"{self.nume} - {self.gen} - {self.ore} ore - {self.status}")

    def marcheaza_terminat(self):
        self.status = "Terminat"

    def modifica_ore(self, ore_noi):
        self.ore = ore_noi

    def to_dict(self):
        return {
            "nume": self.nume,
            "gen": self.gen,
            "ore": self.ore,
            "status": self.status
        }


jocuri = []


def salveaza_jocuri():
    with open("jocuri.json", "w") as f:
        json.dump([joc.to_dict() for joc in jocuri], f, indent=4)


def incarca_jocuri():
    try:
        with open("jocuri.json", "r") as f:
            jocuri_data = json.load(f)

            for joc_data in jocuri_data:
                joc = Joc(
                    joc_data["nume"],
                    joc_data["gen"],
                    joc_data["ore"],
                    joc_data["status"]
                )

                jocuri.append(joc)

    except (FileNotFoundError, json.JSONDecodeError):
        print("📁 Nu exista date salvate. Se porneste cu o biblioteca goala.")


incarca_jocuri()


while True:
    print("\n--- 🎮 GAME LIBRARY ---")
    print("1. Adauga joc")
    print("2. Vezi jocurile")
    print("3. Marcheaza joc ca terminat")
    print("4. Modifica orele jucate")
    print("5. Sterge joc")
    print("6. Statistici")
    print("7. Iesire")

    alegere = input("👉 Alege o optiune: ").strip()


    if alegere == "1":
        nume = input("Numele jocului: ").strip()
        gen = input("Genul jocului: ").strip()

        while True:
            try:
                ore = int(input("Cate ore ai: ").strip())

                if ore < 0:
                    print("❌ Orele nu pot fi negative!")
                    continue

                break

            except ValueError:
                print("❌ Trebuie sa introduci un numar!")

        status = "Playing"

        joc_nou = Joc(nume, gen, ore, status)
        jocuri.append(joc_nou)

        salveaza_jocuri()

        print("✅ Joc adaugat cu succes!")


    elif alegere == "2":
        if not jocuri:
            print("❌ Nu ai niciun joc in biblioteca.")

        else:
            for joc in jocuri:
                joc.afiseaza()


    elif alegere == "3":
        if not jocuri:
            print("❌ Nu ai niciun joc in biblioteca.")

        else:
            for index, joc in enumerate(jocuri, start=1):
                print(f"{index}. {joc.nume}")

            try:
                alegere_joc = int(input("👉 Alege numarul jocului: "))
                index = alegere_joc - 1

                if 0 <= index < len(jocuri):
                    joc_selectat = jocuri[index]

                    joc_selectat.marcheaza_terminat()
                    salveaza_jocuri()

                    print("✅ Jocul a fost marcat ca terminat!")

                else:
                    print("❌ Joc invalid!")

            except ValueError:
                print("❌ Trebuie sa introduci un numar!")


    elif alegere == "4":
        if not jocuri:
            print("❌ Nu ai niciun joc in biblioteca.")

        else:
            for index, joc in enumerate(jocuri, start=1):
                print(f"{index}. {joc.nume}")

            try:
                alegere_joc = int(input("👉 Alege numarul jocului: "))
                index = alegere_joc - 1

                if 0 <= index < len(jocuri):
                    joc_selectat = jocuri[index]

                    ore_noi = int(input("👉 Introdu numarul nou de ore: "))

                    if ore_noi < 0:
                        print("❌ Orele nu pot fi negative!")

                    else:
                        joc_selectat.modifica_ore(ore_noi)
                        salveaza_jocuri()

                        print("✅ Orele au fost modificate!")

                else:
                    print("❌ Joc invalid!")

            except ValueError:
                print("❌ Trebuie sa introduci un numar!")


    elif alegere == "5":
        if not jocuri:
            print("❌ Nu ai niciun joc in biblioteca.")

        else:
            for index, joc in enumerate(jocuri, start=1):
                print(f"{index}. {joc.nume}")

            try:
                alegere_joc = int(input("👉 Alege numarul jocului: "))
                index = alegere_joc - 1

                if 0 <= index < len(jocuri):
                    joc_sters = jocuri.pop(index)

                    salveaza_jocuri()

                    print(f"✅ Jocul '{joc_sters.nume}' a fost sters!")

                else:
                    print("❌ Joc invalid!")

            except ValueError:
                print("❌ Trebuie sa introduci un numar!")


    elif alegere == "6":
        if not jocuri:
            print("❌ Nu ai niciun joc in biblioteca.")

        else:
            total_ore = sum(joc.ore for joc in jocuri)
            total_jocuri = len(jocuri)
            total_terminat = sum(
                1 for joc in jocuri if joc.status == "Terminat"
            )

            print("\n📊 Statistici:")
            print(f"- Total ore jucate: {total_ore}")
            print(f"- Total jocuri: {total_jocuri}")
            print(f"- Jocuri terminate: {total_terminat}")


    elif alegere == "7":
        print("👋 La revedere!")
        break


    else:
        print("❌ Optiune invalida!")