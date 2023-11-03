from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

# Fungsi untuk menampilkan data film
def display_movie_data(movie):
    return f"Judul: {movie['title']}, Tahun: {movie['year']}, Rating: {movie['rating']}, Genre: {movie['genre']}"

# Fungsi untuk menghitung jumlah film berdasarkan genre
def count_movies_by_genre(genre):
    return len(list(filter(lambda movie: movie['genre'] == genre, movies)))

# Fungsi untuk menghitung rata-rata rating film berdasarkan tahun rilis
def calculate_average_rating_by_year(year):
    year_movies = list(filter(lambda movie: movie['year'] == year, movies))
    if not year_movies:
        return 0
    total_rating = reduce(lambda x, y: x + y['rating'], year_movies, 0) #akan menghitung rata2 pada thn tersebut jika ada
    return total_rating / len(year_movies)

# Fungsi untuk menemukan film dengan rating tertinggi
def find_highest_rated_movie():
    return max(movies, key=lambda movie: movie['rating'])

# Fungsi untuk mencari film berdasarkan judul
def find_movie_by_title(title):
    movie = next((movie for movie in movies if movie['title'].lower() == title.lower()), None) #list comperhension
    return movie

# Menampilkan menu
while True:
    print("\nPilih tugas yang ingin dilakukan:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")
    
    choice = input("Masukkan nomor tugas (1/2/3/4/5): ")
    
    if choice == '1':
        # Tugas 1: Menghitung jumlah film berdasarkan genre
        genres = list(set(map(lambda movie: movie['genre'], movies)))
        genre_count = {genre: count_movies_by_genre(genre) for genre in genres}
        print("Jumlah Film Berdasarkan Genre:")
        print(genre_count)
    elif choice == '2':
        # Tugas 2: Menghitung rata-rata rating film berdasarkan tahun rilis
        years = list(set(map(lambda movie: movie['year'], movies))
        )
        average_rating_by_year = {year: calculate_average_rating_by_year(year) for year in years}
        print("Rata-rata Rating Film Berdasarkan Tahun Rilis:")
        print(average_rating_by_year)
    elif choice == '3':
        # Tugas 3: Menemukan film dengan rating tertinggi
        highest_rated_movie = find_highest_rated_movie()
        print("Film dengan Rating Tertinggi:\n")
        print(display_movie_data(highest_rated_movie))
    elif choice == '4':
        # Tugas 4: Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre
        title = input("\nMasukkan judul film yang ingin dicari: ")
        movie = find_movie_by_title(title)
        if movie:
            print(f"\nInformasi Film : {movie['title']}")
            print(f"Rating : {movie['rating']}")
            print(f"Tahun Rilis : {movie['year']}")
            print(f"Genre : {movie['genre']}\n")
        else:
            print(f"Film dengan judul '{title}' tidak ditemukan.\n")
    elif choice == '5':
        # Tugas 5: Keluar dari program
        break
    else:
        print("Pilihan tidak valid. Silakan pilih tugas yang benar.")
