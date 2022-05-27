# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import re
def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename, 'r')
    return file


def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    story = []
    text = text.read()
    content = text.split(' ')
    for i in content:
        #print(i)
        #i = re.sub(r'\n', '', i)
        i = i.strip(',')
        i2 = i.strip('?')
        i3 = i2.strip('.')
        i4 = i3.strip('\n')
        story.append(i4)

    split_content = ''.join(story)

    dictionary = {}
    for s in story:
        dictionary[s] = (story.count(s))
    print(f'Total Words: {len(story)}\nTotal Letters:{len(split_content)}')
    
    return (dictionary)
init = count_words()
print(init)