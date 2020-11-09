from typing import List

class Agent:
    def __init__(self, options: List[float]):
        self.options = options

    def value(self, option: int) -> float:
        return self.options[option]


def isParetoImprovement(agents: List[Agent], option1: int, option2: int) -> bool:
    pareto = False
    for a in range(0, len(agents)):
        if agents[a].value(option1) < agents[a].value(option2):
            return False
        if agents[a].value(option1) > agents[a].value(option2):
            pareto = True
    return pareto


def isParetoOptimal(agents: List[Agent], option: int, allOptions: List[int]) -> bool:
    for a in range(0, len(allOptions)):
        if isParetoImprovement(agents, allOptions[a], option):
            return False
    return True

# function that print all the agents and their options
def printAgentArray(agents: List[Agent]):
    print("\nagent ", end="")
    for i in range(0, len(agents[0].options)):
        print("| option", i+1, end=" ")
    for a in range(0, len(agents)):
        print("\n  ", a, end="  ")
        for b in agents[a].options:
            print("|   ", b, end="     "),
    print("\n")

# function that builds an example of agent and options lists
def listsBuild() -> (List[Agent], List[int]):
    ami = Agent([1, 2, 3, 4, 5])
    tami = Agent([3, 1, 2, 5, 4])
    rami = Agent([3, 5, 5, 1, 1])
    agents = [ami, tami, rami]
    alloptions = [0, 1, 2, 3, 4]
    return agents, alloptions

# in the main we can see a specific example of the functions
def main():
    print("Assignment 3 ,Question 5")
    agents, allOptions = listsBuild()
    printAgentArray(agents)

    print("Part A:")
    for i in range(0, len(allOptions)):
        for j in range(0, len(allOptions)):
            print("Option", i+1, "is Pareto Improvement of option", j+1, "?:", isParetoImprovement(agents, i, j))

    print("\nPart B:")
    for i in range(0, len(allOptions)):
        print("Option", i+1, "is Pareto Optimal ?:", isParetoOptimal(agents, i, allOptions))


if __name__ == "__main__":
    main()
