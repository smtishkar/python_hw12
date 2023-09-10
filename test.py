import csv


def subjects ():
    dict_averages = {}
    with open('subjects.csv', 'r', encoding='utf-8', newline='') as f:
        csv_file = csv.reader(f, delimiter=';')
        for line in csv_file:
            subject = line[0]
            marks = line[1]
            tests = line[2]
            print(line)
            print(subject)
            print(marks)
            print(tests)


# subjects()


subjects_list =[]
with open('subjects.csv', 'r', encoding='utf-8', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
        subjects_list.append(''.join(line))  
    print(subjects_list)    



    a = {}
    a = {'123': {'444':'777777'}}
    # a['123']['4444'] = '43434'
    print(a)