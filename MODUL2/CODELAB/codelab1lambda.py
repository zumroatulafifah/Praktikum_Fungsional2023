
expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

#pure function
add_expense = lambda expenses, date, description, amount: expenses + [{'tanggal': date, 'deskripsi': description, 'jumlah': amount}]

#lambda function
calculate_total_expenses = lambda expenses, date: sum(expense['jumlah'] for expense in expenses if expense['tanggal'] == date)

#calculate_total_expenses = lambda expenses: sum(expense['jumlah'] for expense in expenses)

#calculate_total_expenses = lambda expenses, date: sum(expense['jumlah'] for expense in expenses if expense['tanggal'] == date)


# show_all_total_expenses = lambda expenses: [
#     (date, sum(expense['jumlah'] for expense in daily_expense_list))
#     for date, daily_expense_list in
#     {date: [expense for expense in expenses if expense['tanggal'] == date] for expense in expenses}.items()
# ]


get_expenses_by_date = lambda expenses, date: [expense for expense in expenses if expense['tanggal'] == date]

#
# show_total_expenses_by_date = lambda expenses, date: print(
#     f"Total pengeluaran pada tanggal {date}: {calculate_total_expenses(expenses, date)}")

def generate_expenses_report(expenses):
    daily_expenses = {}
    for expense in expenses:
        date = expense['tanggal']
        if date in daily_expenses:
            daily_expenses[date].append(expense)
        else:
            daily_expenses[date] = [expense]

    for date, daily_expense_list in daily_expenses.items():
        total_expense = sum(expense['jumlah'] for expense in daily_expense_list)
        expense_descriptions = '; '.join(expense['deskripsi'] for expense in daily_expense_list)
        yield f"{date}: {total_expense} - {expense_descriptions}"


def main():
    while True:
        print("\nPilihan Menu 2 :")
        print("1. Tambahkan Pengeluaran")
        print("2. Lihat Laporan Pengeluaran Harian")
        print("3. Lihat Pengeluaran per Tanggal")
        print("4. Total Pengeluaran Harian")
        print("5. Keluar")
        choice = input("Pilih menu (1/2/3/4): ")

        if choice == "1":
            date = input("\nMasukkan tanggal (format: yyyy-mm-dd): ")
            description = input("Masukkan deskripsi pengeluaran: ")
            amount = int(input("Masukkan jumlah pengeluaran: "))
            global expenses
            expenses = add_expense(expenses, date, description, amount)
            print("\nPengeluaran berhasil ditambahkan!")

        elif choice == "2":
            report_generator = generate_expenses_report(expenses)
            print("\nLaporan Pengeluaran Harian:")
            for report in report_generator:
                print(report)

        elif choice == "3":
            date = input("\nMasukkan tanggal (format: yyyy-mm-dd): ")
            #total_expense = calculate_total_expenses(expenses, date)
            expenses_by_date = get_expenses_by_date(expenses, date)

            if expenses_by_date:
                print(f"\nPengeluaran pada tanggal {date}:")
                for expense in expenses_by_date:
                    print(f"Deskripsi: {expense['deskripsi']}, Jumlah: {expense['jumlah']}")

                #print(f"Total pengeluaran pada tanggal {date}: {total_expense}")
            else:
                print(f"Tidak ada pengeluaran pada tanggal {date}.")

        elif choice == "4":
            # total_all_expenses = calculate_total_expenses(expenses)
            # print(f"\nTotal pengeluaran harian: {total_all_expenses}")

            report_generator = generate_expenses_report(expenses)
            for report in report_generator:
                date, _ = report.split(':')  # Memisahkan tanggal dari laporan
                # date = date.strip()  # Menghapus spasi ekstra
                total_daily_expense = calculate_total_expenses(expenses, date)
                print(f"\nTotal pengeluaran harian untuk tanggal {date}: {total_daily_expense}")
            
        elif choice == "5":
            break

        else:
            print("Pilihan tidak valid !. Silahkan Pilih Menu yang benar")

if __name__ == "__main__":
    main()
