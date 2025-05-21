def get_book_text(filepath):
        with open(filepath) as f:
                file_contents = f.read()
        return file_contents

def get_word_count(text):
        num_words = len(text.split())
        return num_words

#character includes spaces and symbols
def get_character_count(text):
	character_dict = {}
	for character in text:
		lower_case_char = character.lower()
		if lower_case_char in character_dict:
			character_dict[lower_case_char] += 1
		else:
			character_dict[lower_case_char] = 1
	return character_dict

def split_dict(character_dict):
	char_list = []
	for char, count in character_dict.items():
		char_entry = {"char": char, "num": count}
		char_list.append(char_entry)
	char_list.sort(reverse=True, key=sort_on)
	return char_list

def sort_on(character_dict):
	return character_dict["num"]

