def sort_by_second_element(List):
    return sorted(List, key=lambda x: x[1])

if __name__ == '__main__':
    First_Elements = []
    Second_Elements = []
    x = int(input("Enter the number of Tuples in Lists: "))
    for i in range(x):
        first_element = int(input(f"Enter element {i + 1} for the first list: "))
        First_Elements.append(first_element)
    for i in range(x):
        second_element = int(input(f"Enter element {i + 1} for the second list: "))
        Second_Elements.append(second_element)
    List = list(zip(First_Elements, Second_Elements))
    print("List:", List)
    sorted_list = sort_by_second_element(List)
    print("Sorted list by second element:", sorted_list)