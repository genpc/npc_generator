import json

fileobj = open("dict.txt")
lines = fileobj.readlines()
lines = [line.strip()for line in lines]

word_indices = []

for line_index in range(len(lines)):
    if lines[line_index].upper() == lines[line_index] and lines[line_index]:
        word_indices.append(line_index)

temp_dict = {}
for word_index in range(len(word_indices)):
    if word_indices[word_index] != word_indices[-1]:
        x = lines[word_indices[word_index] + 1]
        y = lines[word_indices[word_index + 1]]
        temp_dict[lines[word_indices[word_index]]] = "+++".join(lines[word_indices[word_index] + 1:word_indices[word_index + 1]])

adj_dict = {}
for key in temp_dict:
    if ', a.' in temp_dict[key]:
        adj_dict[key] = temp_dict[key]

with open('gutenberg_adj.json', 'w') as outfile:
    outfile.write(json.dumps(adj_dict, indent=4))