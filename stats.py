def get_num_words(text):
    words = text.split()
    return len(words)
def get_char_count(text):
    char_count = {}
    words = text.split()
    for word in words:
        for char in word:
            lowered_char = char.lower()
            if lowered_char in char_count:
                char_count[lowered_char] += 1
            else: char_count[lowered_char] = 1
    return char_count
def sort_on(dict):
    return dict["num"]
def get_sorted_dicts(dict):
    dicts = []
    for key in dict:
        key_value_pairs = {"char":f"{key}","num":dict[key]}
        dicts.append(key_value_pairs)
    dicts.sort(reverse=True,key=sort_on)
    return dicts
    
    
    

        
    

 


