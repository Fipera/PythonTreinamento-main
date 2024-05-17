import pandas as pd
import numpy as np


notasAluno_DataFrame = pd.DataFrame({
    "Nome": ["Ana", "Pedro", "João"],
    "Nota 1": [9, 7, 10],
    "Nota 2": [6, 9, 8],
    "Nota 3": [7, 5, 10],
    "Nota 4": [10, 10, 6]
})

novaColunaFaltas = [2, 5, 3]

notasAluno_DataFrame["Faltas"] = novaColunaFaltas

notasAluno_DataFrame.loc[1, "Nota 2"] = 50

notasAluno_DataFrame["Media"] = (notasAluno_DataFrame["Nota 1"] + notasAluno_DataFrame["Nota 2"] + notasAluno_DataFrame["Nota 3"] + notasAluno_DataFrame["Nota 4"]) / 4


print(notasAluno_DataFrame)