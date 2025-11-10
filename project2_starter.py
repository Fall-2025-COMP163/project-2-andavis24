"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Ajani Davis
Date: 11 - 10 - 2025

AI Usage: Used AI for helpful debugging and creation of the README.md file
"""

import random

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """Base class for all characters."""
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        """Basic attack using strength for damage."""
        damage = self.strength
        print(f"{self.name} attacks {target.name}. They did {damage} damage.")
        target.take_damage(damage)
        
    def take_damage(self, damage):
        """Reduce health, never below 0."""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health left: {self.health}") 
        
    def display_stats(self):
        """Show basic stats."""
        print(f"--- {self.name}'s Stats ---")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")


class Player(Character):
    """Base class for all player characters."""
    
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def display_stats(self):
        """Override to show player-specific info."""
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}")

    def gain_experience(self, amount):
        """Gain experience and level up automatically."""
        self.experience += amount
        print(f"{self.name} gains {amount} XP!")
        if self.experience >= 100:
            self.level += 1
            self.experience = 0
            self.health += 10
            self.strength += 2
            print(f"{self.name} leveled up to Level {self.level}!")

    def equip_weapon(self, weapon):
        """Equip a weapon (composition in action)."""
        self.weapon = weapon
        print(f"{self.name} equips the {weapon.name}! (+{weapon.damage_bonus} damage bonus)")


class Warrior(Player):
    """Warrior class - strong physical fighter."""
    
    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 5)
        
    def attack(self, target):
        """Warrior's basic attack with weapon bonus if equipped."""
        weapon_bonus = self.weapon.damage_bonus if hasattr(self, "weapon") else 0
        damage = self.strength + 5 + weapon_bonus
        weapon_name = self.weapon.name if hasattr(self, "weapon") else "bare hands"
        print(f"{self.name} slashes {target.name} with {weapon_name} for {damage} damage")
        target.take_damage(damage)
        
    def power_strike(self, target):
        """Powerful warrior ability that deals double strength damage."""
        damage = self.strength * 2
        print(f"{self.name} uses power strike on {target.name} for {damage} damage")
        target.take_damage(damage)
        self.gain_experience(50)


class Mage(Player):
    """Mage class - magical spellcaster."""
    
    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)
        
    def attack(self, target):
        """Attack using magic power and weapon bonus if equipped."""
        weapon_bonus = self.weapon.damage_bonus if hasattr(self, "weapon") else 0
        damage = self.magic + weapon_bonus
        weapon_name = self.weapon.name if hasattr(self, "weapon") else "magic energy"
        print(f"{self.name} casts a spell using {weapon_name} on {target.name} for {damage} damage")
        target.take_damage(damage)
        
    def fireball(self, target):
        """Mage's special ability - boosted magic attack."""
        damage = self.magic + 10
        print(f"{self.name} shoots a fireball {target.name} for {damage} damage")
        target.take_damage(damage)
        self.gain_experience(50)


class Rogue(Player):
    """Rogue class - quick and sneaky fighter."""
    
    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 10)
        
    def attack(self, target):
        """Rogue attack with critical hit chance and weapon bonus."""
        weapon_bonus = self.weapon.damage_bonus if hasattr(self, "weapon") else 0
        crit_chance = random.randint(1, 10)
        if crit_chance <= 3:
            damage = (self.strength * 2) + weapon_bonus
            print(f"{self.name} lands a CRITICAL hit on {target.name} for {damage} damage")
        else:
            damage = self.strength + weapon_bonus
            print(f"{self.name} swiftly attacks {target.name} for {damage} damage")
        target.take_damage(damage)
        
    def sneak_attack(self, target):
        """Guaranteed critical hit with possible weapon bonus."""
        weapon_bonus = self.weapon.damage_bonus if hasattr(self, "weapon") else 0
        damage = (self.strength * 2) + weapon_bonus
        print(f"{self.name} performs a sneak attack on {target.name}, dealing {damage} damage!")
        target.take_damage(damage)
        self.gain_experience(50)


class Weapon:
    """Weapon class to demonstrate composition."""
    
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        print(f"Weapon: {self.name}, Damage Bonus: {self.damage_bonus}")

# ============================================================================
# MAIN PROGRAM FOR TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    # Create characters
    warrior = Warrior("Leon")
    mage = Mage("Zara")
    rogue = Rogue("Kai")

    # Show stats
    print("\n--- Character Stats ---")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Create weapons and equip them (composition in action)
    print("\n--- Equipping Weapons ---")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)

    warrior.equip_weapon(sword)
    mage.equip_weapon(staff)
    rogue.equip_weapon(dagger)

    # Dummy target
    dummy = Character("Target Dummy", 100, 0, 0)

    # Test polymorphism (same method, different behavior)
    print("\n--- Testing Normal Attacks ---")
    warrior.attack(dummy)
    dummy.health = 100
    mage.attack(dummy)
    dummy.health = 100
    rogue.attack(dummy)

    # Test special abilities + level up system
    print("\n--- Testing Special Abilities ---")
    warrior.power_strike(dummy)
    mage.fireball(dummy)
    rogue.sneak_attack(dummy)

    # Test weapon composition info
    print("\n--- Testing Weapons ---")
    sword.display_info()
    staff.display_info()
    dagger.display_info()

    # Bonus: Battle demo
    print("\n⚔️ Demo Battle: Warrior vs Mage ---")
    battle = SimpleBattle(warrior, mage)
    battle.fight()

    print("\n✅ Testing complete! All features demonstrated successfully.")
