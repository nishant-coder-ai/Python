month = {
    "jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jly": "July",
    "Aug": "August",
    "Spt": "September",
    "Oct": "October",
    "Nov": "November",
    "Dcm": "December"
}

print(month)
print(month["Oct"])
print(month.get("Oct"))
print(month.get("Lon"))
print(month.get("Lon", "Not a Valid Key"))
