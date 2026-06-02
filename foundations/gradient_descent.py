class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        if iterations == 0:
            return init
        minimizer = 0
        while iterations > 0:
            minimizer = init - learning_rate * 2 * init
            init = minimizer
            iterations = iterations - 1
        return round(minimizer, 5)
