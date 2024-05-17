import pandas as pd
import numpy as np



# dataFrame_Meses = pd.date_range("20221201", periods=12, freq="ME")

# print(dataFrame_Meses)

# numerosAleatorios = pd.DataFrame(np.random.rand(6,2))
# print(numerosAleatorios)

notasAlunos_DF =pd.DataFrame({
     "Nome": ["Ana", "Joao", "Pedro"],
     "Media": [9, 7, 10]

})

print(notasAlunos_DF)