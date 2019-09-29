def tokenize(all_texts_lines):
    word_map = {}
    for l in all_texts_lines:
        words = l.split()
        for w in words:
            if w in word_map.keys():
                word_map[w] += 1
            else:
                word_map[w] = 1
    return word_map


def replace_1_Occur(oldMap, oldUpdatedLines):
    newLines = list(oldUpdatedLines)
    newList = []
    for l in newLines:
        words = l.split()
        for w in words:
            if oldMap[w] == 1:
                a = l.replace(w, "<unk>")
                newList.append(a)
    return newList


def read(file):
    f = open(file)
    all = f.readlines()
    newFile = []
    for l in all:
        newFile.append("<s> " + l.rstrip().lstrip().lower() + " </s>")
    return newFile

def write(updatedLines, newFileName):
    f = open(newFileName, "w+")
    for l in updatedLines:
        f.write(l+"\n")


updatedLines = read("train.txt")
updatedMap = tokenize(updatedLines)
write(updatedLines, "mod.txt")
print(replace_1_Occur(updatedMap, updatedLines))
print("Unique", len(updatedMap))
print("Total tokens", sum(updatedMap.values()))
