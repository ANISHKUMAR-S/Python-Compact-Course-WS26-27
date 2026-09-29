List_of_strings = []
x = int(input("Enter the number of strings: "))
for i in range(x):
    string = input(f"Enter string {i + 1}: ")
    List_of_strings.append(string)
print("Entered string:", List_of_strings)
List = list(map(list, List_of_strings))
print("List of characters:", List)