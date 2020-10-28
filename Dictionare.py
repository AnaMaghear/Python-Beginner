monthConversion = {   # Folosesti colade  cheie: semnificatie, cheiile nu se pot repeta
     0: "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "Octomber",
    "Nov": "November",
    "Dec": "December"

}

print(monthConversion["Nov"]) #sau
print(monthConversion.get("Luv","nu exista"))