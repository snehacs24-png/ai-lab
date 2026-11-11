
# First Order Logic - Forward Chaining with User Input

# Getting input from user
person = input("Enter the person's name: ")
country = input("Enter the country name: ")
weapon = input("Enter the weapon name: ")
nationality = input("Enter nationality: ")
enemy = input("Is the country an enemy of America? (yes/no): ")

# Knowledge Base
facts = set()

# Initial facts
facts.add(("American", person))
facts.add(("Missile", weapon))
facts.add(("Owns", country, weapon))

if enemy.lower() == "yes":
    facts.add(("Enemy", country, "America"))

# Forward Chaining
def forward_chaining(facts):

    new_fact = True

    while new_fact:
        new_fact = False

        # Rule 1: Enemy -> Hostile
        for f in list(facts):
            if f[0] == "Enemy":
                result = ("Hostile", f[1])
                if result not in facts:
                    facts.add(result)
                    print("Inferred:", result)
                    new_fact = True

        # Rule 2: Missile -> Weapon
        for f in list(facts):
            if f[0] == "Missile":
                result = ("Weapon", f[1])
                if result not in facts:
                    facts.add(result)
                    print("Inferred:", result)
                    new_fact = True

        # Rule 3: Missiles owned by country
        # were sold by the person
        for f in list(facts):
            if f[0] == "Missile":
                m = f[1]
                if ("Owns", country, m) in facts:
                    result = ("Sells", person, m, country)
                    if result not in facts:
                        facts.add(result)
                        print("Inferred:", result)
                        new_fact = True

        # Rule 4: American selling weapons to hostile
        # country is a criminal
        if ("American", person) in facts:

            for f in list(facts):
                if f[0] == "Weapon":
                    w = f[1]

                    for s in list(facts):
                        if (s[0] == "Sells" and
                            s[1] == person and s[2] == w):

                            c = s[3]

                            if ("Hostile", c) in facts:
                                result = ("Criminal", person)

                                if result not in facts:
                                    facts.add(result)
                                    print("Inferred:", result)
                                    new_fact = True

    return facts


# Execute
final_facts = forward_chaining(facts)

# Check Goal
print("\nFinal Result:")

if ("Criminal", person) in final_facts:
    print(person, "is Criminal")
else:
    print(person, "is NOT proved to be Criminal")
