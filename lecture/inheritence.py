class Store:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        print("My store")

    def open(self):
        print("open")

shoe_store = Store("my shoe store", "1000 street street")
shoe_store.open()

print(shoe_store.name)
