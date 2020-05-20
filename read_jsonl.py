import jsonlines

data = []

with jsonlines.open('input.jsonl') as f:
    for line in f.iter():
        data.append(line)
