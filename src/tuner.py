import numpy as np

from pymoo.algorithms.nsga2 import NSGA2
from pymoo.model.problem import Problem
from pymoo.optimize import minimize

from carlsat import run_carlsat
from helper import inform


file = None
timer = 0
generation = 0


class ProblemWrapper(Problem):
    def _evaluate(self, designs, out, *args, **kwargs):
        global generation
        inform("Running CarlSAT executable..")
        results = []  # store the results of each mutation
        counter = 0

        for design in designs:  # a design is a specific configuration or an a list/array of the parameters
            inform("Generation: %i" % generation)
            inform("Population: %i" % counter)
            results.append(run_carlsat(file, timer, design))  # design parsed into CarlSAT caller to its get score
            counter += 1

        out['F'] = np.array(results)  # output from CarlSAT
        generation += 1


def tune(filename, timeout):
    global file, timer
    file = filename
    timer = timeout

    inform("Building model..")
    defined_problem = ProblemWrapper(n_var=9, n_obj=1, xl=[1, 10, 1, 0.1, 0.1, 0, 1, 1, 1],
                                     xu=[1000, 1000000, 1000, 1000, 1000, 100, 1000, 10000, 3])

    inform("Using NSGA2 algorithm for model..")
    # Initialize the algorithm NSGA2 with population 1024
    nsga2_algorithm = NSGA2(pop_size=32)

    inform("Setting model to run for 32 generations with population size of 32")
    # Termination condition: stop after 3 generations
    stop_criteria = ('n_gen', 32)

    # Utilise the minimize function to all the work
    solutions = minimize(problem=defined_problem, algorithm=nsga2_algorithm, termination=stop_criteria)

    # Solutions can be access like this 'solutions.F'
    # Is an object of some sort but it is not really defined
    inform("Solution is converging to %i" % solutions.F[0])
