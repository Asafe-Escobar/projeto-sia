import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import unicodedata
from src.coleta import fetch_news
from src.processamento import clean_text, classify_sentiment

def normalize_text(text):
    text = str(text).lower()
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    return text

st.set_page_config(page_title="🤖 Monitor IA Piauí", layout="wide")


st.markdown("""
<h1 style='text-align: center; color: #00BFFF; margin-bottom: 0.5em;'>🤖 Monitor de PESQUISA</h1>
<hr style='border: none; border-top: 2px solid #00BFFF; margin-bottom: 1em;'>
""", unsafe_allow_html=True)

try:
    df = pd.read_csv("data/latest.csv")
    dados_ok = True
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    dados_ok = False


if dados_ok and not df.empty:

    
    busca = st.text_input("� Buscar notícias por palavra-chave (ex: Inteligência Artificial Piauí, SIA Piauí)", value="Inteligência Artificial Piauí")
    sentimento = st.selectbox("🎭 Filtrar por sentimento", ["Todos", "positivo", "negativo", "neutro"])

    if busca:
        with st.spinner("Buscando notícias..."):
            noticias = fetch_news(busca)
            processed = []
            for item in noticias:
                cleaned = clean_text(item["description"])
                sent = classify_sentiment(cleaned)
                processed.append({
                    "title": item["title"],
                    "link": item["link"],
                    "description": cleaned,
                    "sentiment": sent
                })
            df = pd.DataFrame(processed)
        if not df.empty:
            df_filtrado = df.copy()
            if sentimento != "Todos":
                df_filtrado = df_filtrado[df_filtrado['sentiment'] == sentimento]

            n = max(4, min(8, len(df_filtrado)//2 + 4))

            col1, col2 = st.columns([1, 2], gap="large")
            with col1:
                st.markdown("<h3 style='color: #00BFFF;'>📊 Distribuição de Sentimentos</h3>", unsafe_allow_html=True)
                sent_counts = df_filtrado['sentiment'].value_counts()
                
                cores_dict = {"positivo": "#2ecc40", "negativo": "#FF6347", "neutro": "#00BFFF"}
                if len(sent_counts) == 0:
                    
                    st.warning("Nenhum dado para exibir o gráfico de sentimentos.")
                else:
                    cores = [cores_dict.get(label, "#2ecc40" if label=="positivo" else ("#FF6347" if label=="negativo" else "#00BFFF")) for label in sent_counts.index]
                    fig1 = sent_counts.plot.pie(autopct='%1.1f%%', figsize=(n, n), colors=cores).get_figure()
                    st.pyplot(fig1)
               
            with col2:
                st.markdown("<h3 style='color: #00BFFF;'>☁️ Nuvem de Palavras</h3>", unsafe_allow_html=True)
                text = " ".join(df_filtrado['description'])
                if text.strip():
                    wordcloud = WordCloud(width=600, height=300, background_color='#222').generate(text)
                    fig2, ax = plt.subplots(figsize=(n*2, n))
                    ax.imshow(wordcloud, interpolation='bilinear')
                    ax.axis('off')
                    st.pyplot(fig2)
                else:
                    st.info("Nenhuma palavra disponível para gerar a nuvem.")

            st.markdown("<hr style='border: none; border-top: 2px solid #00BFFF; margin: 2em 0 1em 0;'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #00BFFF;'>📰 Tabela de Notícias</h3>", unsafe_allow_html=True)

            
            def make_clickable(val):
                return f'<a href="{val}" target="_blank">Abrir notícia</a>'

            def color_sentiment(val):
                if val == "positivo":
                    return '<span style="color:green;font-weight:bold;">positivo</span>'
                elif val == "negativo":
                    return '<span style="color:red;font-weight:bold;">negativo</span>'
                else:
                    return val

            styled_df = df_filtrado.copy()
            if not styled_df.empty:
                styled_df['link'] = styled_df['link'].apply(make_clickable)
                styled_df['sentiment'] = styled_df['sentiment'].apply(color_sentiment)

            st.write(styled_df.to_html(escape=False, index=False), unsafe_allow_html=True)

            
            csv = df_filtrado.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Exportar tabela filtrada para CSV",
                data=csv,
                file_name="noticias_filtradas.csv",
                mime="text/csv"
            )
        else:
            st.warning("Nenhum dado disponível para exibir com esse filtro.")
    else:
        st.info("Digite uma palavra-chave para buscar notícias.")
st.markdown(
    """
---
<div style='font-size: 14px; color: #888;'>
<b>Aviso:</b> Esta análise de sentimento é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos.
</div>
""",
    unsafe_allow_html=True
)