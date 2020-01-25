"""Riddler Classic
From Dean Ballard comes another coin-related challenge — a game of “Pinching Pennies”:

The game starts with somewhere between 20 and 30 pennies, which I then divide into two piles any way I like. Then we
alternate taking turns, with you first, until someone wins the game. For each turn, a player may take any number of
pennies he or she likes from either pile, or instead take the same number of pennies from both piles. Each player
must also take at least one penny every turn. The winner of the game is the one who takes the last penny.

If we both play optimally, what starting numbers of pennies (again, between 20 and 30) guarantee that you can win the
game?

"""
import collections
import functools


# Memoization class from: https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


@memoized
def nim_solver(current_player, num_p_1, num_p_2):
    if num_p_1 == 0 and num_p_2 == 0:
        return 1 - current_player
    potential_moves_results = [nim_solver(1 - current_player, num_p_1 - i, num_p_2) for i in range(1, num_p_1 + 1)] + [
        nim_solver(1 - current_player, num_p_1, num_p_2 - i) for i in range(1, num_p_2 + 1)] + [
                                  nim_solver(1 - current_player, num_p_1 - i, num_p_2 - i) for i in
                                  range(1, min(num_p_1, num_p_2) + 1)]
    if current_player == 1:
        return max(potential_moves_results)
    if current_player == 0:
        return min(potential_moves_results)


if __name__ == "__main__":
    for num_pennies in range(20, 31):
        for i in range(num_pennies + 1):
            if nim_solver(1, i, num_pennies - i) == 0:
                print("Solution found: ", num_pennies, " divided ", i, " and ", num_pennies - i)
