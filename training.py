
def tokenize(text):
    mc = {}
    for w in text.split():
        if w in mc.keys():
            mc[w] = mc[w] + 1
        else:
            mc[w] = 1

    return mc


t = open("test.txt")
t_read = t.read().lower()

t_processed = "";

for line in t_read.split("\n"):
    line = "<s> " + line + " </s> \n"
    t_processed += line

t_processed_padded = t_processed;

map_count = tokenize(t_processed)

for key in map_count.keys():
    if map_count[key] == 1:
        word = " "+key+" "
        t_processed = t_processed.replace(key, " <unk> ")
new_map_count = tokenize(t_processed)

print(len(t_processed.split()))

def read(file):
    f = open(file)
    all = f.readlines()
    newFile = []
    for l in all:
        newFile.append("<s> " + l.rstrip().lstrip().lower() + " </s>")
    return newFile
