import pandas as pd
import folium
from streamlit_folium import folium_static
import plotly.express as px
import streamlit as st
from datetime import datetime
from PIL import Image
import inflection

st.set_page_config(page_title="Countries",layout="wide",initial_sidebar_state="expanded",page_icon="🏙️​")

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

df_aux = df1.drop_duplicates(subset='restaurant_id', keep='first')
mais_rest1 = (df_aux.loc[:, ['city', 'restaurant_id','country_code']]
          .groupby(['country_code','city']).count()
          .sort_values('restaurant_id', ascending = False).reset_index())

fig1 = px.bar(mais_rest1.head(10), x='city', y='restaurant_id', 
       labels = {'city':'Cidades', 'restaurant_id':'Quantidade de Restaurantes', 'country_code': 'País'},
       color='country_code',  
       text='restaurant_id')
fig1.update_traces(textposition='inside', texttemplate = '%{text:.2s}')
fig1.update_yaxes(showticklabels = False)
fig1.update_layout(title={'text':'Top 10 Cidades com mais Restaurantes na Base de Dados', 
                         'y':0.95,
                         'x':0})
st.plotly_chart(fig1,use_container_width=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        df_t7 = (df1.loc[df1['aggregate_rating'] >= 4, ['city','country_code','restaurant_id']]
                  .groupby(['country_code','city']).count()
                  .sort_values('restaurant_id', ascending = False).reset_index())
        fig2 = px.bar(df_t7.head(7), x='city', y='restaurant_id', 
               labels = {'city':'Cidades', 'restaurant_id':'Quantidade de Restaurantes', 'country_code': 'País'},
               color='country_code',  
               text='restaurant_id')
        fig2.update_traces(textposition='inside', texttemplate = '%{text:.2s}')
        fig2.update_yaxes(showticklabels = False)
        fig2.update_layout(title={'text':'Top 7 Cidades com mais Restaurantes com Avaliações >= 4', 
                                 'y':0.95,
                                 'x':0})
        st.plotly_chart(fig2,use_container_width=True)
    with col2:
        df_m4 = (df1.loc[df1['aggregate_rating'] < 4, ['city','country_code','restaurant_id']]
                  .groupby(['country_code','city']).count()
                  .sort_values('restaurant_id', ascending = False).reset_index())
        fig3 = px.bar(df_m4.head(7), x='city', y='restaurant_id', 
               labels = {'city':'Cidades', 'restaurant_id':'Quantidade de Restaurantes', 'country_code': 'País'},
               color='country_code',  
               text='restaurant_id')
        fig3.update_traces(textposition='inside', texttemplate = '%{text:.2s}')
        fig3.update_yaxes(showticklabels = False)
        fig3.update_layout(title={'text':'Top 7 Cidades com mais Restaurantes com Avaliações < 4', 
                                 'y':0.95,
                                 'x':0})
        st.plotly_chart(fig2,use_container_width=True)
df_cuisines = (df1.loc[:, ['city','country_code','cuisines']]
          .groupby(['country_code','city']).nunique()
          .sort_values('cuisines', ascending = False).reset_index())
fig4 = px.bar(df_cuisines.head(7), x='city', y='cuisines', 
       labels = {'city':'Cidades', 'cuisines':'Quantidade de Restaurantes', 'country_code': 'País'},
       color='country_code',  
       text='cuisines')
fig4.update_traces(textposition='inside', texttemplate = '%{text:.2s}')
fig4.update_yaxes(showticklabels = False)
fig4.update_layout(title={'text':'Top 10 Cidades com mais Restaurantes com Tipos Culinários distintos', 
                         'y':0.95,
                         'x':0})
st.plotly_chart(fig4,use_container_width=True)
