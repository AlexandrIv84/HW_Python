def menu() -> int:
    print('''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Добавить контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход''')
    choice = int(input('Выберите пункт меню: '))
    return choice

def show_contact(phone_book: list[dict]):
    print()
    if phone_book:
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<20} '
                  f'{contact.get("phone"):<20} '
                  f'{contact.get("comment"):<20}')
        print()
    else:
        print('\nТелефонная книга не открыта или пуста\n')

def new_contact() -> dict:
    print()
    name = input('Введите имя и фамилию контакта: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    print()
    return {'name': name, 'phone': phone, 'comment': comment}

def change_contact(book: list) -> tuple:
    show_contact(book)
    choice = int(input('Выберите контакт для изменения: '))
    name = input('Введите новое имя или нажмите Enter для пропуска: ')
    phone = input('Введите новый телефон или нажмите Enter для пропуска: ')
    comment = input('Введите новый комментарий или нажмите Enter для пропуска: ')
    return choice - 1, {'name': name if name else book[choice - 1].get('name'),
                        'phone': phone if phone else book[choice - 1].get('phone'),
                        'comment': comment if comment else book[choice - 1].get('comment')}

def select_to_delete(book: list):
    show_contact(book)
    return int(input('Введите номер элемента для удаления: ')) -1

def input_request(text: str) -> str:
    return input(f'Введите {text}: ')

def goodbye():
    print('Прощайте!')