dup_list = [1,2,2,4,5,5]
get_len = len(dup_list)-1
index_val = 0
get_highval = 0
for i in dup_list:
    while index_val <= get_len:
        if i > dup_list[index_val] and i > get_highval:
            get_highval = i
        index_val += 1
    index_val = 0
print(get_highval)