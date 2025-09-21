def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles /0.621371

def c_to_f(celsius):
    return (celsius *9/5)+32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Unit converter")
print("1. Kilometer to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = input("Pilih conversion (1-4): ")

try:
    if choice =='1':
        km = float(input("Masukin kilometer: "))
        print(f"{km} km = {km_to_miles(km):2f} miles")
    elif choice =='2':
        miles = float(input("Masukin miles: "))
        print(f"{miles} miles = {miles_to_km(miles):.2f} km")
    elif choice == '3':
        c = float(input("Masukin Celcius: "))
        print(f"{c}C ={c_to_f(c):.2f}F")
    elif choice =='4':
        f = float(input("Masukin Fahrenheit: "))
        print(f"f{f}F = {f_to_c(f):.2f}C")
    else:
        print("Pilihan salah")
except ValueError:
    print("Masukin angka yg bener")