def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    count = {}
    for t in text:
        char = t.lower()
        count[char] = count.get(char, 0) + 1
    return count

def sort_on(items):
    return items["num"]

def sorted_list(text):
    merged = []
    for t in text:
        merged.append({"char": t, "num": text[t]})
    merged.sort(reverse=True, key=sort_on)
    return merged