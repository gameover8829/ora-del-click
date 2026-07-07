import streamlit as st
import urllib.parse

st.set_page_config(page_title="Generador de Ofertas", page_icon="🛒")

st.title("Generador de texto para WhatsApp")
st.write("Sube tus links de MercadoLibre y compártelos rápidamente.")

# --- SECCIÓN 1: DATOS DEL PRODUCTO ---
st.header("1. Ingresa los datos del producto")

col1, col2 = st.columns(2)
with col1:
    producto = st.text_input("Nombre del Producto", placeholder="Ej. Tenis Deportivos o iPhone 13")
    precio = st.text_input("Precio de Oferta", placeholder="Ej. 499")
with col2:
    link_ml = st.text_input("Link de MercadoLibre", placeholder="https://articulo.mercadolibre.com.mx/...")
    # Nueva opción para adaptar el texto al tipo de producto
    categoria = st.selectbox("Categoría del producto:", ["General/Cualquiera", "Moda y Ropa", "Tecnología y Gadgets", "Hogar y Cocina", "Belleza y Cuidado"])

# --- SECCIÓN 2: PLANTILLA Y EDICIÓN ---
st.header("2. Personaliza tu mensaje")

# Selector para cambiar el estilo del mensaje
estilo = st.selectbox("Elige el estilo del mensaje:", ["Llamativo", "Corto y directo", "Urgencia"])

# El sistema se activa cuando los campos esenciales están llenos
if producto and precio and link_ml:
    
    # --- LÓGICA DE TEXTOS ADAPTADOS AL PRODUCTO Y ESTILO ---
    # 1. Definimos variables adaptadas según la categoría elegida
    if categoria == "Moda y Ropa":
        emoji_cat = "👟👗"
        frase_cat = f"¡Renueva tu outfit con este increíble {producto}! Luce espectacular."
        frase_urgencia = "¡Últimas tallas y modelos en inventario!"
    elif categoria == "Tecnología y Gadgets":
        emoji_cat = "⚡📱"
        frase_cat = f"¡Llegó la hora de actualizarte! Llévate este {producto} al mejor precio."
        frase_urgencia = "¡Pocas unidades disponibles de esta joya tecnológica!"
    elif categoria == "Hogar y Cocina":
        emoji_cat = "🏡🍳"
        frase_cat = f"Dale un toque especial a tu casa con este {producto}. ¡Te va a encantar!"
        frase_urgencia = "¡Mejora tu hogar antes de que se agote!"
    elif categoria == "Belleza y Cuidado":
        emoji_cat = "✨💄"
        frase_cat = f"Consiéntete como te mereces. Este {producto} es justo lo que necesitas."
        frase_urgencia = "¡Consigue el tuyo antes de que suba de precio!"
    else:  # General / Cualquiera
        emoji_cat = "🎁🛍️"
        frase_cat = f"¡Checa este productazo! El {producto} que estabas buscando ya está aquí."
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
