"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
        "input": [["PATO", "PELE"]],
        "answer": [1, 1]
    },
    {
        "input": [["ANJO", "MENTORA"]],
        "answer": [4, 5]
    },
    {
        "input": [["MENTORA", "ANJO"]],
        "answer": [7, 1]
    },
    {
        "input": [["URUBU", "POLIVALENTE"]],
        "answer": [-1, -1]
    },
    {
        "input": [["ATRITO", "TRUTA"]],
        "answer": [5,4]
    }
    ]
}
