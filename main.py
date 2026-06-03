import json

def load_books():
    with open('books.json','r',encoding='utf-8') as f:
        return json.load(f)

def save_books(books):
    with open('books.json','w',encoding='utf-8') as f:
        json.dump(books,f,ensure_ascii=False,indent=2)

def main():
    while True:
        books=load_books()

        print('1. Добавить книгу')
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
            pass
        elif choice=='6':
            break

if __name__ == "__main__":
    main()