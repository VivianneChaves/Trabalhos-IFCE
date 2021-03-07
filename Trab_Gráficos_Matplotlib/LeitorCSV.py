import csv
import matplotlib.pyplot as plt

#path do arquivo csv
arquivo= r'C:\\Users\vivia\\Documents\\Trabalhos-IFCE\\Trab_Gráficos_Matplotlib\\Boletim.csv'

notas = []
bimestres = []

# Abertura e carga do arquivo csv em um objeto csv_reader
with open(arquivo) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        notas.append(int(row[0]))
        bimestres.append(row[1])

# VERIFICAÇÃO DOS DADOS
print(notas)
print(bimestres)

# GRAFICO DE LINHAS
plt.title("BOLETIM DE NOTAS")
plt.xlabel("BIMESTRES")
plt.ylabel("NOTAS")
plt.plot(bimestres, notas, label = "Notas")
plt.scatter(bimestres, notas)
plt.legend()
plt.show()

# GRAFICO DE COLUNAS
plt.title("BOLETIM DE NOTAS")
plt.xlabel("BIMESTRES")
plt.ylabel("NOTAS")
plt.bar(bimestres, notas, label = "Notas")
plt.legend()
plt.show()

# GRAFICO DE PIZZA
plt.title('BOLETIM DE NOTAS')
plt.xlabel("BIMESTRES")
plt.pie(notas, labels = bimestres, autopct = "%1.0f%%")
plt.show()     


