def zellerCongruence():
    # month number
    m = (int(input("Enter a month number: ")));
    # date 
    q = (int(input("Enter a date: ")));
    # year
    y = (int(input("Enter a year: ")));
    
    # Algorithm adjustment for January and February
    if (m == 1 or m == 2): 
        m += 12;
        y -= 1;
     
    # Zeller's Congruence formula   
    h = int(q + (13 * (m + 1) / 5) + y + (y / 4) - (y / 100) + (y / 400)) % 7;
    
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
    
    print(m, q, y," is on a", days[h], ".");
    
def leapYear():
    # year
    y = (int(input("Enter a year: ")));
    if (y % 400 == 0 or y % 100 != 0):
        if (y % 4 == 0):
            print(y, "is a leap year.");
        else:
            print(y, "is not a leap year.");

prompt = int(0) 

# menu prompt
while (prompt != 3):
    print("1. Calculate the day of the week for any calendar date.");
    print("2. Calculate a leap year.");
    print("3. Exit program");
    prompt = int(input("Select an option: "));
    if (prompt == 1): zellerCongruence();
    if (prompt == 2): leapYear();


