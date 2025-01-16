#Area of a flower
#name - Karthikeya Telapalli
#UID - U04125021
#Description 
#This program computes the area of a flower which consists of a square and four semicircles




r = float(input("Enter the radius of the flower: "))

#By using input function the program takes user input for the radius value

PI = 3.14159
square_area = r*r
semicircle_area = PI * r * r / 8

#as the radius of circle is r/2 the semicircle area becomes pir^2/8

flower = square_area + 4* semicircle_area

#area of flower is the sum of the square area and 4 times the semicircle area as there are 4 semi circles

print("The area of flower is" , flower , "square units")
