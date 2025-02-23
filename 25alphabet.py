import pandas

# ------------------------------ MAIN --------------------------

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# ? Create a dictionary in this format:
alphabet_data = pandas.read_csv("resources/Data/25nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

print(alphabet_dict)


def generate_phonetic():
    """
    Create a list of the phonetic code words from a word that the user input.
    """
    word = input("Enter a word: ").upper()
    try:
        output_list = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()  # looping by calling input again after failure
    else:
        print(output_list)


# this can be ignored
def related_note_code():
    """
    This is pandas code for managing dictionaries
    Function only exists to hide the code and reduce clutter
    """
    student_dict = {
        "student": ["Angela", "James", "Lily"],
        "score": [55, 76, 98]
    }

    # Looping through dictionaries:
    for (key, value) in student_dict.items():
        # Access key and value
        print(f"Key: {key}, Value: {value}")

    student_data_frame = pandas.DataFrame(student_dict)

    # Loop through rows of a data frame
    for (index, row) in student_data_frame.iterrows():
        # Access index and row
        print(f"Index: {index}, Student: {row.student}, Score: {row.score}")
