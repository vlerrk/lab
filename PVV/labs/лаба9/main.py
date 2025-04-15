import xml.etree.ElementTree as ET
from statistics import mean

def process_library(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        books = []
        
        # Вывод всех книг
        print("Список книг:")
        for book in root.findall('book'):
            book_data = {
                'title': book.find('title').text,
                'author': book.find('author').text,
                'year': book.find('year').text,
                'genre': book.find('genre').text,
                'price': float(book.find('price').text)
            }
            books.append(book_data)
            print(f"""
            Название: {book_data['title']}
            Автор: {book_data['author']}
            Год: {book_data['year']}
            Жанр: {book_data['genre']}
            Цена: {book_data['price']:.2f}
            """)
        
        # Средняя цена
        avg_price = mean(b['price'] for b in books)
        print(f"Средняя цена книг: {avg_price:.2f}")
        
        # Фильтрация по жанру (пример)
        filtered_genre = 'Fantasy'
        filtered_books = [b for b in books if b['genre'] == filtered_genre]
        print(f"\nКниги в жанре '{filtered_genre}':")
        for b in filtered_books:
            print(f"- {b['title']} ({b['year']})")
            
    except ET.ParseError:
        print("Ошибка чтения XML!")
    except FileNotFoundError:
        print("Файл не найден!")
    except Exception as e:
        print(f"Ошибка: {e}")

process_library("library.xml")