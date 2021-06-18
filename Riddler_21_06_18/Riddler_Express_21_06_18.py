from scipy.special import binom


def score_a_frame(a: int, b: int, c: int):
    if a == b - 1 and b == c - 1:
        return 60
    if a == b - 1 or b == c - 1:
        return 40
    return 30


def count_frames():
    score = 0
    for a in range(8):
        for b in range(a + 1, 9):
            for c in range(b + 1, 10):
                score += score_a_frame(a, b, c)
    return score / binom(10, 3)


if __name__ == "__main__":
    print(count_frames())
