class ShoppingList:
    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.items = []

    def add_items(self,items):
        self.items.append(items)

content_list1 = ['Milk', 'Soda', 'Fish']
list1 = ShoppingList('Fiesta','clown fiesta!')
list1.add_items(content_list1)

content_list2 = ['Paper', 'Napkins', 'Plate', 'Chips']
list2 = ShoppingList('walmart','wallyworld!')
list2.add_items(content_list2)

content_list3 = ['Chicken', 'Beef', 'Eggs', 'Sugar', 'Salt', 'Pepper', 'Honey' ]
list3 = ShoppingList('sams club','babby seals!')
list3.add_items(content_list3)

print(list1.title,list1.description)
for item in list1.items:
    print(item)

print(list2.title,list2.description)
for item in list2.items:
    print(item)

print(list3.title,list3.description)
for item in list3.items:
    print(item)
