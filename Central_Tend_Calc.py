# Find CENTRAL TENDENCIES of a dataset

print("\n** ENTER ALL THE DATAS BELOW AND GET YOUR CENTRAL TENDENCIES **\n")
dataset = []
print("\nEnlist your elements (datas) below\tENTER 00 TO STOP ENTERING DATA.\n")
k = True
index = 0
while (k != 00):
    k = int(input(f"Enter element {index+1} - "))
    dataset.append(k)
    index += 1
dataset.remove(dataset[index-1])
datasets = list(set(dataset))
k2 = len(datasets)
n = len(dataset)
print(f'\nYour DataSet is {dataset}\n')
print(f'\nLength of DataSet is {len(dataset)}\n')
mean1 = sum(dataset)/len(dataset)
mean = round(mean1,2)
print(f'Mean of given dataset is {mean}\n')
dataset.sort
median = True
if (len(datasets)%2 != 0):
    median = datasets[int((k2+1)/2)]
else :
    median = (datasets[int(k2/2)] + datasets[int(k2/2)+1])/2
print(f'Median of given dataset is {median}\n') 
counts = []
for m in dataset:
    o = dataset.count(m)
    counts.append(o)
counts.sort()
z = max(counts)
for p in dataset:
    if (dataset.count(p) >= z):
        mode = p
print(f'Mode of given dataset is {mode}\n')
k = 0
for j in dataset:
    k = k + ((j-mean)**2)
variance = round((k/n),3)
print(f"Variance of given dataset is {variance}\n")
sd = round((variance**(0.5)),3)
print(f"Standard Deviation of given dataset is {sd}\n")
print("Thank You -\n\tGodARD")
