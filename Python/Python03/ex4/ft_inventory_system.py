import sys

if __name__ == "__main__":
    inventory = dict()

    for arg in sys.argv[1:]:
        parts = arg.split(':')
        if len(parts) == 2:
            name = parts[0]
            try:
                qty = int(parts[1])
                inventory[name] = inventory.get(name, 0) + qty
            except ValueError:
                pass

    print("=== Inventory System Analysis ===")
    total_items = 0
    for val in inventory.values():
        total_items += val

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}\n")

    print("=== Current Inventory ===")
    items_list = []
    for k, v in inventory.items():
        items_list += [(k, v)]

    n = len(items_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if items_list[j][1] < items_list[j+1][1]:
                items_list[j], items_list[j+1] = items_list[j+1], items_list[j]

    for k, v in items_list:
        pct = (v / total_items) * 100 if total_items > 0 else 0
        unit_str = "unit" if v == 1 else "units"
        print(f"{k}: {v} {unit_str} ({pct:.1f}%)")
    print()

    print("=== Inventory Statistics ===")
    most_abundant_k, most_abundant_v = "", -1
    least_abundant_k, least_abundant_v = "", -1

    for k, v in inventory.items():
        if most_abundant_v == -1 or v > most_abundant_v:
            most_abundant_v = v
            most_abundant_k = k
        if least_abundant_v == -1 or v < least_abundant_v:
            least_abundant_v = v
            least_abundant_k = k

    unit_str_most = "unit" if most_abundant_v == 1 else "units"
    unit_str_least = "unit" if least_abundant_v == 1 else "units"
    print(
        f"Most abundant: {most_abundant_k} "
        f"({most_abundant_v} {unit_str_most})")
    print(
        f"Least abundant: {least_abundant_k} "
        f"({least_abundant_v} {unit_str_least})\n")

    print("=== Item Categories ===")
    categories = dict()
    categories.update({'moderate': dict()})
    categories.update({'scarce': dict()})

    for k, v in inventory.items():
        if v >= 5:
            categories.get('moderate').update({k: v})
        else:
            categories.get('scarce').update({k: v})

    print(f"Moderate: {categories.get('moderate')}")
    print(f"Scarce: {categories.get('scarce')}\n")

    print("=== Management Suggestions ===")
    restock_str = ""
    is_first = True
    for k, v in inventory.items():
        if v == 1:
            if not is_first:
                restock_str += ", "
            restock_str += k
            is_first = False
    print(f"Restock needed: {restock_str}\n")

    print("=== Dictionary Properties Demo ===")
    keys_str = ""
    is_first_key = True
    for k in inventory.keys():
        if not is_first_key:
            keys_str += ", "
        keys_str += k
        is_first_key = False

    vals_str = ""
    is_first_val = True
    for v in inventory.values():
        if not is_first_val:
            vals_str += ", "
        vals_str += f"{v}"
        is_first_val = False

    print(f"Dictionary keys: {keys_str}")
    print(f"Dictionary values: {vals_str}")

    sample_key = 'sword'
    print(
        f"Sample lookup - '{sample_key}' in "
        f"inventory: {sample_key in inventory}")
