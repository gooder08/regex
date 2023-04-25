from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
string = []
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    
    # pprint(contacts_list)
    # string = ''
    # new_string = ''
    for i in contacts_list:
        a = ' '.join(i)
        # print(a)
        b = a.split(' ')
        # print(b)
        string.append(b)
# print(string)
new_string = {}
for row in string:
    surname = row[:2]
    # print(surname)
    fi = ",".join(surname)
    # print(fi)
    m = row[2:]
    # print(m)
    field = " ".join(m)
    # print(field)
    if fi in new_string:
        new_string[fi] = (new_string[fi] + ',' + field)
    else:
        new_string[fi] = (fi + ',' + field)
# print(new_string)
last_string = []
values = new_string.values()
last_string.extend(values)
# print(last_string)
last_string1 = ''
for l in last_string:
  last_string1 += l + '\n'
print(last_string1)
# pattern_fio = r"([А-Я][а-я]+,[А-Я][а-я]+,[А-Я][а-я]+)"
# pattern = r"([А-Я][а-я]+,[А-Я][а-я]+,[А-Я][а-я]+)(\s+)(ФНС|Минфин)([а-яёА-ЯЁ|–|\s+]*)(495)([) |-|)]*)([0-9][0-9][0-9])([-]*)([0-9][0-9])([-]*)([0-9][0-9])(\s+)([доб\. |(доб\. ]*)([0-9]*[0-9]*[0-9]*[0-9]*(?!@))"
pattern = r"([А-Я][а-я]+,[А-Я][а-я]+,[А-Я][а-я]+)(\s+)(ФНС|Минфин)([а-яёА-ЯЁ|–|\s]*)(\s)([+7 (|+7|8 |8(]*)(495)([) |)|-]*)(\d\d\d)([-]*)(\d\d)([-]*)(\d\d)([\s|\s(]*)([доб.]*)(\s)([\d{4}(?!1248)]*)([\s+|.|,]*)([a-zA-Z|@|.|d+]*)"
# pattern = r"([а-я])"
final = re.sub(pattern, r"\1,\3,+7(\7)\9-\11-\13 \15\17,\19\n", last_string1)
# pattern_org = r"(ФНС|Минфин)"
find = re.findall(pattern, last_string1)
# g = fio + org
print(find)
print(final)
# pattern1 = r"?!\1\w+"
# position = re.findall(pattern1, last_string1)
# print(position)

  
    
    #     
    #     string += a + '\n'
    # print(string[:1])
    # pattern = r'([А-Я][а-я]+)(\s+|[,])([А-Я][а-я]+)'
    # replace = re.sub(pattern, r'\1,\3,', string)
    # print(replace)
    # pattern1 = r'([А-Я][а-я]+)(\s+|[,])([А-Я][а-я]+)([,])'
    # matches = re.match(pattern1, replace)
    # print(matches)

        
    #     a = ",".join(i)
    #     string += a + "\n"
    # print(string)
    #     b = " ".join(i[2:])
    #     # i[:len(a)] = a
    #     # print(a)
    #     string[f'{a[:2]}'] = f'{b}'
    # pprint(string)
        # string[a[:2]] = 
        # pattern = r'\b([А-Я][а-я]+)(\s+|[,])([А-Я][а-я]+)'
        # replace = re.sub(pattern, r'\1,\3', a)
        # pattern1 = r'[А-Я][а-я]+[,][А-Я][а-я]+'
        # first_word = re.search(pattern1, replace)
        # print(first_word)
        # string 
        # if first_word not in string:
        #    string += a
    # print(string)

        # print(first_word)
    #   
    #   string += a + '\n'
    # # print(string)
    # new_string = ''
    # pattern =   r'([А-Я][а-я]+)(\s+|[,])'
    # matches = re.findall(pattern, string)
    # print(matches)
    # print(n)
    #    for k in i:
    # #       string = " ".join(k)
    #       print(k)
    # string = " ".join(map(str, contacts_list))
    # print(string)
    # pattern =   r'([А-Я][а-я]+)(\s+|[,])([А-Я][а-я]+)'
    # pattern =   r'([А-Я][а-я]+)(\s+|[,])([А-Я][а-я]+)(\s+|[,])([А-Я][а-я]+)([,]+)([ФНС|Минфин]+)([,]+)'
    # matches = re.search(pattern, )
    # replace = re.sub(pattern, r'\1', string)
    
    
    # pattern1 = r'\b([А-Я][а-я]+)[,]([А-Я][а-я]+)[,])\b\b\1\b'
    # replace1 = re.sub(pattern1, r'\1', replace)

    # matches = re.sub(pattern, r'/1,', string)
    
    # pprint(matches)
    # print()
    # print(replace)
    # new_string = []
    # last_name = None
    # for line in string:
    #    current_last_name = matches.group(1)
    #    if current_last_name == last_name:
    #       new_string[-1] += ',' + line
    #    else:
    #       new_string.append(line)
    #       last_name = current_last_name
    # for line in new_string:
    #    print(line)



## 1. Выполните пункты 1-3 задания.
## Ваш код

## 2. Сохраните получившиеся данные в другой файл.
# ## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  
## Вместо contacts_list подставьте свой список:
  datawriter.writerow(contacts_list[0])
  # datawriter.writerows()