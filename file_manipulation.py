from collections import Counter
import re

def count_word_occurrences(filepath):
    """
    Counts the occurrences of each word in a text file and displays the results
    alphabetically.
    """
    try:
        with open(filepath, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Process text
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()

    if not words:
        print("The file is empty or contains no valid words.")
        return

    word_counts = Counter(words)
    sorted_words = sorted(word_counts.items())

    print("\nWord Occurrences:\n")
    for word, count in sorted_words:
        print(f"{word}: {count}")

if __name__ == "_main_":
    file_path = input("Enter the path to the text file: ").strip()
    count_word_occurrences(file_path)