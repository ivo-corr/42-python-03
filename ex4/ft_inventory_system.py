import sys

if __name__ == "__main__":
    items = {}
    print("=== Inventory System Analysis ===")
    if (len(sys.argv) == 1):
        print("No items provided. Usage: "
              "python3 <item1>:<qty1> <item2>:<qty2>...")
        exit()
    for i in sys.argv[1:]:
        try:
            k, v = i.split(":")
            if k in items:
                print(f"Redundant item '{k}' - discarding")
                continue
            v = int(v)
            items[k] = v
        except ValueError as e:
            split_value = i.split(":")
            if (len(split_value) == 1):
                print(f"Error - invalid parameter '{i}'")
            else:
                print(f"Quantity error for '{split_value[0]}': {e}")
    print(f"Got inventory: {items}")
    print(f"Item list: {[k for k in items]}")
    total_items = sum(value for value in items.values())
    print(f"Total quantity of the {len(items)} items: {total_items}")
    highest = ""
    lowest = ""
    for k in items:
        percentage = round((items[k] / total_items) * 100, 1)
        if (highest == "" or items[k] > items[highest]):
            highest = k
        if (lowest == "" or items[k] < items[lowest]):
            lowest = k
        print(f"Item {k} represents: {percentage}%")
    print(f"Item most abundant: {highest} with quantity {items[highest]}")
    print(f"Item least abundant: {lowest} with quantity {items[lowest]}")
    items.update({"magic_item": 1})
    print(f"Updated inventory: {items}")
