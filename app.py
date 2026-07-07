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
    
    # Lista actualizada con las categorías reales de las imágenes
    lista_categorias = [
        "General / Cualquiera", 
        "Vehículos y Accesorios", 
        "Supermercado y Alimentos", 
        "Tecnología y Electrónica", 
        "Hogar y Muebles", 
        "Moda", 
        "Deportes y Fitness", 
        "Herramientas y Construcción", 
        "Mascotas", 
        "Bebés y Juguetes", 
        "Salud y Belleza"
    ]
    categoria = st.selectbox("Categoría del producto:", lista_categorias)

# --- SECCIÓN 2: PLANTILLA Y EDICIÓN ---
st.header("2. Personaliza tu mensaje")

# Selector para cambiar el estilo del mensaje
estilo = st.selectbox("Elige el estilo del mensaje:", ["Llamativo", "Corto y directo", "Urgencia"])

# El sistema se activa cuando los campos esenciales están llenos
if producto and precio and link_ml:
    
    # --- LÓGICA DE TEXTOS ADAPTADOS AL PRODUCTO Y ESTILO ---
    # 1. Definimos variables adaptadas según la amplia lista de categorías
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
    elif categoria == "Hogar y Muebles":
        emoji_cat = "🏡🛋️"
        frase_cat = f"Dale un toque especial a tu casa con este {producto}."
        frase_urgencia = "¡Mejora tu hogar hoy mismo antes de que se acaben!"
    elif categoria == "Moda":
        emoji_cat = "👟👗"
        frase_cat = f"¡Renueva tu outfit con este increíble {producto}! Luce espectacular."
        frase_urgencia = "¡Últimas tallas y modelos en inventario!"
    elif categoria == "Deportes y Fitness":
        emoji_cat = "🏋️‍♂️⚽"
        frase_cat = f"¡Ponte en forma y da tu máximo con este {producto}!"
        frase_urgencia = "¡Equípate antes de que suba de precio!"
    elif categoria == "Herramientas y Construcción":
        emoji_cat = "🛠️🏗️"
        frase_cat = f"¡Haz tus proyectos realidad con la mejor calidad! Increíble {producto}."
        frase_urgencia = "¡Herramientas indispensables a un precio irrepetible!"
    elif categoria == "Mascotas":
        emoji_cat = "🐶🐱"
        frase_cat = f"¡Consiente a tu mejor amigo peludo con este {producto}!"
        frase_urgencia = "¡Lo mejor para tu mascota a un clic, últimas piezas!"
    elif categoria == "Bebés y Juguetes":
        emoji_cat = "👶🧸"
        frase_cat = f"¡Diversión y cuidado garantizado con este {producto}!"
        frase_urgencia = "¡Consíguelo antes de que vuele!"
    elif categoria == "Salud y Belleza":
        emoji_cat = "✨💄"
        frase_cat = f"Consiéntete como te mereces. Este {producto} es justo lo que necesitas."
        frase_urgencia = "¡Cuida de ti al mejor precio antes de que se agote!"
    else:  # General / Cualquiera
        emoji_cat = "🎁🛍️"
        frase_cat = f"¡Checa este productazo! El {producto} que estabas buscando."
        frase_urgencia = "¡Corre porque vuelan las piezas!"

    # 2. Construimos la plantilla final uniendo el Estilo + los datos de la Categoría
    if estilo == "Llamativo":
        mensaje_default = f"🔥 ¡GRAN OFERTA DE NO CREER! 🔥\n\n{emoji_cat} {frase_cat}\n\n💰 Precio especial: solo $ {precio}. 😱\n\n👉 Cómpralo de forma segura en MercadoLibre aquí: \n{link_ml} \n\n#Ofertas #MercadoLibre #Imperdible"
    
    elif estilo == "Corto y directo":
        mensaje_default = f"✅ {emoji_cat} {producto} disponible por solo ${precio}.\n\n🛒 Cómpralo aquí directo en MercadoLibre: {link_ml}"
    
    else:  # Urgencia
        mensaje_default = f"🚨 ¡ÚLTIMAS PIEZAS DISPONIBLES! 🚨\n\n{producto} súper rebajado a solo ${precio}. 😱\n\n⚠️ {frase_urgencia}\n\n🛒 Haz tu pedido AQUÍ antes de que se acabe: {link_ml}"
    
    # 3. Mostramos la caja de texto editable para el usuario
    mensaje_final = st.text_area("Edita el texto final si deseas agregar o quitar algo:", value=mensaje_default, height=200)
    
    # 4. Codificación y botón de WhatsApp
    mensaje_codificado = urllib.parse.quote(mensaje_final)
    url_whatsapp = f"https://wa.me/?text={mensaje_codificado}"
    
    st.link_button("📲 Haz clic aquí para enviarlo directo por WhatsApp", url_whatsapp, type="primary")

else:
    st.info("Por favor, introduce el nombre del producto, precio y link arriba para generar los textos personalizados.")

st.divider()
