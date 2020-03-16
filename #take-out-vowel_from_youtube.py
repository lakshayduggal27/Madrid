name = "youtube"
vowel = ("a","e","i","o","u")
get_len = len(name)
start_index = 0
while start_index < get_len:
    if name[start_index] in vowel:
        print("vowel", name[start_index])
    else:
        print("consonant", name[start_index])
    start_index = start_index+1