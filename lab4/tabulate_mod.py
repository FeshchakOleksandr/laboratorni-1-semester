from tabulate import tabulate

def run_tabulate():
    data = [["Предмет", "Оцінка"], ["Програмісти", 12]]
    print(tabulate(data, headers="firstrow", tablefmt="outline"))