import json

def load_books():
    with open('books.json','r',encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            return []

def save_books(books):
    with open('books.json','w',encoding='utf-8') as f:
        json.dump(books,f,ensure_ascii=False,indent=2)

def list_for_deletion(books):
    index=0
    for book in books:
        index+=1
        print(f'{index}: {book['author']} "{book['name']}", Оценка: {book['rating']}, Дата: {book['date']}')

def delete_book(books):
    if len(books)>0:
        list_for_deletion(books)
        index=input('Введите индекс книги: ')
        try:
            index=int(index)
            if index>len(books):
                print('\nКниги с данным индексом не существует')
                return
        except:
            print('\nИндекс введен неправильно')
            return
        books.pop(index-1)
        save_books(books)
        print('\nКнига удалена из списка')
    else:
        print('\nСписок пуст')


def main():
    while True:
        books=load_books()

        print('\n1. Добавить книгу')
        print('2. Показать все книги')
        print('3. Показать среднюю оценку')
        print('4. Статистика по авторам')
        print('5. Удалить книгу')
        print('6. Выход')
        choice=input('Выберите действие (1-6): ').strip()
        if choice=='1':
            pass
        elif choice=='2':
            pass
        elif choice=='3':
            pass
        elif choice=='4':
            pass
        elif choice=='5':
            delete_book(books)
        elif choice=='6':
            break

if __name__ == "__main__":
    main()