from scipy.special import binom


def calc_num_slots(i_start, i_end):
    return i_end - i_start - 1


def prob_accident(num_intersections):
    i_start = 0
    num_configs = 0
    nonintersecting = 0
    for i_end in range(1, num_intersections):
        num_slots = calc_num_slots(i_start, i_end)
        refl_num_slots = num_intersections - num_slots - 2
        num_configs += (num_intersections - 1) ** 2
        nonintersecting += 2 * (binom(num_slots, 2) + binom(refl_num_slots, 2))
    return num_configs, nonintersecting, nonintersecting / num_configs


if __name__ == "__main__":
    print(prob_accident(8))
