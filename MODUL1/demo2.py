class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.borrowed_books = []

    def borrow_book(self, book, book_list):
        if book in book_list:
            if book.available:
                book.available = False
                self.borrowed_books.append(book)
                print(f"{self.username} berhasil meminjam buku: {book.title}")
            else:
                print(f"Buku '{book.title}' sedang dipinjam oleh pengguna lain.")
        else:
            print(f"Buku '{book.title}' tidak tersedia dalam perpustakaan.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.username} berhasil mengembalikan buku: {book.title}")
        else:
            print(f"Buku '{book.title}' tidak ada dalam daftar peminjaman {self.username}.")

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_book(self, book, book_list):
        book_list.append(book)
        print(f"Admin {self.username} berhasil menambahkan buku: {book.title}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

def main():
    # Inisialisasi akun admin dan user
    admin = Admin("admin", "adminpass")
    user1 = User("user1", "userpass")
    user2 = User("user2", "userpass")

    # Inisialisasi daftar buku (kosong)
    books = []

    while True:
        print("\nPilihan Menu:")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Keluar")
        choice = input("Pilih menu (1/2/3): ")

        if choice == "1":
            admin_username = input("Masukkan username admin: ")
            admin_password = input("Masukkan password admin: ")

            if admin_username == admin.username and admin_password == admin.password:
                while True:
                    print("\nPilihan Admin:")
                    print("1. Tambahkan Buku")
                    print("2. Logout")
                    admin_choice = input("Pilih aksi (1/2): ")

                    if admin_choice == "1":
                        book_title = input("Masukkan judul buku: ")
                        book_author = input("Masukkan penulis buku: ")
                        new_book = Book(book_title, book_author)
                        admin.add_book(new_book, books)
                    elif admin_choice == "2":
                        break
                    else:
                        print("Pilihan tidak valid!")

            else:
                print("Username atau password admin salah!")

        elif choice == "2":
            user_username = input("Masukkan username user: ")
            user_password = input("Masukkan password user: ")

            current_user = None
            for user in [user1, user2]:
                if user_username == user.username and user_password == user.password:
                    current_user = user
                    break

            if current_user:
                while True:
                    print("\nPilihan User:")
                    print("1. Pinjam Buku")
                    print("2. Kembalikan Buku")
                    print("3. Logout")
                    user_choice = input("Pilih aksi (1/2/3): ")

                    if user_choice == "1":
                        if books:
                            print("Buku yang tersedia:")
                            for i, book in enumerate(books):
                                print(f"{i + 1}. {book.title} oleh {book.author}")
                            book_choice = input("Pilih nomor buku yang ingin dipinjam: ")
                            if book_choice.isdigit():
                                book_choice = int(book_choice)
                                if 1 <= book_choice <= len(books):
                                    current_user.borrow_book(books[book_choice - 1], books)
                                else:
                                    print("Nomor buku tidak valid!")
                            else:
                                print("Input harus berupa angka!")
                        else:
                            print("Tidak ada buku yang tersedia untuk dipinjam.")

                    elif user_choice == "2":
                        if current_user.borrowed_books:
                            print("Buku yang Anda pinjam:")
                            for i, book in enumerate(current_user.borrowed_books):
                                print(f"{i + 1}. {book.title} oleh {book.author}")
                            book_choice = input("Pilih nomor buku yang ingin dikembalikan: ")
                            if book_choice.isdigit():
                                book_choice = int(book_choice)
                                if 1 <= book_choice <= len(current_user.borrowed_books):
                                    current_user.return_book(current_user.borrowed_books[book_choice - 1], books)
                                else:
                                    print("Nomor buku tidak valid!")
                            else:
                                print("Input harus berupa angka!")
                        else:
                            print("Anda belum meminjam buku apapun.")
                    
                    elif user_choice == "3":
                        break
                    else:
                        print("Pilihan tidak valid!")

            else:
                print("Username atau password user salah!")

        elif choice == "3":
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
