from stats import get_book_text, get_word_count, get_character_count, split_dict, sort_on
import sys

def main():
	if len(sys.argv) != 2:
		print ("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	filepath = sys.argv[1]
	book_text = get_book_text(filepath)
	num_words = get_word_count(book_text)
	char_count = get_character_count(book_text)
	char_list = split_dict(char_count)
	print ("============ BOOKBOT ============")
	print (f"Analyzing book found at {filepath}...")
	print ("----------- Word Count ----------")
	print (f"Found {num_words} total words")
	print ("--------- Character Count -------")
	for character_dict in char_list:
		char = character_dict["char"]
		count = character_dict["num"]
		if char.isalpha():
			print (f"{char}: {count}")
	print ("============= END ===============")

main()

