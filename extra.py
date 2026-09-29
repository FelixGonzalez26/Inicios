def limpiar_texto(texto):
    """Limpia el texto convirtiéndolo a minúsculas y removiendo espacios."""
    return texto.lower().replace(" ", "")

def es_palindromo(palabra):
    """Verifica si una palabra se lee igual al revés."""
    p_limpia = limpiar_texto(palabra)
    return p_limpia == p_limpia[::-1]

def son_anagramas(p1, p2):
    """Verifica si dos palabras tienen exactamente las mismas letras."""
    l1, l2 = limpiar_texto(p1), limpiar_texto(p2)
    return sorted(l1) == sorted(l2)

def es_isograma(palabra):
    """Verifica si una palabra no tiene letras repetidas."""
    p_limpia = limpiar_texto(palabra)
    return len(set(p_limpia)) == len(p_limpia)

def analizar_palabras(palabra1, palabra2):
    """Función principal que agrupa todas las comprobaciones."""
    print(f"\n--- Análisis para: '{palabra1}' y '{palabra2}' ---")
    
    # Comprobación de palíndromos (individual)
    print(f"* ¿'{palabra1}' es palíndromo?: {'Sí' if es_palindromo(palabra1) else 'No'}")
    print(f"* ¿'{palabra2}' es palíndromo?: {'Sí' if es_palindromo(palabra2) else 'No'}")
    
    # Comprobación de anagramas (comparación mutua)
    print(f"* ¿Son anagramas entre sí?: {'Sí' if son_anagramas(palabra1, palabra2) else 'No'}")
    
    # Comprobación de isogramas (individual)
    print(f"* ¿'{palabra1}' es isograma?: {'Sí' if es_isograma(palabra1) else 'No'}")
    print(f"* ¿'{palabra2}' es isograma?: {'Sí' if es_isograma(palabra2) else 'No'}")

# Ejemplo de uso:
analizar_palabras("reconocer", "correo")