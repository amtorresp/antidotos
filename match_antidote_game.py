# -*- coding: utf-8 -*-
import random


def main():
    pairs = {
        "Paracetamol": "N-acetilcisteína",
        "Heparina": "Protamina",
        "Benzodiacepinas": "Flumazenilo",
        "Opioides": "Naloxona",
        "Intoxicación por hierro": "Deferoxamina",
    }

    drugs = list(pairs.keys())
    antidotes = list(pairs.values())
    random.shuffle(drugs)
    random.shuffle(antidotes)

    print("Une cada fármaco con su antídoto escribiendo el número correspondiente de la lista de antídotos.")
    print()
    print("Fármacos:")
    for idx, drug in enumerate(drugs, 1):
        print(f"  {idx}. {drug}")
    print()
    print("Antídotos:")
    for idx, antidote in enumerate(antidotes, 1):
        print(f"  {idx}. {antidote}")
    print()

    score = 0
    for drug in drugs:
        ans = input(f"Antídoto para '{drug}': ")
        try:
            choice = int(ans)
            if 1 <= choice <= len(antidotes):
                selected = antidotes[choice - 1]
                if pairs[drug] == selected:
                    print("¡Correcto!\n")
                    score += 1
                else:
                    print(f"Incorrecto. El antídoto es {pairs[drug]}.\n")
            else:
                print("Número fuera de rango. Se cuenta como incorrecto.\n")
        except ValueError:
            print("Entrada no válida. Se cuenta como incorrecto.\n")

    print(f"Puntuación final: {score} de {len(drugs)}")


if __name__ == "__main__":
    main()
