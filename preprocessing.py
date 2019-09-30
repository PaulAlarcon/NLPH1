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


def read(file):
    f = open(file)
    all = f.readlines()
    newFile = []
    for l in all:
        newFile.append("<s> " + l.rstrip().lstrip().lower() + " </s>")
    return newFile


def rep_occ_once(m_count, line_list):
    new_line_list = []
    new_line = ""
    for line in line_list:
        for w in line.split():
            if m_count[w] == 1:
                new_line += " <unk> "
            else:
                new_line += w + " "
        new_line_list.append(new_line)
        new_line = ""
    return new_line_list


def write_into_file(output_file, text_lines):
    temp = open(output_file, "w+")
    for l in text_lines:
        temp.write(l+"\n")

def build_prob(token_map):
    stats = {}
    total_tokens = sum(token_map.values())
    for key in token_map:
        stats[key] = token_map[key] / total_tokens

    return stats


brown_train = read("brown-train.txt")
brown_train_tokens = tokenize(brown_train)
new_brown_train = rep_occ_once(brown_train_tokens, brown_train)
new_brown_train_tokens = tokenize(new_brown_train)
write_into_file("brown-train-out.txt", new_brown_train)


brown_test = read("brown-test.txt")
brown_test_tokens = tokenize(brown_test)
