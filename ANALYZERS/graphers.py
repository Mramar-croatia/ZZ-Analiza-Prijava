from matplotlib.ticker import MaxNLocator
from matplotlib import pyplot as plt

import pandas as pd

from . import visualizers as vis

def graph_razred(df: pd.DataFrame, save_directory: str, y_label: str = 'Broj prijava'):
    
    counts = df['RAZRED'].value_counts()
    counts = counts.sort_index()
    
    vis.graph_bar_plot(counts, size = (12,10), save_path = save_directory+ f"{y_label.lower().replace(' ', '_')}_po_razredu_graf.png", x_label = 'Razred', y_label = y_label, title = f'{y_label} po razredu')
    
    counts = counts.reset_index()
    counts.columns = ['RAZRED', y_label.upper()]
    counts.set_index('RAZRED', inplace=True)
    counts = counts.reset_index()
    
    vis.graph_table(counts = counts, save_path = save_directory+f"{y_label.lower().replace(' ', '_')}_po_razredu_tablica.png")
    
def graph_skola(df: pd.DataFrame, save_directory: str, y_label: str = 'Broj prijava'):
    
    counts = df['SKOLA'].value_counts()
    
    vis.graph_bar_plot(counts, size = (12,10), save_path = save_directory + f"{y_label.lower().replace(' ', '_')}_po_skoli_graf.png", x_label = 'Škola', y_label = y_label, title = f'{y_label} po školi')
    
    counts = counts.reset_index()
    counts.columns = ['ŠKOLA', y_label.upper()]
    counts.set_index('ŠKOLA', inplace=True)
    counts = counts.reset_index()
    
    vis.graph_table(counts = counts, save_path = save_directory+f"{y_label.lower().replace(' ', '_')}_po_skoli_tablica.png")
    
def graph_lokacija(df: pd.DataFrame, save_directory: str, y_label: str = 'Broj prijava'):
    
    flattened = df.explode('LOKACIJA')
    
    counts = flattened['LOKACIJA'].value_counts()
    counts = counts.sort_index()
    
    vis.graph_bar_plot(counts, size = (12,10), save_path = save_directory+f"{y_label.lower().replace(' ', '_')}_po_lokaciji_graf.png", x_label = 'Skola', y_label = y_label, title = f'{y_label} po lokaciji')
    
    counts = counts.reset_index()
    counts.columns = ['LOKACIJA', y_label.upper()]
    counts.set_index('LOKACIJA', inplace=True)
    counts = counts.reset_index()
    
    vis.graph_table(counts = counts, save_path = save_directory+f"{y_label.lower().replace(' ', '_')}_po_lokaciji_tablica.png")

def graph_termin(df: pd.DataFrame, save_directory: str, y_label: str = 'Broj prijava'):
    
    flattened = df.explode('TERMIN')
    
    counts = flattened['TERMIN'].value_counts()
    counts = counts.sort_index(ascending=False)
    
    vis.graph_bar_plot(counts, size = (12,10), save_path = save_directory+f"{y_label.lower().replace(' ', '_')}_po_terminu_graf.png", x_label = 'Termin', y_label = y_label, title = f'{y_label} po terminu')
    
    counts = counts.reset_index()
    counts.columns = ['TERMIN', y_label.upper()]
    counts.set_index('TERMIN', inplace=True)
    counts = counts.reset_index()
    
    vis.graph_table(counts = counts, save_path = save_directory+f"{y_label.lower().replace(' ', '_')}_po_terminu_tablica.png")
       
def graph_predmet(df: pd.DataFrame, save_directory: str, y_label: str = 'Broj prijava'):
    
    flattened = df.explode('PREDMET')
    
    counts = flattened['PREDMET'].value_counts()
    counts = counts.sort_index(ascending=False)
    
    vis.graph_bar_plot(counts, size = (12,10), save_path = save_directory+f"{y_label.lower().replace(' ', '_')}_po_predmetu_graf.png", x_label = 'Predmet', y_label = y_label, title = f'{y_label} po predmetu')
    
    counts = counts.reset_index()
    counts.columns = ['PREDMET', y_label.upper()]
    counts.set_index('PREDMET', inplace=True)
    counts = counts.reset_index()
    
    vis.graph_table(counts = counts, save_path = save_directory+f"{y_label.lower().replace(' ', '_')}_po_predmetu_tablica.png")
    
def graph_gender(df: pd.DataFrame, save_directory: str, y_label: str = 'Broj prijava'):
    
    counts = df['SPOL'].value_counts()
    counts = counts.sort_index(ascending=False)
    
    vis.graph_bar_plot(counts, size = (12,10), save_path = save_directory+f"{y_label.lower().replace(' ', '_')}_po_spolu_graf.png", x_label = 'Spol', y_label = y_label, title = f'{y_label} po predmetu')
    
    counts = counts.reset_index()
    counts.columns = ['SPOL', y_label.upper()]
    counts.set_index('SPOL', inplace=True)
    counts = counts.reset_index()
    
    vis.graph_table(counts = counts, save_path = save_directory+f"{y_label.lower().replace(' ', '_')}_po_spolu_tablica.png")