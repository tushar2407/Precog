import matplotlib.pyplot as plt 

file = open("lis.txt", "r+")
d = eval(file.read())
d = sorted(d, key= lambda x : x[0], reverse=True)
d = d[:10]
x = [i[1] for i in d]
y = [i[0] for i in d]
print(x)
print(y)
plt.plot(x,y)
plt.bar(x, y, alpha=0.2)
plt.xlabel('Tags') 
plt.ylabel('Number of questions') 
plt.xticks(x, [str(i) for i in x], rotation=45)

plt.tick_params(axis='x', which='major', labelsize=10)

plt.tight_layout()
plt.savefig('tags.png')

plt.show()