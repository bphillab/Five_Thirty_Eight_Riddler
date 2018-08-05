def calculate_non_water_weight(total_weight, percent):
    return (1-percent)*total_weight


def calculate_new_weight(non_water_weight, percent):
    return non_water_weight/(1-percent)

if __name__ == "__main__":
    non_water_weight = calculate_non_water_weight(1000,.99)
    new_weight = calculate_new_weight(non_water_weight,.98)
    print(new_weight)