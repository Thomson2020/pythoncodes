from pandas import DataFrame

headers = ['Roll.No', 'Name', 'Marks-Sub1', 'Marks-Sub2', 'Total']
data = [['1', 'Zeus',       '60', '90', ''],
        ['2', 'Horos',      '30', '10', ''],
        ['3', 'Perseus',    '20', '20', ''],
        ['4', 'Athena',     '70', '30', ''],
        ['5', 'Hades',      '70', '40', ''],
        ['6', 'Apollo',     '80', '50', ''],
        ['7', 'Zagreus',    '90', '60', ''],
        ['8', 'Chaos',      '100','70', ''],
        ['9', 'Aphrodite',  '75', '80', ''],
        ['10','Hercules',   '68', '90', '']]

# Calculate the total and update the 'Total' column
for d in range(len(data)):
    data[d][4] = int(data[d][3]) + int(data[d][2])

df = DataFrame(data, columns=headers)
print(df.to_markdown(index=False))

# Sort the data based on the 'Total' column
for i in range(len(data) - 1, 0, -1):
    for j in range(i):
        if data[j][4] > data[j + 1][4]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp

df1 = DataFrame(data, columns=headers)
print()
print(df1.to_markdown(index=False))

# Print the value at the second row and third column
print(data[1][2])
