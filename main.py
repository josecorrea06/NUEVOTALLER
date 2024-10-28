import json
import os

# Nombre del archivo donde se guardan los contactos
FILENAME = 'contacts.json'

# Función para cargar contactos desde el archivo JSON
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []

# Función para guardar contactos en el archivo JSON
def save_contacts(contacts):
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file, indent=4)

# Función para añadir un nuevo contacto
def add_contact(contacts):
    name = input("Ingrese el nombre del contacto: ")
    phone = input("Ingrese el teléfono del contacto: ")
    email = input("Ingrese el correo electrónico del contacto: ")
    
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contacto '{name}' añadido exitosamente.")

# Función para actualizar un contacto existente
def update_contact(contacts):
    name = input("Ingrese el nombre del contacto que desea actualizar: ")
    for contact in contacts:
        if contact['name'] == name:
            phone = input("Ingrese el nuevo teléfono (deje en blanco para no cambiar): ")
            email = input("Ingrese el nuevo correo electrónico (deje en blanco para no cambiar): ")
            
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            
            save_contacts(contacts)
            print(f"Contacto '{name}' actualizado exitosamente.")
            return
    
    print(f"Contacto '{name}' no encontrado.")

# Función para eliminar un contacto
def delete_contact(contacts):
    name = input("Ingrese el nombre del contacto que desea eliminar: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"Contacto '{name}' eliminado exitosamente.")
            return
    
    print(f"Contacto '{name}' no encontrado.")

# Función para mostrar todos los contactos
def show_contacts(contacts):
    if not contacts:
        print("No hay contactos registrados.")
        return
    print("\nLista de contactos:")
    for contact in contacts:
        print(f"Nombre: {contact['name']}, Teléfono: {contact['phone']}, Correo: {contact['email']}")
    print()

# Menú principal
def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Menú ---")
        print("1. Añadir contacto")
        print("2. Actualizar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar contactos")
        print("5. Salir")
        
        choice = input("Seleccione una opción (1-5): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            update_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            show_contacts(contacts)
        elif choice == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
