import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import generuj_grupy as grupa

"""
# Witaj Sprzedawco Allegro!

Wrzucaj tu swoje statystyki aby dowiedzieć się więcej o ofertach

"""

file = st.file_uploader("ZAŁADUJ Statystyki oferty z panelu ads np. statystyki_oferty_01-03-2024_31-03-2024.xlsx")

######kod generujący statsy#####
if file:
    g1, g2 = grupa.generuj(file)
    """Grupa 1 promocji"""
    st.write(g1)
    """Grupa 2 Oferty do poprawy"""
    st.write(g2)
    
