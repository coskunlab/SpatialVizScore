from pathlib import Path

data_dir = (Path().cwd().parents[0] / 'data').absolute()
data_raw = data_dir / 'raw'
data_ROI = data_dir / 'ROI'
data_nuclei = data_dir / 'nuclei'

data_figure = (Path().cwd().parents[0] / 'figures').absolute()
data_cluster = data_figure / 'cluster'
data_ex_level = data_figure / 'expression_level'
data_pixels = data_figure / 'pixel'

# Marker group
Stroma = ['SMA', 'Vimentin', 'CD44', 'ECadherin', 'Col1']
DNA = ['DNA1', 'DNA2', 'H3K9me3', 'Histone3']
Immune = ['PDL1', 'Foxp3', 'CD4', 'CD68', 'CD20', 'CD8a', 'PD1', 'GranzymeB', 'CD3', 'Ki67', 'CD45RO']
Epithelial = ['ECadherin', 'PanKeratin', 'Ki67', 'MHCII']