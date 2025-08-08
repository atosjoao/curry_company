import streamlit as st
from PIL import Image
import inflection
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Cousines",layout="wide",initial_sidebar_state="expanded",page_icon="🍽️​")

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
    df = pd.read_parquet("datasets\\zomato.parquet")
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
df_cuisines = df1.copy()

image_path = "assets\\logo1.png"
image = Image.open(image_path)
st.sidebar.image(image, width = 120)
st.sidebar.write("## Filtros")
paises = st.sidebar.multiselect("Escolha os Paises que \n Deseja visualizar os Restaurantes", 
                                options=df1['country_code'].unique(), 
                                default=["Brazil", "United States of America", "England", "Australia"])
slider_restaurantes = st.sidebar.slider('Selecione a quantidade de Restaurantes que deseja visualizar',min_value=1, max_value=20, value=10)
cuisines = st.sidebar.multiselect("Escolha os Tipos de Culinária", 
                                options=df1['cuisines'].unique(), 
                                default=["Home-made", "BBQ", "Japanese", "Brazilian", "American", "Italian"])
selected = df1.loc[(df1['country_code'].isin(paises)) & (df1['cuisines'].isin(cuisines)),:]
df1 = selected
df_restaurantes = ((df1.loc[:,['restaurant_name','country_code','city','cuisines','average_cost_for_two','aggregate_rating','votes']]
                            .groupby(['restaurant_name','country_code','city','cuisines'])
                            .mean()
                            .sort_values('aggregate_rating', ascending = False)
                            .reset_index()).head(slider_restaurantes))
df_restaurantes['average_cost_for_two'], df_restaurantes['aggregate_rating'], df_restaurantes['votes'] = round(df_restaurantes['average_cost_for_two'],2), round(df_restaurantes['aggregate_rating'],3), round(df_restaurantes['votes'],2)
df_restaurantes = df_restaurantes.rename(columns={'restaurant_name':'Restaurante',
                        'country_code':'País',
                        'city':'Cidade',
                        'cuisines':'Culinária',
                        'average_cost_for_two':'Preço para Dois',
                        'aggregate_rating':'Avaliação Média',
                        'votes':'Nº Avaliações'})

st.write('# Visão Tipos de Culinárias')
st.write('## Melhores Restaurantes dos Principais tipos Culinários')

with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric(f"North Indian: {df_cuisines.loc[df_cuisines['cuisines']=='North Indian',['restaurant_name','aggregate_rating']].groupby('restaurant_name').mean().sort_values('aggregate_rating', ascending = False).reset_index().iloc[0,0]}", value= f"{df_cuisines.loc[df_cuisines['cuisines']=='North Indian',['restaurant_name','aggregate_rating']].groupby('restaurant_name').mean().sort_values('aggregate_rating', ascending = False).reset_index().iloc[0,1]} / 5.0")
        with col2:
            st.metric(f"Italian: {df_cuisines.loc[df_cuisines['cuisines']=='Italian',['restaurant_name','aggregate_rating']].groupby('restaurant_name').mean().sort_values('aggregate_rating', ascending = False).reset_index().iloc[0,0]}", value= f"{df_cuisines.loc[df_cuisines['cuisines']=='Italian',['restaurant_name','aggregate_rating']].groupby('restaurant_name').mean().sort_values('aggregate_rating', ascending = False).reset_index().iloc[0,1]} / 5.0")
        with col3:
            st.metric(f"American: {df_cuisines.loc[df_cuisines['cuisines']=='American',['restaurant_name','aggregate_rating']].groupby('restaurant_name').mean().sort_values('aggregate_rating', ascending = False).reset_index().iloc[0,0]}", value= f"{df_cuisines.loc[df_cuisines['cuisines']=='American',['restaurant_name','aggregate_rating']].groupby('restaurant_name').mean().sort_values('aggregate_rating', ascending = False).reset_index().iloc[0,1]} / 5.0")
        with col4:
            st.metric(f"Brazilian: {df_cuisines.loc[df_cuisines['cuisines']=='Brazilian',['restaurant_name','aggregate_rating']].groupby('restaurant_name').mean().sort_values('aggregate_rating', ascending = False).reset_index().iloc[0,0]}", value= f"{df_cuisines.loc[df_cuisines['cuisines']=='Mexican',['restaurant_name','aggregate_rating']].groupby('restaurant_name').mean().sort_values('aggregate_rating', ascending = False).reset_index().iloc[0,1]} / 5.0")
        with col5:
            st.metric(f"Cafe: {df_cuisines.loc[df_cuisines['cuisines']=='Cafe',['restaurant_name','aggregate_rating']].groupby('restaurant_name').mean().sort_values('aggregate_rating', ascending = False).reset_index().iloc[0,0]}", value= f"{df_cuisines.loc[df_cuisines['cuisines']=='Cafe',['restaurant_name','aggregate_rating']].groupby('restaurant_name').mean().sort_values('aggregate_rating', ascending = False).reset_index().iloc[0,1]} / 5.0")

st.write(f'## Top {slider_restaurantes} Restaurantes')
st.table(df_restaurantes)

with st.container():
        col1, col2 = st.columns(2)
        with col1:
            df_fig = (df1.loc[:,['cuisines','aggregate_rating']].groupby(['cuisines']).mean().sort_values('aggregate_rating', ascending = False).reset_index()).head(10)
            df_fig['aggregate_rating'] = round(df_fig['aggregate_rating'], 2)
            fig = px.bar(df_fig, x='cuisines', y='aggregate_rating',
                         labels={'cuisines': 'Tipo de Culinária', 'aggregate_rating':'Média de Avaliação'},
                         text='aggregate_rating')
            fig.update_traces(textposition='inside')
            fig.update_yaxes(showticklabels = False)
            fig.update_layout(title={'text':f'Top {10} Melhores Tipos de Culinárias', 
                                     'y':0.95,
                                     'x':0})
            st.plotly_chart(fig,use_container_width=True)
        with col2:
            df_fig2 = (df1.loc[:,['cuisines','aggregate_rating']].groupby(['cuisines']).mean().sort_values('aggregate_rating', ascending = True).reset_index()).head(10)
            df_fig2['aggregate_rating'] = round(df_fig2['aggregate_rating'], 2)
            fig2 = px.bar(df_fig2, x='cuisines', y='aggregate_rating',
                         labels={'cuisines': 'Tipo de Culinária', 'aggregate_rating':'Média de Avaliação'},
                         text='aggregate_rating')
            fig2.update_traces(textposition='inside')
            fig2.update_yaxes(showticklabels = False)
            fig2.update_layout(title={'text':f'Top {10} Piores Tipos de Culinárias', 
                                     'y':0.95,
                                     'x':0})
            st.plotly_chart(fig2,use_container_width=True)