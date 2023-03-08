rows = int(input("Enter rows quantity: "))
fur_tree = ""
for i in range(rows):
    fur_tree += (rows - 1 - i) * " " + (2 * i + 1) * "*" + (rows - 1 - i) * " " + "\n"
print(fur_tree)
