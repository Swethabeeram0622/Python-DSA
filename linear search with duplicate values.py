# to append duplicate values in list1
def duplicate(arr,key):
    list1=[]
    for i in range(len(arr)):
        if arr[i] == key:    
            list1.append(i)
    if list1:          # if not empty
        print(f"element {key} is found at list1 {list1}")        
    else:
      print("element not found")
arr =list(map(int, input().split()))
key = int(input("enter a key: "))
duplicate(arr,key)
