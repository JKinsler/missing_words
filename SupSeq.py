"""

"""

def missingWords(s, t):
    # Write your code here

    """
    inputs:
    s = string
    t = string
    """
    missingWords = []
    new_t = t.split()
    print(new_t)
    new_s = s.split()
    print(new_s)
    for index, word in enumerate(new_s):
        if new_t[index] != word:
            missingWords.append(word)
            new_t[index] = word

    new_list = new_s - new_t

    return new_list

def missingWords2(s, t):
    """
    inputs:
    s = string
    t = string

    output: 
    return
    each
    word

    This solution doesn't work if a word is repeated later but initially doesn't 
    have the right order of a missing word.
    """
    # missingWords = []
    
    new_s = s.split()
    # print(new_s)

    new_t = t.split()
    # print(new_t)

    missing = []

    while len(new_t) > 0:
        for word in new_s:
            if word not in new_t:
                missing.append(word)
            else:
                new_t.remove(word)

    return missing


def missingWords3(s, t):
    """
    inputs:
    s = string
    t = string

    output: 
    return
    each
    word
    """
    # missingWords = []
    
    new_s = s.split()
    new_t = t.split()
    missing = []
    j = 0

    for i in range(len(new_s)):
        if j <= len(new_t) - 1
        if new_s[i] != new_t[j]:
            missing.append(new_s[i])
        else:
            j += 1

    return missing

if __name__ == '__main__':
    
    s = 'I am using HackerRank to improve programming'
    t = 'am HackerRank to improve'
    print('Test s, t:')
    print(missingWords3(s, t))

    first = 'Python is an easy to learn powerful programming language It has efficient high-level data structures and a simple but effective approach to objectoriented programming Python elegant syntax and dynamic typing'
    second = 'Python is an easy to learn powerful programming language'
    print('Test first, second')
    print(missingWords3(first, second))

    

