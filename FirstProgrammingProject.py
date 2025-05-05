# Simple Programmer Info Entry Program

def print_title(title):
line = "=" * len(title)
print(line)
print(title)
print(line)

def get_user_data():
name = input("Enter name: ")
age = input("Enter age: ")
current_job = input("Enter current job: ")

print("Select programming level:")
levels = ["Beginner", "Intermediate", "Advanced", "Expert"]
for i, level in enumerate(levels, start=1):
print(f"{i}. {level}")
level_choice = int(input("Enter choice (1-4): "))
prog_level = levels[level_choice - 1]

years_exp = input("Enter years of experience: ")
prog_lang = input("Enter programming language: ")

return {
"Name": name,
"Age": age,
"Job": current_job,
"Level": prog_level,
"Experience": years_exp,
"Language": prog_lang
}

def print_data_table(data_list):
print("\n=== Programmer Information Table ===")
headers = ["Name", "Age", "Job", "Level", "Experience", "Language"]
print("{:<15} {:<5} {:<20} {:<15} {:<10} {:<15}".format(*headers))
print("-" * 85)

for data in data_list:
print("{:<15} {:<5} {:<20} {:<15} {:<10} {:<15}".format(
data["Name"], data["Age"], data["Job"], data["Level"], data["Experience"], data["Language"]
))

def main():
title = "Programmer's Info Database Entry"
print_title(title)

data_list = []
while True:
data = get_user_data()
data_list.append(data)

more = input("Add another? (y/n): ").lower()
if more != 'y':
break

print_data_table(data_list)

# Run the program
main()