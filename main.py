import json
from datetime import datetime

def load_books():
    with open('books.json','r',encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            return []

def save_books(books):
    with open('books.json','w',encoding='utf-8') as f:
        json.dump(books,f,ensure_ascii=False,indent=2)

def add_book(books):
    print('\nВведите следующие данные:')
    author=input('Автора книги: ')
    name=input('Название книги: ')
    rating=input('Оценку книги от 1 до 5: ')
    try:
        rating=int(rating)
        if rating>5 or rating<1:
            print('Оценка выходит за заданные пределы')
            return
    except:
        print('Оценка введена неправильно')
        return
    date=input('Дату (дд/мм/гггг): ')
    books.append({'author':author,'name':name,'rating':rating,'date':date})
    save_books(books)
    print('Книга добавлена в список')

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
            add_book(books)
        elif choice=='2':
            pass
        elif choice=='3':
            pass
        elif choice=='4':
            pass
        elif choice=='5':
            pass
        elif choice=='6':
            break

if __name__ == "__main__":
    main()