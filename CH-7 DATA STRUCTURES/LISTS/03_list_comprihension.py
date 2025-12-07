# a=5
# table=[]
# for i in range(1,11):
#     table.append(a*i)

table=[5*i for i in range(1,11)]
print(table)



squared = [x**2 for x in range(5)]
print(squared)  # Output: [0, 1, 4, 9, 16]