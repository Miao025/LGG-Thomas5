import csv

def read_names_from_csv(filename):
    with open('utils/'+filename, newline='') as f:
        names_list = []
        reader = csv.reader(f)
        data = list(reader)
        for name in data:
            names_list.append(name[0])
    return names_list


