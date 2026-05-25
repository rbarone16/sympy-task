import sympy
from sympy import diff, Dict
from sympy import symbols
from sympy import series
# Controlla il file readme.md per i dettagli su ciascun sub-task

def calcola_derivata(espressione: str, variabile: str) -> sympy.Expr:
    """Sub-task 1: Calcolare una Derivata."""
    print("Rispetto quale variabile stai derivando?")
    x = symbols(input("Inserisci variabile: "))
    print("Quale è la tua funzione?")
    expr = input("Inserisci la tua funzione: ")
    df = diff(expr,x)
    print(f"La derivata della funzione inserita è:\n{df}")
    print("")
    pass

def calcola_integrale_definito(espressione: str, variabile: str, estremo_inf: float, estremo_sup: float) -> sympy.Expr:
    """Sub-task 2: Calcolare un Integrale Definito."""
    a = estremo_inf
    b = estremo_sup
    expr = espressione
    x = variabile
    integral = sympy.integrate(expr, (x, a, b))
    return(integral)

    pass

def calcola_limite(espressione: str, variabile: str, punto: str) -> sympy.Expr:
    """Sub-task 3: Calcolare un Limite."""
    expr = espressione
    x = variabile
    x_0 = punto
    val = sympy.limit(expr, x, x_0)
    return(val)
    pass

def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sympy.Expr:
    """Sub-task 4: Calcolare una Serie di Taylor."""
    ess = espressione
    x = variabile
    z = punto
    n = ordine
    somm = series(ess,x,z,n,"+")
    return(somm)
    pass

def risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str):
    """Sub-task 5: Risolvere un Sistema Lineare."""
    pass

def main():
    print("Sub-task 1:", calcola_derivata("x**3 + 2*x", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x**2", "x", 0, 3))
    print("Sub-task 3:", calcola_limite("sin(x)/x", "x", "0"))
    print("Sub-task 4:", calcola_polinomio_taylor("exp(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()

