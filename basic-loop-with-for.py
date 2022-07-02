"""
Loop with For
"""
book_count = 100
print('Mom says, "Read all books"')

book_count_read = 0
print(f'Total books have read: {book_count_read} ')

print('With for')
for book_count_read in range(1,book_count+1):
    print(f'Book no: {book_count_read}')

print(f'Total books have read: {book_count_read}')
