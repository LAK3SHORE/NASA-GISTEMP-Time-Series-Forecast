import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

def setup_custom_theme():
    
    DARK_BLUE_BG = '#254D70'
    
    COLORS = {
        'primary': '#00D9FF',      # Bright cyan
        'secondary': '#FF6B6B',    # Coral red
        'accent1': '#4ECDC4',      # Turquoise
        'accent2': '#FFE66D',      # Soft yellow
        'accent3': '#95E1D3',      # Mint green
        'accent4': '#FF8CC8',      # Pink
        'accent5': '#98D8C8',      # Seafoam
        'text': '#FFFFFF',         # White text
        'grid': '#3D6A8C',         # Lighter blue for grid
        'subtext': '#B8D4E3'       # Light blue for secondary text
    }
    
  
    custom_style = {
        'figure.facecolor': DARK_BLUE_BG,
        'figure.edgecolor': DARK_BLUE_BG,
        
        'axes.facecolor': DARK_BLUE_BG,
        'axes.edgecolor': COLORS['grid'],
        'axes.labelcolor': COLORS['text'],
        'axes.titlecolor': COLORS['text'],
        'axes.grid': True,
        'axes.grid.axis': 'both',
        'axes.spines.left': True,
        'axes.spines.bottom': True,
        'axes.spines.right': False,
        'axes.spines.top': False,
        
        'grid.color': COLORS['grid'],
        'grid.alpha': 0.3,
        'grid.linestyle': '--',
        'grid.linewidth': 0.8,
        
        'xtick.color': COLORS['text'],
        'ytick.color': COLORS['text'],
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        
        'legend.facecolor': DARK_BLUE_BG,
        'legend.edgecolor': COLORS['grid'],
        'legend.framealpha': 0.9,
        'legend.labelcolor': COLORS['text'],
        
        'text.color': COLORS['text'],
        'font.size': 11,
        'font.family': 'sans-serif',
        
        'lines.linewidth': 2,
        'lines.antialiased': True,
        
        'patch.facecolor': COLORS['primary'],
        'patch.edgecolor': COLORS['text'],
        'patch.antialiased': True,
        
        'savefig.facecolor': DARK_BLUE_BG,
        'savefig.edgecolor': DARK_BLUE_BG,
    }
    

    plt.rcParams.update(custom_style)
    
    palette_main = [
        COLORS['primary'],
        COLORS['secondary'], 
        COLORS['accent1'],
        COLORS['accent2'],
        COLORS['accent3'],
        COLORS['accent4']
    ]
    
    sns.set_palette(palette_main)
    
    return COLORS, palette_main


def create_custom_figure(figsize=(12, 8), title=None):
    """Create a figure with custom dark blue background"""
    COLORS, _ = setup_custom_theme()
    
    fig, ax = plt.subplots(figsize=figsize)
    
    if title:
        fig.suptitle(title, fontsize=16, color=COLORS['text'], y=0.98)
    
    fig.patch.set_facecolor('#254D70')
    ax.set_facecolor('#254D70')
    
    return fig, ax

def style_axis(ax, xlabel=None, ylabel=None, title=None):
    """Apply custom styling to an existing axis"""
    COLORS, _ = setup_custom_theme()
    
    if xlabel:
        ax.set_xlabel(xlabel, color=COLORS['text'], fontsize=12)
    if ylabel:
        ax.set_ylabel(ylabel, color=COLORS['text'], fontsize=12)
    if title:
        ax.set_title(title, color=COLORS['text'], fontsize=14, pad=10)
    
    ax.spines['bottom'].set_color(COLORS['grid'])
    ax.spines['left'].set_color(COLORS['grid'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.tick_params(colors=COLORS['text'], which='both')

    ax.grid(True, alpha=0.3, color=COLORS['grid'], linestyle='--')
    
    return ax

if __name__ == "__main__":
    COLORS, palette = setup_custom_theme()