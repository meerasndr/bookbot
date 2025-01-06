def wordcount(content):
    words = content.split()
    return len(words)


def charactercount(content):
    char_map = {}
    for char in content:
        if char and char.isalpha():
            lowered = char.lower()
            if lowered in char_map:
                char_map[lowered] += 1
            else:
                char_map[lowered] = 1
    return {
        k: v
        for k, v in sorted(char_map.items(), key=lambda item: item[1], reverse=True)
    }


with open("books/frankenstein.txt") as f:
    file_contents = f.read()

cc = charactercount(file_contents)
print("--- Begin report of books/frankenstein.txt ---")
print(f"{wordcount(file_contents)} words found in the document")
for k, v in cc.items():
    print(f"The '{k}' character was found {v} times")
print("--- End report ---")
