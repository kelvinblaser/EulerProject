"""Euler 938 - Exhausting a Color"""

class CardProbability:
    def __init__(self, R: int, B: int):
        # self._probability = [[0.0] * (B + 1) for _ in range(R+1)]
        # for b in range(1, B + 1):
        #     self._probability[0][b] = 1.0
        #     self._probability[1][b] = 0.0
        prob_r_minus_2 = [1.0] * (B + 1)
        prob_r_minus_1 = [0.0] * (B + 1)
        for r in range(2, R+1):
            prob_r = [0.0] * (B + 1)
            if r % 1000 == 0:
                print(f'r = {r} out of {R}')
            for b in range(1, B + 1):
                rr = r * (r - 1)
                rb2 = 2 * r * b
                d = rr + rb2
                prob_r[b] = (rr / d) * prob_r_minus_2[b] + (rb2 / d) * prob_r[b-1]
            prob_r_minus_2 = prob_r_minus_1
            prob_r_minus_1 = prob_r
        self.solution = prob_r_minus_1[B]

    def __call__(self):
        return self.solution
    

def P(R: int, B: int) -> float:
    return CardProbability(R, B)()

if __name__ == '__main__':
    for R, B in [(2, 2), (10, 9), (34, 25), (24690, 12345)]:
        print(f'P({R}, {B}) = {P(R, B)}')


"""
r^2 = (r-4)^2 + 8^2
    = r^2 - 8r + 16 + 64

8r = 80
r = 10
"""