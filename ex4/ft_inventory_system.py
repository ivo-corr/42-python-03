import sys

if __name__ == "__main__":
    items = {}
    print("=== Inventory System Analysis ===")
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
    print()
