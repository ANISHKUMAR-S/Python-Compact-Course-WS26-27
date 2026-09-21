if __name__ == '__main__':
    Integer = 20
    Float = 90.56
    String2 = "100"
    Boolean = True

    print(f"An integer {Integer} is converted to a Float: {float(Integer)}")
    print(f"A float {Float} is converted to an integer: {int(Float)}")
    print(f"An integer {Integer} is converted to a string: {str(Integer)}")  # noqa: RUF010
    print(f"A string containing number {String2} is converted to an integer: {int(String2)}")
    print(f"An integer {Integer} is converted to a boolean: {bool(Integer)}")