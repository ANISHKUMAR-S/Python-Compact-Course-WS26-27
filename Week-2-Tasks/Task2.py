String = str(input("Enter a string of characters including numbers: "))
print("Entered string:", String)
numbers = [int(char) for char in String if char.isdigit()]
print("Extracted numbers:", numbers) if numbers else print("No numbers found")
sum = sum(map(int, numbers))
print("Sum of extracted numbers:", sum)
avg = sum / len(numbers) if numbers else 0
print("Average of extracted numbers:", avg)