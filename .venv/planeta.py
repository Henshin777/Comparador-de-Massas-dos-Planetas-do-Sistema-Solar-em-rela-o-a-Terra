import streamlit as st
import pandas as pd
import plotly.express as px
# base de dados

planetas = {
    "Mercúrio": 3.285e23,
    "Vênus": 4.867e24,
    "Terra": 5.972e24,
    "Marte": 6.39e23,
    "Júpiter": 1.898e27,
    "Saturno": 5.683e26,
    "Urano": 8.681e25,
    "Netuno": 1.024e26,
}

df = pd.DataFrame(list(planetas.items()), columns=["Planetas", "Massas (Kg)"])
print(df)
massa_terra = planetas["Terra"]

st.title("🌌Comparador de Massas (kg)")
st.subheader("Compara a massa da Terra com a dos plantetas do nosso sistema solar de forma intuitiva")
planeta = st.selectbox("Escolha um planeta", df["Planetas"])
massa_planeta = planetas[planeta]
relacao = massa_planeta / massa_terra

fig = px.pie(
    df,
    names="Planetas",
    values="Massas (Kg)",
    title="Proporção de Massas dos Planetas",
    hover_data=["Massas (Kg)"],
)
st.plotly_chart(fig)
st.write(f"Em relação á Terra: {relacao:.3f}x")
fig.update_traces(textinfo="label+percent")

escolha_planeta = input("Escolha um planeta:").title()

if escolha_planeta in planetas:
    massa_planeta = planetas[escolha_planeta]
    print(f"Massa do {escolha_planeta}: {massa_planeta:.2e} kg")
    print(
        f"Massa do {escolha_planeta} em relação à Terra: {massa_planeta / massa_terra:.3f}"
    )
else:
    print(f"Planeta {escolha_planeta} não encontrado na base de dados.")
