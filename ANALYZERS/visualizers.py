from matplotlib.ticker import MaxNLocator
from matplotlib import pyplot as plt

import pandas as pd
import constants as const

def graph_bar_plot(counts: pd.DataFrame, save_path: str, size: tuple[int,int], x_label: str, y_label:str, title: str) -> None:
    
    font_dicts = const.font_dict

    # Create the figure and the axes, draw the plot
    fig, ax = plt.subplots(figsize=size)
    counts.plot(kind='bar', color=const.colors, ax=ax)

    # Set the title and the labels
    ax.set_title(title, fontdict=font_dicts['title'], pad=30)
    ax.set_xlabel(x_label, fontdict=font_dicts['label'], labelpad=20)
    ax.set_ylabel(y_label, fontdict=font_dicts['label'], labelpad=20)

    # Set the tick frequency
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=12))

    # Set the font for the ticks
    plt.xticks(fontname=font_dicts['tick']['family'], fontsize=font_dicts['tick']['size'], rotation=0)
    plt.yticks(fontname=font_dicts['tick']['family'], fontsize=font_dicts['tick']['size'])

    # Show the plot
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
def graph_table(counts: pd.DataFrame, save_path: str) -> None:
    
    font_dicts = const.font_dict
    
    row_height = 0.7
    first_row_height = 1
    size = (10, len(counts) * 0.15 + 0.4)
    
    # Create the figure and the axes
    fig, ax = plt.subplots(figsize=size)
    
    # Hide the axes
    ax.axis('tight')
    ax.axis('off')

    # Plot the table
    table = ax.table(cellText=counts.values,
                     colLabels=counts.columns.tolist(),  # Ensure columns are defined
                     cellLoc='center', loc='center')

    # Set the font size
    table.auto_set_font_size(False)
    table.set_fontsize(font_dicts['tick']['size'])
    
    # Set the font family
    plt.rcParams['font.family'] = font_dicts['tick']['family']

    # Adjust the first row
    table[0, 0].set_height(first_row_height)  # Adjust height as needed
    table[0, 1].set_height(first_row_height)  # Adjust height as needed
    for j in range(len(counts.columns)):
        table[0, j].set_fontsize(font_dicts['label']['size'])
        table[0, j].set_text_props(weight='bold')  # Make the header bold

    # Adjust heights of rows
    for i in range(len(counts)):
        table[i+1, 0].set_height(row_height)  # Adjust height as needed
        table[i+1, 1].set_height(row_height)  # Adjust height as needed

    # Adjust the figure size if necessary to avoid large dimensions
    fig.tight_layout()
    
    plt.savefig(save_path, bbox_inches='tight', dpi=150)