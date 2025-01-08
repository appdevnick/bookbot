def main():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
    
    print_report(book_contents)

def count_words(book):
    return len(book.split())

def character_counts(book):
    total_counts = {}
    for char in book.lower():
        if(char in total_counts):
            total_counts[char] += 1
        else:
            total_counts[char] = 0
    
    return total_counts

def print_report(book):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(book)} words found in the document.")
    counts = character_counts(book)
    sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1]))
    for count in sorted_dict.items():
        print(f"The character {count[0]} occurred {count[1]} times.")

main()