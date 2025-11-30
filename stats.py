def count_words(file_c):
    file_after_split=file_c.split()
    print(f"Found {len(file_after_split)} total words")
    return len(file_after_split)

def count_chars(text_from_book):
    text_from_book = text_from_book.lower()
    new_dict={}
    for char in text_from_book:
        #if char.isalpha():    
        if char in new_dict:
            new_dict[char] +=1
        else:
            new_dict[char]=1
    #print(new_dict)
    return new_dict

def convert_dict_to_list(dict_t_c):
    char_list=[]
    for b_key,val in dict_t_c.items():
        pair={"char":b_key,"num":val}
        char_list.append(pair)
    char_list.sort(reverse=True, key=get_key)
    for small_dict in char_list:
        if small_dict["char"].isalpha():
            print(f"{small_dict["char"]}: {small_dict["num"]}")
    return char_list

def get_key(di):
    return di["num"]

    