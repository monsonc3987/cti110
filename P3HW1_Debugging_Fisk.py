# I was supposed to put a comment here
# Fisk


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = input('Enter grade for Module 1: ')
mod_2 = input('Enter grade for Module 2: ')
mod_3 = input('Enter grade for Module 3: ')
mod_4 = input('Enter grade for Module 4: ')
mod_5 = input('Enter grade for Module 5: ')
mod_6 = input('Enter grade for Module 6: ')

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades
for i in range(0, len(grades)):
   grades[i] = float(grades[i])
low = min(grades)
high = max(grades)
sum = sum(grades)
avg = round(sum/len(grades),2)

print('-----------Results----------')
print(f'Lowest Grade:     {low}')
print(f'Highest Grade:    {high}')
print(f'Sum of Grades:    {sum}')
print(f'Average:          {avg}')
print('----------------------')
# determine letter grade for average

if avg >= 90:
    print('Your grade is: A')

elif avg >= 80:
 print('Your grade is: B')

elif avg >= 70:
   print('Your grade is: C')

else:
    print('Your grade is: F')



