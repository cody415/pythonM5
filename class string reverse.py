
class StringReverser:
    def __init__(self, text):
        # Instance variable to store the string
        self.text = text

    def reverse_words(self):
        # Split the string into words
        words = self.text.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join them back into a string
        return " ".join(reversed_words)


# Example usage
sentence1 = StringReverser("Hello world this is Python")
sentence2 = StringReverser("Object oriented programming is fun")

print("Original:", sentence1.text)
print("Reversed:", sentence1.reverse_words())
print("-" * 40)
print("Original:", sentence2.text)
print("Reversed:", sentence2.reverse_words())
