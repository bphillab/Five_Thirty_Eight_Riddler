optimal_strategy = {}


def find_optimal_strategy(x: set):
    if str(set(sorted(x))) in optimal_strategy.keys():
        return optimal_strategy[str(x)]
    else:
        not_in_x = {i for i in range(1, 10) if i not in x}
        optimal_strategy[str(set(sorted(x)))] = max(sum([find_optimal_strategy(set(sorted(x.union({i})))) for i in
                                                         not_in_x]
                                                        ) / (len(not_in_x) + 1),
                                                    sum(x))
        return optimal_strategy[str(set(sorted(x)))]


if __name__ == "__main__":
    print("Best you can do: ", find_optimal_strategy(set()))
