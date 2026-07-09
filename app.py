import streamlit as st
import urllib.parse

st.set_page_config(page_title="Generador de Ofertas", page_icon="🛒")

st.title("Generador de texto para WhatsApp")
st.write("Sube tus links de MercadoLibre y compártelos rápidamente.")

# --- SECCIÓN 1: DATOS DEL PRODUCTO ---
st.header("1. Ingresa los datos del producto")

col1, col2 = st.columns(2)
with col1:
    producto = st.text_input("Nombre del Producto", placeholder="Ej. Taladro Inalámbrico")
    precio = st.text_input("Precio de Oferta", placeholder="Ej. 1299")
with col2:
    link_ml = st.text_input("Link de MercadoLibre", placeholder="https://articulo.mercadolibre.com.mx/...")
    
    # Lista actualizada con nuevas categorías
    lista_categorias = [
        "General / Cualquiera", 
        "Vehículos y Accesorios", 
        "Supermercado y Alimentos", 
        "Tecnología y Electrónica", 
        "Videojuegos y Consolas",       # NUEVA
        "Electrodomésticos",            # NUEVA
        "Hogar y Muebles", 
        "Moda", 
        "Joyería y Relojes",            # NUEVA
        "Deportes y Fitness", 
        "Herramientas y Construcción", 
        "Mascotas", 
        "Bebés y Juguetes", 
        "Salud y Belleza",
        "Libros y Música",              # NUEVA
        "Instrumentos Musicales",       # NUEVA
        "Papelería y Arte"              # NUEVA
    ]
    categoria = st.selectbox("Categoría del producto:", lista_categorias)

# --- SECCIÓN 2: PLANTILLA Y EDICIÓN ---
st.header("2. Personaliza tu mensaje")

# Selector para cambiar el estilo del mensaje
estilo = st.selectbox("Elige el estilo del mensaje:", ["Llamativo", "Corto y directo", "Urgencia"])

# El sistema se activa cuando los campos esenciales están llenos
if producto and precio and link_ml:
    
    # --- LÓGICA DE TEXTOS ADAPTADOS AL PRODUCTO Y ESTILO ---
    if categoria == "Vehículos y Accesorios":
        emoji_cat = "🚗🔧"
        frase_cat = f"¡Equipa tu vehículo con este excelente {producto}!"
        frase_urgencia = "¡No dejes pasar esta oportunidad para tu auto o moto!"
    elif categoria == "Supermercado y Alimentos":
        emoji_cat = "🛒🍎"
        frase_cat = f"¡Aprovecha y llévate {producto} al mejor precio!"
        frase_urgencia = "¡Llena tu despensa antes de que se agote!"
    elif categoria == "Tecnología y Electrónica":
        emoji_cat = "⚡📱"
        frase_cat = f"¡Llegó la hora de actualizarte! Llévate este {producto}."
        frase_urgencia = "¡Pocas unidades disponibles de esta joya tecnológica!"
    elif categoria == "Videojuegos y Consolas":
        emoji_cat = "🎮🕹️"
        frase_cat = f"¡Lleva tu entretenimiento al siguiente nivel con este {producto}!"
        frase_urgencia = "¡Sube de nivel antes de que se agoten las unidades!"
    elif categoria == "Electrodomésticos":
        emoji_cat = "🧊🍳"
        frase_cat = f"¡Facilita tu día a día con este increíble {producto}!"
        frase_urgencia = "¡Equipa tu casa al mejor precio ahora mismo!"
    elif categoria == "Hogar y Muebles":
        emoji_cat = "🏡🛋️"
        frase_cat = f"Dale un toque especial a tu casa con este {producto}."
        frase_urgencia = "¡Mejora tu hogar hoy mismo antes de que se acaben!"
    elif categoria == "Moda":
        emoji_cat = "👟👗"
        frase_cat = f"¡Renueva tu outfit con este increíble {producto}! Luce espectacular."
        frase_urgencia = "¡Últimas tallas y modelos en inventario!"
    elif categoria == "Joyería y Relojes":
        emoji_cat = "💍⌚"
        frase_cat = f"¡Luce increíble y a la moda con este hermoso {producto}!"
        fr
