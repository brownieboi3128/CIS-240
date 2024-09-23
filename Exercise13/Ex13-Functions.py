#Christian Brown

def gradecenter(name, score):
    """uses positional arguments to print the name and score of an exersice

    Args:
        name (string): name of the exersice
        score (string): score of the exersice
    """
    print("Exersice name: " + name)
    print("Score: " + score)

def gradecenterKwargs(name, score):
    """uses keyword arguments to print the name and score of an exersice

    Args:
        name (string): name of the exersice
        score (string): score of the exersice
    """
    print("\nExersice name: " + name)
    print("Score: " + score)

def gradecenterVarargs(name, score, **kwargs):
    """uses variable arguments to print the name and score of an exersice

    Args:
        name (string): name of the exersice
        score (string): score of the exersice
    """
    print("\nExersice name: " + name)
    print("Score: " + score)
    print("Exersice ID: " + kwargs["exersiceID"])

def run():
    gradecenter("Functions", "100")
    gradecenterKwargs(name = "Funtions",
                      score = "100")
    gradecenterVarargs(name = "Funtions",
                       score = "100",
                       exersiceID = "13")

run()