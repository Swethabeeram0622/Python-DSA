# Linear search
def search(list,key):
    for i in range(len(list)):
        if key == list[i]:
            print("element found", i)
            break
    else:
      print("element not found")

list=(34, 20, 15, 16, 17)
print(list)
key = int(input("enter a key: "))
search(list,key)
