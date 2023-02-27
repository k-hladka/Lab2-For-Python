month = int(input("Введіть номер місяця: "))
resultStringMonth = "Incorrect"
match month:
    case 1: resultStringMonth = "January"
    case 2: resultStringMonth = "February"
    case 3: resultStringMonth = "March"
    case 4: resultStringMonth = "April"
    case 5: resultStringMonth = "May"
    case 6: resultStringMonth = "June"
    case 7: resultStringMonth = "July"
    case 8: resultStringMonth = "August"
    case 9: resultStringMonth = "September"
    case 10: resultStringMonth = "October"
    case 11: resultStringMonth = "November"
    case 12: resultStringMonth = "December"

print(resultStringMonth)