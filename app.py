import streamlit as st
import urllib.parse

st.set_page_config(page_title="Generador de Ofertas", page_icon="🛒")

st.title("Generador de texto para WhatsApp")
st.write("Sube tus links de MercadoLibre y compártelos rápidamente.")

# --- SECCIÓN 1: DATOS DEL PRODUCTO ---
st.header("1. Ingresa los datos")

# Campos para ingresar los datos
col1, col2 = st.columns(2)
with col1:
    producto = st.text_input("Nombre del Producto", placeholder="Ej. Tenis Deportivos")
    precio = st.text_input("Precio de Oferta", placeholder="Ej. $499")
with col2:
    link_ml = st.text_input("Link de MercadoLibre", placeholder="https://articulo.mercadolibre.com.mx/...")

# --- SECCIÓN 2: PLANTILLA Y EDICIÓN ---
st.header("2. Personaliza tu mensaje")

# Selector para cambiar el texto base promocional
estilo = st.selectbox("Elige el estilo del mensaje:", ["Llamativo", "Corto y directo", "Urgencia"])

# Todo esto se muestra y actualiza automáticamente cuando se llenan los campos
if producto and precio and link_ml:
    
    # 1. Definir el texto base según la opción seleccionada
    if estilo == "Llamativo":
        mensaje_default = f"🔥 ¡Gran oferta, no te la pierdas! 🔥\n\nLlévate {producto} a solo $ {precio}. 😱\n\n👉 Cómpralo aquí antes de que se acabe: \n\n {link_ml} \n\n#Ofertas #MercadoLibre"
    elif estilo == "Corto y directo":
        mensaje_default = f"✅ {producto} disponible por ${precio}.\n\nCómpralo aquí directo: {link_ml}"
    else:
        mensaje_default = f"🚨 ¡ÚLTIMAS PIEZAS! 🚨\n\n{producto} súper rebajado a ${precio}. ¡Corre que vuelan!\n\n🛒 Link aquí: {link_ml}"
    
    # 2. Mostramos el área de texto con la plantilla. 
    # El usuario puede borrar o agregar palabras manualmente aquí antes de enviarlo.
    mensaje_final = st.text_area("Edita el texto si lo necesitas (tus cambios se guardarán en el enlace):", value=mensaje_default, height=180)
    
    # 3. Codifica el texto FINAL (incluyendo lo que el usuario haya editado a mano)
    mensaje_codificado = urllib.parse.quote(mensaje_final)
    url_whatsapp = f"https://wa.me/?text={mensaje_codificado}"
    
    # 4. Muestra un botón clicable que abre WhatsApp
    st.link_button("📲 Haz clic aquí para enviarlo directo por WhatsApp", url_whatsapp, type="primary")

else:
    # Mensaje de ayuda si faltan campos
    st.info("Llena los 3 campos de arriba para generar tu mensaje.")

st.divider()
