###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    #if target weight is equal to zero, then zero eggs can be chosen. no room in ship.

    if target_weight == 0:
        number_of_eggs = 0
    #see if the solution at that weight has already been calculated
    elif target_weight in memo:
        #if so, set number of eggs equal to solution
        number_of_eggs = memo[target_weight]
    #if not, go through each available egg weight
    else:    
        for egg_weight in egg_weights:
            #is target weight > egg weight? can we pick this egg?
            if target_weight >= egg_weight:
                #reduce available weight by egg weight amount
                #recall function using remaining weight and find solution for that
                number_of_eggs = dp_make_weight(egg_weights, target_weight - egg_weight, memo)
                #add one more egg to number of eggs chosen for current egg
                number_of_eggs += 1
                #is this number best number we can take at that target weight? 
                #if not, store to memo at that target weight.
                if target_weight not in memo:
                    memo[target_weight] = number_of_eggs
                elif number_of_eggs < memo[target_weight]:
                    memo[target_weight] = number_of_eggs
        #return number of eggs chosen
    return number_of_eggs

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 10
    print("Egg weights = (1, 5, 10, 25)")
    print("n =", n)
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()