def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                month, day, year = date.split('/')
                m = int(month)
                d = int(day)
                y = int(year)
                if 1 <= m <= 12 and 1 <= d <= 31:
                    print(f"{year}-{m:02}-{d:02}")
                    break
            else:
                if "," in date:
                    date = date.replace(',','')
                    month_name, day, year = date.split()

                    if month_name in months:
                        month = months.index(month_name) + 1
                        day = int(day)
                        year = int(year)
                        if 1 <= day <= 31:
                            print(f"{year}-{month:02}-{day:02}")
                            break
        except (UnboundLocalError, ValueError, IndexError):
            pass
if __name__ == "__main__":
    main()
