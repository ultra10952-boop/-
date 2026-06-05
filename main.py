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

def list_books(books):
    if len(books)>0:
        print('\nКниги:')
        for book in books:
           print(f'{book['author']} "{book['name']}", Дата: {book['date']}, Оценка: {book['rating']}/5')
    else:
        print('\nСписок пуст')

def show_average(books):
    if len(books)>0:
        rating_sum=0
        for book in books:
            rating_sum+=book['rating']
        print(f'\nСредняя оценка среди книг в списке: {round(rating_sum/len(books),2)}')
    else:
        print('\nСписок пуст')

def stats_by_author(books):
    if len(books)>0:
        print()
        authors={}
        for book in books:
            authors[book['author']]=authors.get(book['author'],0)+1
        for author,amt in authors.items():
            print(f'Автор: {author}, всего {amt} книг')
    else:
        print('\nСписок пуст')
        
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
    for book in books:
        if author==book['author']and name==book['name']:
            print('\nДанная книга уже существует')
            return
    books.append({'author':author,'name':name,'rating':rating,'date':date})
    save_books(books)
    print('\nКнига добавлена в список')

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
            list_books(books)
        elif choice=='3':
            show_average(books)
        elif choice=='4':
            stats_by_author(books)
        elif choice=='5':
            delete_book(books)
        elif choice=='6':
            break

if __name__ == "__main__":
    main()