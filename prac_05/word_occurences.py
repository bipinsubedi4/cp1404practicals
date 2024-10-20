"""
Word Occurrences Program

Time Estimate: 25-30  minutes
Actual : 34 minutes
"""

def main():
    """Main function to count word occurrences and print results aligned."""
    text = input("Text: ")
    word_counts = {}

    # Split the input text into words and count occurrences
    words = text.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Get the longest word for formatting alignment
    longest_word = max(len(word) for word in word_counts)

    # Sort the dictionary by word and print the results in aligned format
    for word in sorted(word_counts):
        print(f"{word:{longest_word}} : {word_counts[word]}")

if __name__ == "__main__":
    main()
