import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        enemy.take_damage(damage)

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print(f"A wild {self.enemy.name} appeared!")
        while self.player.is_alive() and self.enemy.is_alive():
            print(f"{self.player.name} - HP: {self.player.health} | {self.enemy.name} - HP: {self.enemy.health}")
            choice = input("What will you do? (a: attack, r: run): ")
            if choice == "a":
                self.player.attack_enemy(self.enemy)
                if self.enemy.is_alive():
                    self.enemy.attack_enemy(self.player)
            elif choice == "r":
                print("You ran away.")
                break
        if self.player.is_alive():
            print(f"You defeated the {self.enemy.name}!")
        else:
            print(f"You were defeated by the {self.enemy.name}...")

# Example usage:
player = Character("Hero", 100, 20, 10)
enemy = Character("Dragon", 200, 30, 5)

battle = Battle(player, enemy)
battle.start_battle()
