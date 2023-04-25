from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
from collections import defaultdict 

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    
# Меняем телефоны и получаем список    
def get_contacts(contacts_list):
    contacts = []
    for el in contacts_list:
        if len(el[0].split()) == 3:
            lastname = el[0].split()[0]
            firstname = el[0].split()[1] 
            surname = el[0].split()[2]
        elif len(el[0].split()) == 2:
            lastname = el[0].split()[0]
            firstname = el[0].split()[1] 
            surname = el[1]  
        else:
            lastname = el[0].split()[0]
            firstname = el[1] if len(el[1].split()) == 1 else el[1].split()[0]
            surname = el[2] if len(el[1].split()) == 1 else el[1].split()[1]
        organization = el[3]
        position = el[4]
        email = el[6]
        if 'доб' in el[5]:
            phone = re.sub(r'(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})\s*\(*доб\.*\s*(\d+)*\)*', r'+7(\2)\3-\4-\5 доб.\6', el[5])
        else:
            phone = re.sub(r'(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})', r'+7(\2)\3-\4-\5', el[5])
        contacts.extend([lastname, firstname, surname, organization, position, phone, email])
    return contacts


# разбиваем список на несколько списков
def new_list(contacts):
    n = len(contacts) // 7
    new_lists = [contacts[i:i + 7] for i in range(0, n * 7, 7)]
    if len(contacts) % 7 != 0:
        new_lists.append(contacts[n * 7:])
    return new_lists

a = get_contacts(contacts_list)
# print(new_list(a))


# обьединяем дубликаты
def merge_dub(big_list):
    new_dict = defaultdict(list)
    for lst in big_list:
        new_dict[lst[0]].extend(lst[1:])
    new_list = [[k] + v for k, v in new_dict.items()]
    return new_list

# удаляем дубли в списках списка
def del_dub(new_list):
    for n in new_list:
        for k in n:
            
            while n.count(k) > 1:
                n.remove(k)
    return new_list


if __name__ == '__main__':

    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    
    contacts = get_contacts(contacts_list)
    print(contacts)
    print()
    big_list = new_list(contacts)
    print(big_list)
    print()
    merge = merge_dub(big_list)
    print(merge)
    print()
    a = del_dub(merge)
    print(a)
    print()
    final_list = new_list(a)
    print(final_list)
    
    




                
## 1. Выполните пункты 1-3 задания.
## Ваш код

## 2. Сохраните получившиеся данные в другой файл.
# ## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  
## Вместо contacts_list подставьте свой список:
  datawriter.writerow(final_list)
  # datawriter.writerows()