

def read_file_content(filename):
    with open(filename) as f:
        lines = f.readlines()
    return (lines)


def count_words():
    words = []
    text = read_file_content("story.txt")

    for t in text:
        t = t.split()

    for i in t:
        words.append(i)
    
    final_dict = {}
    for word in words:
        final_dict[word] = words.count(word)

    print (final_dict)

print (count_words())

