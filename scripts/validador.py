# Script de prueba: Validador de variables industriales (Tags)

def validar_tag(nombre_tag):
    # En Siemens, las variables de bloque suelen empezar por 'DB_'
    if nombre_tag.startswith("DB_"):
        return True
    return False

if __name__ == "__main__":
    tag_prueba = "DB_Motor_Speed"
    if validar_tag(tag_prueba):
        print(f"✅ El tag '{tag_prueba}' cumple con el estándar.")
    else:
        print(f"❌ El tag '{tag_prueba}' NO cumple con el estándar.")