def func(*data):
    second_chars = {}
    for name in data:
        if len(name) >= 2:
            second_char = name[1]
            if second_char not in second_chars:
                second_chars[second_char] = 1
            else:
                second_chars[second_char] += 1
    
    result = []
    for name in data:
        if len(name) >= 2 and second_chars[name[1]] == 1:
            result.append(name)
    
    if len(result) > 0:
        print(" ".join(result))
    else:
        print("沒有")

func("彭⼤牆", "王明雅", "吳明")  # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有