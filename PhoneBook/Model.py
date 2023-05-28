phone_book: list[dict[str, str]] = []
PATH = 'Phone_book.txt'


def open_file():
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        contact = {'name': contact[0], 'phone': contact[1], 'comment': contact[2]}
        phone_book.append(contact)


def save_file():
    data =[]
    for contact in phone_book:
        contact = ':'.join([value for value in contact.values()])
        data.append(contact)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))


def get_pb() -> list[dict[str, str]]:
    return phone_book

def add_contact(contact: dict[str, str]):
    phone_book.append(contact)


def change(ind: int, contact: dict[str, str]) -> dict[str, str]:
    cur = phone_book[ind]
    cur.update(contact)
    result = phone_book.pop(ind)
    phone_book.insert(ind, cur)
    return result


def del_contact(index: int):
    return phone_book.pop(index-1).get('name')

def find_contact(message: str, pb: dict) ->list:
    for contact in pb:
        if message.lower() in contact.get('name').lower():
            return contact