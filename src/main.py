import json
import os
import random
import sys

LEVELS = [
    (0, "Mortal Scribbler"),
    (10, "Seedling Influencer"),
    (30, "Overdramatic Ascendant"),
    (70, "Chapter-Cliffhanger God"),
    (150, "Final-Page Eternal")
]

SAVE_FILE = "save.json"

class Game:
    def __init__(self):
        self.state = {
            "name": "Anonymous Protagonist",
            "qi": 10,
            "aura": 0,
            "followers": 0,
            "cringe": 0,
            "level": 0,
            "ticks": 0
        }

    def save(self):
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2)
        print("[Saved]")

    def load(self):
        if not os.path.exists(SAVE_FILE):
            print("No save found.")
            return
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            self.state = json.load(f)
        print("[Loaded]")

    def show_status(self):
        name = self.state["name"]
        qi = self.state["qi"]
        aura = self.state["aura"]
        followers = self.state["followers"]
        cringe = self.state["cringe"]
        level_name = self.current_level_name()
        print(f"\n{name} — {level_name}")
        print(f"Qi: {qi}  Aura: {aura}  Followers: {followers}  Cringe: {cringe}")

    def current_level_name(self):
        name = LEVELS[self.state["level"]][1]
        return name

    def check_level_up(self):
        current_idx = self.state["level"]
        next_idx = current_idx + 1
        if next_idx < len(LEVELS):
            threshold = LEVELS[next_idx][0]
            if self.state["aura"] >= threshold:
                self.state["level"] = next_idx
                self.state["aura"] = 0
                print(f"\n*** Ascension! You are now {LEVELS[next_idx][1]}! ***")

    def random_event(self):
        if random.random() < 0.2:
            ev = random.choice([self.ev_roast, self.ev_harem, self.ev_ancient_ad, self.ev_rival_edit])
            ev()

    def ev_roast(self):
        loss = random.randint(1, 5)
        self.state["followers"] = max(0, self.state["followers"] - loss)
        self.state["cringe"] += 2
        print("An onlooker posts a scathing thread about your 'technique'. You lose followers and gain public shame.")

    def ev_harem(self):
        gain = random.randint(2, 8)
        self.state["followers"] += gain
        self.state["cringe"] += 3
        print("A mysterious admirer likes your last post. Followers rush in—interpretations vary.")

    def ev_ancient_ad(self):
        found = random.choice(["amulet of plot armor","suspicious supplement","mystery contract"])
        if found == "amulet of plot armor":
            self.state["aura"] += 10
            print("You discover an 'Amulet of Plot Armor'—for a price. Aura surges.")
        else:
            self.state["cringe"] += 5
            print(f"You buy a {found}. Regrets are immediate.")

    def ev_rival_edit(self):
        change = random.randint(1, 4)
        self.state["qi"] = max(0, self.state["qi"] - change)
        print("A rival author edits your reputation. Qi drained by petty critique.")

    def action_meditate(self):
        amt = random.randint(3, 7)
        self.state["qi"] += amt
        self.state["aura"] += random.randint(1, 3)
        print(f"You meditate. Qi +{amt}.")

    def action_drill(self):
        cost = 5
        if self.state["qi"] < cost:
            print("Not enough Qi to endure the drill.")
            return
        self.state["qi"] -= cost
        gain = random.randint(5, 10)
        self.state["aura"] += gain
        print(f"You endure a grueling drill. Aura +{gain}, Qi -{cost}.")

    def action_post(self):
        gain = random.randint(1, 8)
        cringe = random.randint(2, 6)
        self.state["followers"] += gain
        self.state["cringe"] += cringe
        self.state["aura"] += 1
        print(f"You post a dramatic status. Followers +{gain}, Cringe +{cringe}.")

    def action_gamble(self):
        r = random.random()
        if r < 0.2:
            self.state["aura"] += 30
            self.state["followers"] += 20
            print("Plot armor activated: massive surge!")
        elif r < 0.6:
            self.state["cringe"] += 10
            self.state["followers"] += 5
            print("Mediocre success and social embarrassment.")
        else:
            self.state["qi"] = max(0, self.state["qi"] - 8)
            self.state["followers"] = max(0, self.state["followers"] - 10)
            print("Backfires spectacularly. You are memed.")

    def run(self):
        print("Welcome to Absurd Ascension — a parody text simulator.")
        try:
            name = input("Name your protagonist (or press Enter): ").strip()
            if name:
                self.state["name"] = name
            while True:
                self.show_status()
                print("\nChoose an action:")
                print("1) Meditate  2) Drill  3) Post  4) Gamble Fate")
                print("5) Save  6) Load  7) Quit")
                choice = input("> ").strip()
                if choice == "1":
                    self.action_meditate()
                elif choice == "2":
                    self.action_drill()
                elif choice == "3":
                    self.action_post()
                elif choice == "4":
                    self.action_gamble()
                elif choice == "5":
                    self.save()
                elif choice == "6":
                    self.load()
                elif choice == "7":
                    print("Goodbye.")
                    break
                else:
                    print("Invalid choice.")
                self.state["ticks"] += 1
                self.random_event()
                self.check_level_up()
        except KeyboardInterrupt:
            print("\nInterrupted. Goodbye.")

if __name__ == "__main__":
    Game().run()
