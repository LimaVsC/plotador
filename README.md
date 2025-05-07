# Plotador

<img src="./docs/images/plotador.png" alt="step1" width="700"/>

Plotador is a simple and easy-to-use plotting app built with [Flet](https://github.com/flet-dev/flet).  
It uses [Seaborn](https://github.com/mwaskom/seaborn) to create and customize your graphs, all through a clean and intuitive interface.

No login, no subscription — everything runs locally!

## How to use

The first thing to do is to choose a file with your data. To do this, click the "plus" button at the botton left. 
A dialog will open allowing you to browse and choose your file. For this example, we'll be using a dataset from Seaborn called "flights".

<img src="./docs/images/step_1.png" alt="step1" width="700"/>

Now we can select the plot type. Plotador supports three types: distribution, scatter and line. 
We'll select the line option on the right side of the interface.

<img src="./docs/images/step_2.png" alt="step2" width="700"/>

After choosing the plot type, we need to select the information for each axis. 
Just below the plot type, we can find two dropdows — one for each axis (X and Y). 
We'll select "year" for the X-axis and "passengers" for the Y-axis.

<img src="./docs/images/step_3.png" alt="step3" width="700"/>

A plot showing the number of passengers per year will appear in the center of the screen. 
Now we can further customize the plot by clicking the "Properties" tab at the top right.

<img src="./docs/images/step_4.png" alt="step4" width="700"/>

Here, we can change the apperance of the plot and/or add more information to it. 
For example, let's say we want to know if the number of passengers varies depending on the mouth of the year. 
We can select the "month" option in the "Hue" dropdown. 
This option will draw a separate line for each month on the same plot.

<img src="./docs/images/step_5.png" alt="step5" width="700"/>

Plotador automatically sets different colors for each month and adds a legend on the right side of the plot.

<img src="./docs/images/step_6.png" alt="step6" width="700"/>


When you're happy with the plot, you can save it by clicking the save button. 
This will open a dialog so you can choose where to save the file and name the figure as you wish.

<img src="./docs/images/step_7.png" alt="step7" width="700"/>

After confirming the save process, you can find the figure where you saved it. 
Plotador saves your plot as a .png image.

<img src="./docs/images/step_8.png" alt="step8" width="700"/>


Now, explore other types of plots and available options!

## Plot types

Currently three types of plots are suported:

- Distribution;
- Line;
- Scatter;
- Categorical.

Each with its own customizations.

### Distribution

Plot distributions on 1D and 2D. A color bar can be added to 2D distributions. You can choose between:

- Histograms;
- KDE;
- eCDF.

2D KDE plots may take a second to load.

<img src="./docs/images/distribution.png" alt="distribution" width="700"/>

### Scatter

Make a scatter plot. You can set markers shape and size.

<img src="./docs/images/scatter.png" alt="scatter" width="700"/>

### Line

A line plot of your data. If multiple Y values are found for the same X value, a confidence interval is show. You can set line width and style.

<img src="./docs/images/line.png" alt="line" width="700"/>

### Categorical

Categorical plot. The following types are accepted:

- Strip;
- Swarn;
- Box;
- Violin;
- Boxen;
- Point;
- Bar;
- Count.

<img src="./docs/images/categorical.png" alt="line" width="700"/>


## Files Formats

- Plotador accepts CSVs and Excel files formats.

## Features

In addition to specific customizations, all plot types share the following features:

- **Title**:  
  Sets the title of the figure. When a value is selected in the "Column" option, it sets the title for each subplot column accordingly.

- **Labels**:  
  Sets the axis labels. For 1D distributions, the Y-axis label cannot be changed.

- **Columns**:  
  All plots include the options "Column" and "Column wrap".  
  - The "Column" option creates subplots based on a categorical column in your data. It generates one subplot per category (up to 15). If there are more than 15 categories, a dialog will prompt you to choose a different column.  
  - The "Column wrap" property defines how many subplots appear per row.

- **Auto-reload**:  
  If you edit the data file, the application will detect the changes and automatically update your plot.