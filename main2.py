# main.py
from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Draw Categorical Plot
cat_plot = draw_cat_plot()
cat_plot.savefig('catplot.png')

# Draw Heat Map
heat_map = draw_heat_map()
heat_map.savefig('heatmap.png')
