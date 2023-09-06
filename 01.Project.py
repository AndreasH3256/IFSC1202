Time = int(input("Enter Length of Time in Days: "))

year = Time // 365
weeks =  Time // 52
days = weeks % 7

print(year)
print(weeks)
print(days)