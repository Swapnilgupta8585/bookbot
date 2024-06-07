def main():

    file_path = "books/frankenstein.txt"
    text = get_file_text(file_path)
    num_words = count_words(text)
    ch_count_dict = count_char(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    print_report(ch_count_dict)
    print("--- End report ---")


def count_words(text):
    words = text.split()
    return len(words)

def get_file_text(path):
    with open(path) as f:
        return f.read()

def count_char(text):
    ch_count = {}
    for word in text:
        for ch in word.lower():
            if ch in ch_count:
                ch_count[ch] += 1
            else:
                ch_count[ch] = 1
    return ch_count

def print_report(ch_dict):

    list_of_dict = dict_to_list_of_dict(ch_dict)
    list_of_dict.sort(reverse=True, key=sort_basis)
    sorted_ch_dict = list_of_dict_sorted_dict(list_of_dict)

    for key in sorted_ch_dict:
        if key.isalpha():
            print(f"The '{key}' character was found {sorted_ch_dict[key]} times")

def sort_basis(dict):
    return dict["num"]

def dict_to_list_of_dict(dict):
    list_of_dict = []
    for key,value in dict.items():
        list_of_dict.append({"ch":key,"num":value})
    return list_of_dict

def list_of_dict_sorted_dict(list_of_dict):
    sorted_ch_dict = {}
    for dict in list_of_dict:
        sorted_ch_dict[dict["ch"]] = dict["num"]
    return sorted_ch_dict

main()


