class LKL:
    def __init__(self):
        self.teams = []

    def is_empty(self):
        return len(self.teams) == 0

    def push(self, team):
        self.teams.append(team)

    def pop(self):
        if not self.is_empty():
            return self.teams.pop()
        raise IndexError("Cannot take a team – list is empty.")

    def size(self):
        return len(self.teams)

    def show(self):
        if self.is_empty():
            print("No LKL teams in the list.")
        else:
            print("LKL teams arranged in a column:")
            for x in self.teams:
                print(f"– {x}")

lkl = LKL()

# Adding 5 teams to the list

lkl.push("Žalgiris")
lkl.push("Rytas")
lkl.push("Lietkabelis")
lkl.push("Neptūnas")
lkl.push("Šiauliai")

# Show the teams

lkl.show()

# Removing 2 teams from the list

print("Removed team:", lkl.pop())
print("Removed team:", lkl.pop())

lkl.push("Wolves")
print(f"After adding Wolves: {lkl.show()}")

# Show the number of teams in the list

print("Number of teams:", lkl.size())

# Show the teams again

lkl.show()
