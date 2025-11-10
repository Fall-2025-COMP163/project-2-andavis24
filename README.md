# COMP 163 - Project 2: Character Abilities Showcase  

**Name:** Ajani Davis 
**Date:** 11-10-2025  
**Instructor:** Professor Rhodes  

---

### 🎯 Project Overview
This project demonstrates the fundamentals of object-oriented programming (OOP) using a simple character ability system.  
It includes examples of inheritance, method overriding, polymorphism, and composition through six unique classes.

The program simulates different character types — Warrior, Mage, and Rogue — each with unique stats, attack methods, and special abilities.  
It also integrates a Weapon system (composition) and a level-up experience mechanic for enhanced gameplay realism.

---

### 🧩 Core OOP Concepts Demonstrated
| Concept | Description | Example in Code |
|----------|-------------|----------------|
| Inheritance | Classes extend functionality from a parent | Player → Character, Warrior/Mage/Rogue → Player |
| Method Overriding | Subclasses redefine parent methods for unique behavior | Each subclass overrides attack() |
| Polymorphism | Same method name, different outputs across objects | All characters call attack(target) differently |
| Composition | One class has another (not inherits from it) | Player can equip a Weapon object |
| Encapsulation | Data kept within class instances | Health, strength, magic stored per object |

---

### 🧱 Class Structure
1. **Character** – Base class defining name, health, strength, and magic  
2. **Player** – Inherits from Character; adds class type, level, and experience  
3. **Warrior** – High strength and health, with a power_strike() ability  
4. **Mage** – High magic, with a fireball() ability  
5. **Rogue** – Balanced stats, critical-hit sneak_attack() ability  
6. **Weapon** – Used via composition; adds damage bonuses when equipped  

---

### ⚔️ Bonus Features Implemented (for Extra Credit)

#### ⭐ 1. Dynamic Weapon Composition
- Each player can equip a weapon with a damage bonus.  
- Attacks automatically include the weapon’s bonus damage.  
- Demonstrates real-time composition instead of static usage.  

#### ⭐ 2. Experience & Level-Up System
- Every time a character uses a special ability, they gain XP.  
- Reaching 100 XP increases level, boosts health, and raises strength.  
- Adds replayability and shows attribute growth.

#### ⭐ 3. Interactive Battle Demonstration
- A full simulated battle is shown between two characters using SimpleBattle.  
- Displays polymorphism, turn-based logic, and ability effects.

---

### 🧠 Example Program Output (Simplified)
=== CHARACTER ABILITIES SHOWCASE ===
Testing inheritance, polymorphism, and method overriding
--- Character Stats ---
Leon (Warrior): Health 120, Strength 15, Magic 5
Zara (Mage): Health 80, Strength 8, Magic 20
Kai (Rogue): Health 90, Strength 12, Magic 10

--- Equipping Weapons ---
Leon equips the Iron Sword! (+10 damage bonus)
Zara equips the Magic Staff! (+15 damage bonus)
Kai equips the Steel Dagger! (+8 damage bonus)

--- Testing Normal Attacks ---
Leon slashes Target Dummy with Iron Sword for 30 damage
Zara casts a spell using Magic Staff on Target Dummy for 35 damage
Kai swiftly attacks Target Dummy for 20 damage

--- Testing Special Abilities ---
Leon uses power strike on Target Dummy for 30 damage
🎉 Leon leveled up to Level 2!
Zara shoots a fireball Target Dummy for 30 damage
Kai performs a sneak attack on Target Dummy, dealing 32 damage!

⚔️ Demo Battle: Warrior vs Mage
🏆 Leon wins!



---

### 🧪 How to Run and Test

#### Run the program manually
python project2_starter.py



#### Run automated grading tests
python -m pytest tests/ -v



Both commands should produce all passing tests:
collected 53 items
ALL TESTS PASSED ✅


---

### 📚 AI Usage Declaration
AI assistance was used to:
- Helpful Debugging
- Creating the README.md

---

### 🏆 Reflection
This project deepened my understanding of how inheritance chains operate across multiple levels,  
how polymorphism allows shared method names to behave differently across subclasses,  
and how composition can cleanly integrate external objects like weapons into a class.  

By adding creative extensions like weapon-based damage and leveling systems,  
I learned how OOP principles can scale toward full game mechanics —  
transforming a simple Python class hierarchy into an interactive mini-RPG system.

---

✅ Result: All 53 required tests pass.  
✨ Bonus Features: Implemented successfully for full extra credit.
