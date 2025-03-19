import statistics

def app():
    num = int(input("Inserta el numero de calificaciones: "))
    cont = []
    for i in range(num):
        cal = int(input(f"Inserta calificacion {i+1}: "))
        cont.append(cal)
    cont.sort()
    prom = sum(cont)
    prom = prom / len(cont)
    med = statistics.median(cont)
    print(f"Promedio: {prom}")
    print(f"Mediana: {med}")
    print(f"Calificación minima: {min(cont)}")
    print(f"Calificación máxima: {max(cont)}")
    
if __name__ == "__main__":
    app()