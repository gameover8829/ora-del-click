import streamlit as st
import urllib.parse

st.set_page_config(page_title="Generador de Ofertas", page_icon="🛒")

st.title("Generador de texto para WhatsApp")
st.write("Sube tus links de MercadoLibre y compártelos rápidamente.")

# --- SECCIÓN 1: GENERADOR DE MENSAJES PARA WHATSAPP ---
st.header("1. Crea tu mensaje de oferta")

# Campos para ingresar los datos
col1, col2 = st.columns(2)
with col1:
    producto = st.text_input("Nombre del Producto", placeholder="Ej. Tenis Deportivos")
    precio = st.text_input("Precio de Oferta", placeholder="Ej. $499")
with col2:
    link_ml = st.text_input("Link de MercadoLibre", placeholder="https://articulo.mercadolibre.com.mx/...")

# Botón mágico
if st.button("Generar Texto y Link de WhatsApp", type="primary"):
    if producto and precio and link_ml:
        # 1. Crea el texto promocional que pediste
        mensaje_venta = f"🔥 ¡Gran oferta, no te la pierdas! 🔥\n\nLlévate {producto} a solo $ {precio}. 😱\n\n👉 Cómpralo aquí antes de que se acabe: \n\n {link_ml} \n\n#Ofertas #MercadoLibre"
        
        st.success("¡Texto generado con éxito!")
        st.text_area("Vista previa del mensaje:", value=mensaje_venta, height=150)
        
        # 2. Codifica el texto para crear un link directo a WhatsApp
        mensaje_codificado = urllib.parse.quote(mensaje_venta)
        url_whatsapp = f"https://wa.me/?text={mensaje_codificado}"
        
        # 3. Muestra un botón clicable que abre WhatsApp
        st.link_button("📲 Haz clic aquí para enviarlo directo por WhatsApp", url_whatsapp, type="primary")
    else:
        st.warning("Por favor, llena los 3 campos (Producto, Precio y Link) primero.")

st.divider()
