def find_and_print(msg):
    for name, message in msg.items():
        keywords = {"college", "legal age", "vote"}  
        # 根據下列依據將college, legal age, vote最為大於17歲的依據: 
        # 1.大學學齡為19 - 23 2.民法及刑法法定年齡為18歲 3.美國法定投票年齡為18歲
        for word in keywords:
            if word in message:
                print(f'{name}')
        words = message.split()
        for word in words:
            if word.isdigit() and int(word) > 17 and "years"in words:
                print(name) 
find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
})