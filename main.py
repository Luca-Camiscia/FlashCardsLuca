import json
import random

# Archivo para guardar las flashcards
FILE_NAME = "flashcards_Economia.json"

# Cargar flashcards desde el archivo
def load_flashcards():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Guardar flashcards en el archivo
def save_flashcards(flashcards):
    with open(FILE_NAME, "w") as file:
        json.dump(flashcards, file, indent=4)

# Agregar nuevas flashcards
def add_flashcard(flashcards):
    question = input("Escribe la pregunta: ")
    answer = input("Escribe la respuesta: ")
    flashcards.append({"question": question, "answer": answer})
    save_flashcards(flashcards)
    print("¡Flashcard agregada!")

# Practicar flashcards
def practice_flashcards(flashcards):
    if not flashcards:
        print("No hay flashcards disponibles. ¡Agrega algunas primero!")
        return
    
    random.shuffle(flashcards)
    for card in flashcards:
        print("\nPregunta:", card["question"])
        input("Presiona Enter para ver la respuesta...")
        print("Respuesta:", card["answer"])
        input("Presiona Enter para continuar...")

# Menú principal
def main():
    flashcards = load_flashcards()
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar Flashcard")
        print("2. Practicar Flashcards")
        print("3. Salir")
        choice = input("Selecciona una opción: ")
        
        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            practice_flashcards(flashcards)
        elif choice == "3":
            print("¡Hasta luego puto!!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
