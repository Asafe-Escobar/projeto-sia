"""Funções de visualização reutilizáveis (Streamlit)."""

import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def show_dashboard(df):
    """Exibe componentes básicos do dashboard dado um DataFrame processado.

    Não altera dados, apenas renderiza gráficos e tabelas no Streamlit.
    """
    st.set_page_config(page_title="Monitor IA Piauí", layout="wide")
    st.title("Monitor de Inteligência Artificial no Piauí")

    if not df.empty:
        st.subheader("Distribuição de Sentimentos")
        sent_counts = df["sentiment"].value_counts()
        fig1 = sent_counts.plot.pie(autopct="%1.1f%%", figsize=(5, 5)).get_figure()
        st.pyplot(fig1)

        st.subheader("Nuvem de Palavras")
        text = " ".join(df["description"])
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
        fig2, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig2)

        st.subheader("Tabela de Notícias")
        st.dataframe(df)
    else:
        st.warning("Nenhum dado disponível para exibir.")

    st.markdown(
        """
        ---
        **Aviso:** Esta análise de sentimento é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos.
        """
    )
