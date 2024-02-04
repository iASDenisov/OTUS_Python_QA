import csv
import json

# Чтение данных из файла books.csv
books = []
with open('books.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        books.append(row[0])

# Чтение данных из файла users.json
with open('users.json', 'r') as file:
    users = json.load(file)

# Распределение книг пользователям
num_books = len(books)
num_users = len(users)
books_per_user = num_books // num_users
remainder = num_books % num_users

for i in range(num_users):
    start_index = i * books_per_user
    end_index = start_index + books_per_user
    if i < remainder:
        end_index += 1
    user_books = books[start_index:end_index]
    users[i]['books'] = user_books

# Запись данных в файл result.json
with open('result.json', 'w') as file:
    json.dump(users, file, indent=4)

print("Распределение книг пользователям успешно завершено.")
