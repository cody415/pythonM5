
class RomanConverter:
    def __init__(self, number):
        # Instance variable to store the integer
        self.number = number

    def to_roman(self):
        # Mapping of integers to Roman numerals
        val = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV", "I"]

        num = self.number
        roman_num = ""

        # Loop through values and symbols
        for i in range(len(val)):
            while num >= val[i]:
                roman_num += syms[i]
                num -= val[i]

        return roman_num


# Example usage
number1 = RomanConverter(29)
number2 = RomanConverter(199)

print("Integer:", number1.number, "-> Roman Numeral:", number1.to_roman())
print("Integer:", number2.number, "-> Roman Numeral:", number2.to_roman())
