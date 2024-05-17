#Write a program to create and manage a shopping list
# Allow users to add items, remove items, and display the list.
class Shopping_list:
    def __init__(self,item =None):
        self.item = item
        self.m=[]
    def add_item(self):
        p =int(input("how many item you want to add"))
        for i in range(p):
            t = input("enter the name of the product which you want from shop")
            self.m.append(t)

    def display_item(self):
        print("the shopping item list is here:")
        for i in range(len(self.m)):
            print(i+1,self.m[i])
    def remove_items(self):
        t = input("which item you want to remove from the list")
        self.m.remove(t)
s = Shopping_list()
s.add_item()
s.display_item()
s.remove_items()
s.display_item()
