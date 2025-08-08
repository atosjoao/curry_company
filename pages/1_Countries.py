import pandas as pd
import folium
from streamlit_folium import folium_static
import plotly.express as px
import streamlit as st
from datetime import datetime
from PIL import Image
import inflection

st.set_page_config(page_title="Countries",layout="wide",initial_sidebar_state="expanded",page_icon="🌍​")

COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}
@st.cache_data
def country_name(country_id):
    return COUNTRIES[country_id]

@st.cache_data
def create_price_type(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}
@st.cache_data
def color_name(color_code):
    return COLORS[color_code]

@st.cache_data
def rename_columns():
    df = pd.read_parquet("datasets/zomato.parquet")
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

df1 = rename_columns()
df1['rating_color'] = df1['rating_color'].map(color_name)
df1['country_code'] = df1['country_code'].map(country_name)
df1['price_range'] = df1['price_range'].map(create_price_type)
df1 = df1.dropna(subset=['cuisines'])
df1["cuisines"] = df1.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

image_path = "assets\\logo1.png"
image = Image.open(image_path)
st.sidebar.image(image, width = 120)
st.sidebar.write("## Filtros")
paises = st.sidebar.multiselect("Escolha os Paises que \n Deseja visualizar os Restaurantes", 
                                options=df1['country_code'].unique(), 
                                default=["Brazil", "United States of America", "England", "Qatar"])
paises_selecionados = df1['country_code'].isin(paises)
df1 = df1.loc[paises_selecionados, :].copy()

st.title("🌍​ Visão Países")

mais_rest1 = (df1.loc[:, ['restaurant_id', 'country_code']]
             .groupby('country_code').nunique()
             .sort_values('restaurant_id', ascending = False).reset_index())

fig1 = px.bar(mais_rest1, x='country_code', y='restaurant_id', 
       labels = {'country_code':'Paises', 'restaurant_id':'Quantidade de Restaurantes'}, 
       color_discrete_sequence=px.colors.qualitative.Dark2, 
       template='plotly_white', 
       text='restaurant_id')
fig1.update_traces(textposition='inside', texttemplate = '%{text:.2s}')
fig1.update_yaxes(showticklabels = False)
fig1.update_layout(title={'text':'Restaurantes cadastrados por país', 
                         'y':0.95,
                         'x':0})
st.plotly_chart(fig1,use_container_width=True)

mais_cidades = (df1.loc[:, ['country_code', 'city']]
                .groupby('country_code')
                .count().sort_values('city', ascending=False).reset_index())
fig = px.bar(mais_cidades, x='country_code', y='city', 
       labels = {'country_code':'Paises', 'city':'Quantidade de Cidades'}, 
       color_discrete_sequence=px.colors.qualitative.Dark2, 
       template='plotly_white', 
       text='city')
fig.update_traces(textposition='inside', texttemplate = '%{text:.2s}')
fig.update_yaxes(showticklabels = False)
fig.update_layout(title={'text':'Cidades cadastradas por país', 
                         'y':0.95,
                         'x':0})
st.plotly_chart(fig,use_container_width=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        df_aux1 = (df1.loc[:, ['country_code', 'votes']]
          .groupby('country_code').mean()
          .sort_values('votes', ascending = False).reset_index())
        fig_3 = px.bar(df_aux1, x='country_code', y='votes', 
            labels = {'country_code':'Paises', 'votes':'Quantidade de Avaliações'}, 
            color_discrete_sequence=px.colors.qualitative.Dark2, 
            template='plotly_white', 
            text='votes')
        fig_3.update_traces(textposition='inside', texttemplate = '%{text:.2s}')
        fig_3.update_yaxes(showticklabels = False)
        fig_3.update_layout(title={'text':'Restaurantes com mais Avaliações', 
                         'y':0.95,
                         'x':0})
        st.plotly_chart(fig_3,use_container_width=True)
    with col2:
        for_two = (df1.loc[:, ['country_code', 'average_cost_for_two']]
          .groupby('country_code').mean()
          .sort_values('average_cost_for_two', ascending = False).reset_index())
        for_two['average_cost_for_two'] = round(for_two['average_cost_for_two'], 2)
        fig_4 = px.bar(for_two, x='country_code', y='average_cost_for_two', 
        labels = {'country_code':'Paises', 'average_cost_for_two':'Valor Médio (U$)'}, 
        color_discrete_sequence=px.colors.qualitative.Dark2, 
        template='plotly_white', 
        text='average_cost_for_two')
        fig_4.update_traces(textposition='inside', texttemplate = '%{text:.2s}')
        fig_4.update_yaxes(showticklabels = False)
        fig_4.update_layout(title={'text':'Media de preco em um prato para dois', 
                                'y':0.95,
                                'x':0})
        st.plotly_chart(fig_4,use_container_width=True)

