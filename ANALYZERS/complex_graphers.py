from matplotlib.ticker import MaxNLocator
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

import pandas as pd

### BADDLY WRITTEN CODE

def graph_lokacije_pie(df: pd.DataFrame, save_directory: str):
    
    df['LOKACIJA'] = df['LOKACIJA'].apply(lambda x: ', '.join(x))

    # Assuming df['LOKACIJA'] is already defined
    font = {'family': 'DejaVu Sans', 'size': 22}

    # Get value counts and sort them
    counts = df['LOKACIJA'].value_counts()
    counts = counts.sort_index()

    # Define a list of light colors for the pie chart
    light_colors = [
        '#FFB3BA', '#FFDFBA', '#FFFFBA', '#BAFFC9',
        '#BAE1FF', '#FFC3A0', '#FF677D', '#D4A5A5',
        '#392F5A', '#FFE156', '#B9FBC0', '#A0E7E5',
        '#D2C6FF', '#FFABAB', '#FFC3A0'
    ]

    # Ensure the color list matches the number of categories
    colors = light_colors[:len(counts)]

    # Custom function for percentage display
    def func(pct):
        return f'{pct:.1f}%' if pct >= 5 else ''  # Show percentage only if >= 5%

    # Create the pie chart
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.pie(counts, labels=counts.index, colors=colors, autopct=func, startangle=90)

    # Add a title
    ax.set_title('Broj prijava po lokaciji', fontdict={'family': 'DejaVu Sans', 'size': 24}, pad=30, loc='center')

    # Adjust the aspect ratio to ensure pie is a circle
    ax.axis('equal')

    # Set font properties for the percentage labels
    plt.setp(ax.texts, fontname='DejaVu Sans', fontsize=12)

    # Save the figure
    plt.savefig(save_directory + 'prijave_po_lokaciji_pie.png', dpi=300, bbox_inches='tight')

def graph_time_distribution_skole(df: pd.DataFrame, save_directory: str):
    
    # Set the default font to DejaVu Sans
    plt.rc('font', family='DejaVu Sans')

    # Convert timestamp to datetime
    df['VRIJEME'] = pd.to_datetime(df['VRIJEME'])

    # Extract date from timestamp
    df['DATUM'] = df['VRIJEME'].dt.date

    # Group by date and school, then count submissions
    grouped = df.groupby(['DATUM', 'SKOLA']).size().unstack(fill_value=0)

    # Define custom colors for each school
    school_colors = {
        'MIOC': 'blue',
        'GLV': 'green',
        'GTB': 'red',
        'PŠVP': 'purple',
        'KGZ': 'orange'
    }

    # Plotting
    plt.figure(figsize=(12, 10))

    fig, ax = plt.subplots(figsize=(10, 8))
    # Use the colors in school_colors dict for the respective schools
    grouped.plot(kind='line', marker=None, color=[school_colors.get(school, 'black') for school in grouped.columns], ax=ax)

    plt.title('Vremenska distribucija prijava po školama', fontsize=24, pad = 30)
    plt.xlabel('Datum', fontsize=18, labelpad=20)
    plt.ylabel('Broj prijava', fontsize=18, labelpad=20)
    plt.legend(title='Škola', fontsize=14, title_fontsize=14, loc='upper right')

    # Set date format on the x-axis
    ax = plt.gca()
    # Set x-axis tick locator for more frequent ticks (daily ticks in this case)
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))  # Daily ticks
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))  # Croatian date format (day.month.year)

    # Set y-axis to show more frequent integer ticks
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=10))  # Increase nbins for more frequent ticks

    # Ensure the y-axis starts at zero
    ax.set_ylim(bottom=0)

    plt.xticks(fontname='DejaVu Sans', fontsize=12, rotation=45)
    plt.yticks(fontname='DejaVu Sans', fontsize=12)

    plt.grid()
    plt.tight_layout()

    plt.savefig(save_directory + 'vremenska_distribucija_prijava_po_skolama.png', dpi=300, bbox_inches='tight')
    
def graph_time_distribution_general(df: pd.DataFrame, save_directory: str):
    
    # Set the default font to DejaVu Sans
    plt.rc('font', family='DejaVu Sans')

    # Convert timestamp to datetime
    df['VRIJEME'] = pd.to_datetime(df['VRIJEME'])

    # Extract date from timestamp
    df['DATUM'] = df['VRIJEME'].dt.date

    # Group by date and count total submissions across all schools
    grouped = df.groupby('DATUM').size()

    # Plotting
    plt.figure(figsize=(12, 10))

    fig, ax = plt.subplots(figsize=(10, 8))
    # Plot the total submissions
    grouped.plot(kind='line', marker=None, color='blue', ax=ax)

    plt.title('Vremenska distribucija ukupnih prijava', fontsize=24, pad=30)
    plt.xlabel('Datum', fontsize=18, labelpad=20)
    plt.ylabel('Ukupan broj prijava', fontsize=18, labelpad=20)

    # Set date format on the x-axis
    ax = plt.gca()
    # Set x-axis tick locator for more frequent ticks (daily ticks in this case)
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))  # Daily ticks
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))  # Croatian date format (day.month.year)

    # Set y-axis to show more frequent integer ticks
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=10))  # Increase nbins for more frequent ticks

    # Ensure the y-axis starts at zero
    ax.set_ylim(bottom=0)

    plt.xticks(fontname='DejaVu Sans', fontsize=12, rotation=45)
    plt.yticks(fontname='DejaVu Sans', fontsize=12)

    plt.grid()
    plt.tight_layout()

    plt.savefig(save_directory + 'vremenska_distribucija_prijava.png', dpi=300, bbox_inches='tight')