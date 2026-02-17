def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    if not day:
        return

    def count_up(count):
        if count > day:
            print("Harvest time!")
            return
        print(f"Day {count}")
        count_up(count + 1)
    count_up(1)
