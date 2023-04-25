from pprint import pprint
import csv
import re
 
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

# убираем дубли
def get_final_list(string):
    new_string = {}
    for row in string:
        surname = row[:2]
        fi = " ".join(surname)
        if fi in new_string:
            for ind, l in enumerate(new_string[fi]):
                if not l:
                    new_string[fi][ind] = row[ind]
        else:
            new_string[fi] = row
    new_list = list(new_string.values())

    return new_list


if __name__ == '__main__':

    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    
    contacts = get_contacts(contacts_list)
   
    big_list = new_list(contacts)
    
    final_list = get_final_list(big_list)
    print(final_list)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(final_list)
  
    
    


