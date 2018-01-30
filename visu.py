import matplotlib.pyplot as plt

x = []
#= [2,4,3,5,7,6,2,7,9,1]
z= []
m= 1

x1 =[1,2,3,4,5]
y1 = [4,6,7,1,8]

for i in range(10):
    x.append(i)
    z.append(int(m)*int(i % 2))

print(z)


plt.bar(x,z , label = 'first line',color= 'red')
plt.bar(x1,y1, label = 'second line',color = 'yellow')

plt.xlabel('thek axis')
plt.ylabel('tupppo axis')
plt.title('learn graphs')
plt.legend()
plt.show()


