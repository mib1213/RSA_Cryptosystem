import random

def teiler(n: int) -> list[int]:
    if ist_primzahl(n):
        return [n]
    teiler: list[int] = [i for i in range(2, n // 2 + 1) if n % i == 0]
    teiler.append(n)
    return teiler

def teiler_fremde_zahlen(phi: int) -> list[int]:
    phi_teiler: list[int] = teiler(phi)
    return [i for i in range(2, phi) if not (set(phi_teiler) & set(teiler(i)))]

def multiplikative_inverse(e: int, phi: int, N: int) -> int:
    d: int = 2
    while True:
        if e*d % phi == 1:
            if (d != e) & (d != N):
                return d
        d += 1

def ist_primzahl(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def zufällige_primzahl(von: int, bis: int, außer: int | None = None) -> int | None:
    primzahlen: list[int] = [number for number in range(von, bis + 1) if ist_primzahl(number)]
    if außer:
        primzahlen.remove(außer)
    if primzahlen:
        return random.choice(primzahlen)
    return None

def verschlüsseln(m: int, e: int, N: int) -> int:
    return (m**e) % N

def entschlüsseln(c: int, d: int, N: int) -> int:
    return (c**d) % N

def kontrolle(e: int, d: int, N: int) -> bool:
    for i in  range(2, N):
        if entschlüsseln(verschlüsseln(i, e, N), d, N) != i:
            return False
    return True