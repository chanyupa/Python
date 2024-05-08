mark = 40
grade = int(input('Your marks:'))
if grade >= 90:
    print('A grade')
elif grade >= 80:
    print('B grade')
elif grade>= 70:
    print('C grade')
elif grade >= 50:
    print('D grade')
elif grade >= 40:
    print('E grade')
else:
    print('Failing grade')

list1 = [1,2,3,4,5]
for n in list1:
    print (n);

number = [1,2,3,4,5]

sum = 0
for num in number:
    sum = sum+num

print('The sum is', sum)

for i in range(100,0,-10):
    print(i)

color = ['yellow', 'blue', 'red', 'green']

for item in range(len(color)):
    color.append('pink')
print(color)
num=[]
for i in range(10):
    num.append(i)
print(num)

name = 'nang'
for i in name:
    print(i)
lis=[(10,11),(12,13),(14,15)]
for turple in lis:
    print(turple)
for (t,q) in lis:
    print(t)
for (t,q) in lis:    
    print(q)

dict = {'name': 'nang' , 'age': 20, 'gender':'female'}
print(dict.items())
for key , value in dict.items():
    print(key)
    print(value)
