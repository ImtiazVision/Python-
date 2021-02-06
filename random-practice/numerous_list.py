available_items = ['rice','bean','potato','pizza']

demanded_items = ['pizza','chicken_nuggets','chicken_wings']

for item in available_items:
    if demanded_items in available_items:
        print("Cool! " + demanded_items + "will be served :)")
    else:
        print("Sorry, we don't have the item " + item )