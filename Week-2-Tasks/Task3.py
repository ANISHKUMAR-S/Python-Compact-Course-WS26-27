def sort_by_data(data):
    return sorted(data, key=lambda x: x['make'].strip())

if __name__ == '__main__':
    n = int(input("Enter number of dictionaries: "))

    data = []
    for i in range(n):
        print(f"\nEnter dictionary {i+1}:")
        make = input("  make: ")
        model = input("  model: ")
        color = input("  color: ")
        data.append({'make': make, 'model': model, 'color': color})

    print("\nOriginal list:")
    print(data)

    print("\nSorted list (by 'make'):")
    print(sort_by_data(data))