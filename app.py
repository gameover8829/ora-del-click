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
if st.button("🚀 Generar Texto y Link de WhatsApp", type="primary"):
    if producto and precio and link_ml:
        # 1. Crea el texto promocional que pediste
        mensaje_venta = f"🔥 ¡Gran oferta, no te la pierdas! 🔥\n\nLlévate {producto} a solo {precio}. 😱\n\n👉 Cómpralo aquí antes de que se acabe: \n\n {link_ml} \n\n#Ofertas #MercadoLibre"
        
        st.success("¡Texto generado con éxito!")
        st.text_area("Vista previa del mensaje:", value=mensaje_venta, height=150)
        
        # 2. Codifica el texto para crear un link directo a WhatsApp
        mensaje_codificado = urllib.parse.quote(mensaje_venta)
        url_whatsapp = f"https://wa.me/?text={mensaje_codificado}"
        
        # 3. Muestra un enlace clicable que abre WhatsApp
        st.markdown(f"### [Haz clic aquí para enviarlo directo por WhatsApp]({url_whatsapp})", unsafe_allow_html=True)
    else:
        st.warning("Por favor, llena los 3 campos (Producto, Precio y Link) primero.")

st.divider()

# --- SECCIÓN 2: CHATBOT GRATUITO (Basado en Reglas) ---
st.header("Chatbot de Asistencia (100% Gratis)")
st.caption("Este chat no usa servicios de paga. Funciona con las reglas que tú le programes.")

# Inicializar la memoria del chat
if "mensajes" not in st.session_state:
    st.session_state.mensajes = [{"rol": "assistant", "contenido": "¡Hola! Soy tu asistente de ventas. Pregúntame cómo usar la plataforma o dudas sobre los links."}]

# Mostrar el historial de conversación en pantalla
for msg in st.session_state.mensajes:
    with st.chat_message(msg["rol"]):
        st.write(msg["contenido"])

# Caja de texto para que el usuario escriba
if prompt := st.chat_input("Escribe tu pregunta aquí..."):
    
    # 1. Mostrar lo que el usuario escribió
    st.session_state.mensajes.append({"rol": "user", "contenido": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # 2. Lógica del Bot Gratuito (Detecta palabras clave)
    prompt_minusculas = prompt.lower()
    
    if "whatsapp" in prompt_minusculas or "compartir" in prompt_minusculas:
        respuesta = "Para compartir, solo llena el nombre, precio y enlace arriba. ¡Al hacer clic en 'Generar', te daré un botón directo a tu WhatsApp!"
    elif "dinero" in prompt_minusculas or "gratis" in prompt_minusculas:
        respuesta = "Este bot está programado en Python puro. ¡No requiere de ninguna API de paga, por lo que es totalmente gratis de mantener!"
    elif "mercado libre" in prompt_minusculas or "link" in prompt_minusculas:
        respuesta = "Recuerda siempre copiar el enlace completo desde la app o web de MercadoLibre para que tus compradores lleguen directo al producto."
    else:
        respuesta = "No estoy seguro de entender. Intenta preguntarme sobre 'whatsapp', 'compartir links' o 'mercado libre'."
        
    # 3. Mostrar la respuesta del bot
    st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta})
    with st.chat_message("assistant"):
        st.write(respuesta)
