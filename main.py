import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df = pd.read_csv('all_data.csv')

# Now that we have the data, let's separate the data for each country first.
gdp_dict = {

    "Chile": [],
    "China": [],
    "Germany": [],
    "Mexico": [],
    "America": [],
    "Zimbabwe": []

}
life_dict = {

    "Chile": [],
    "China": [],
    "Germany": [],
    "Mexico": [],
    "America": [],
    "Zimbabwe": []

}
years = list(dict.fromkeys(df.Year.to_list()))

for index in df.index:
    if(df["Country"][index] == "Chile"):
        #print(df["GDP"][index])
        gdp_dict["Chile"].append(df["GDP"][index])
        life_dict["Chile"].append(df["Life expectancy at birth (years)"][index])
    elif(df["Country"][index] == "China"):
        gdp_dict["China"].append(df["GDP"][index])
        life_dict["China"].append(df["Life expectancy at birth (years)"][index])
    elif(df["Country"][index] == "Germany"):
        gdp_dict["Germany"].append(df["GDP"][index])
        life_dict["Germany"].append(df["Life expectancy at birth (years)"][index])
    elif(df["Country"][index] == "Mexico"):
        gdp_dict["Mexico"].append(df["GDP"][index])
        life_dict["Mexico"].append(df["Life expectancy at birth (years)"][index])
    elif(df["Country"][index] == "United States of America"):
        gdp_dict["America"].append(df["GDP"][index])
        life_dict["America"].append(df["Life expectancy at birth (years)"][index])
    elif(df["Country"][index] == "Zimbabwe"):
        gdp_dict["Zimbabwe"].append(df["GDP"][index])
        life_dict["Zimbabwe"].append(df["Life expectancy at birth (years)"][index])

# we have separates lists containing the values for gdp and life expectancy for each country, now lets find some summary statistics.
gdp_avgs = {

    "Chile": sum(gdp_dict["Chile"]) / len(gdp_dict["Chile"]),
    "China": sum(gdp_dict["China"]) / len(gdp_dict["China"]),
    "Germany": sum(gdp_dict["Germany"]) / len(gdp_dict["Germany"]),
    "Mexico": sum(gdp_dict["Mexico"]) / len(gdp_dict["Mexico"]),
    "America": sum(gdp_dict["America"]) / len(gdp_dict["America"]),
    "Zimbabwe": sum(gdp_dict["Zimbabwe"]) / len(gdp_dict["Zimbabwe"])

}
life_avgs = {

    "Chile": sum(life_dict["Chile"]) / len(life_dict["Chile"]),
    "China": sum(life_dict["China"]) / len(life_dict["China"]),
    "Germany": sum(life_dict["Germany"]) / len(life_dict["Germany"]),
    "Mexico": sum(life_dict["Mexico"]) / len(life_dict["Mexico"]),
    "America": sum(life_dict["America"]) / len(life_dict["America"]),
    "Zimbabwe": sum(life_dict["Zimbabwe"]) / len(life_dict["Zimbabwe"])

}

#### Does GDP correlate with time? ####

## to find this, there are a few tools that we can use, such as visualisation tools like scatter plots and quantitative stats such as pearson correlation

## setting up the figure to show multiple plots in one window
fig = plt.figure(1)
cols = 3
rows = 2
i = 1
colors_list = ['brown', 'red', 'black', 'green', 'blue', 'purple']

## looping through each country in the dictionary so that we can create and label each scatter plot
for country in gdp_dict:
    fig.add_subplot(rows, cols, i)
    plt.scatter(x=years, y=gdp_dict[country], color=colors_list[i-1])
    plt.xlabel('Years (2000-2015)')
    plt.ylabel('GDP')
    plt.title(country, loc='right')
    plt.subplots_adjust(hspace=0.5, wspace=1)
    i += 1

## making sure plt.show() and supertitle is OUTSIDE the loop so that only one window is shown.
plt.suptitle("GDP vs. Time")
plt.savefig('gdp_time_plt.png')
plt.show()
plt.clf()

## calculating pearson correlation, storing p value and correlations in respective dictionaries.
corr_gdp_time_dict = {

    "Chile": [],
    "China": [],
    "Germany": [],
    "Mexico": [],
    "America": [],
    "Zimbabwe": []

}
p_gdp_time_dict = {

    "Chile": [],
    "China": [],
    "Germany": [],
    "Mexico": [],
    "America": [],
    "Zimbabwe": []

}

## looping through correlation calculations for each entry in the dictionary
for country in gdp_dict:
    corr_gdp_time_dict["{0}".format(country)], p_gdp_time_dict["{0}".format(country)] = pearsonr(years, gdp_dict[country])



#### Does life span correlate with time? ####
fig = plt.figure(1)
cols = 3
rows = 2
i = 1
colors_list = ['brown', 'red', 'black', 'green', 'blue', 'purple']

## looping through each country in the dictionary so that we can create and label each scatter plot
for country in life_dict:
    fig.add_subplot(rows, cols, i)
    plt.scatter(x=years, y=life_dict[country], color=colors_list[i-1])
    plt.xlabel('Years (2000-2015)')
    plt.ylabel('Life Expectancy')
    plt.title(country, loc='right')
    plt.subplots_adjust(hspace=0.5, wspace=1)
    i += 1

## making sure plt.show() and supertitle is OUTSIDE the loop so that only one window is shown.
plt.suptitle("Life Expectancy vs. Time")
plt.savefig('lifespan_time_plt.png')
plt.show()
plt.clf()


## calculating pearson correlation, storing p value and correlations in respective dictionaries.
corr_life_time_dict = {

    "Chile": [],
    "China": [],
    "Germany": [],
    "Mexico": [],
    "America": [],
    "Zimbabwe": []

}
p_life_time_dict = {

    "Chile": [],
    "China": [],
    "Germany": [],
    "Mexico": [],
    "America": [],
    "Zimbabwe": []

}

## looping through correlation calculations for each entry in the dictionary
for country in life_dict:
    corr_life_time_dict["{0}".format(country)], p_life_time_dict["{0}".format(country)] = pearsonr(years, life_dict[country])

#### Does life span correlate with gdp? ####
fig = plt.figure(1)
cols = 3
rows = 2
i = 1
colors_list = ['brown', 'red', 'black', 'green', 'blue', 'purple']

## looping through each country in the dictionary so that we can create and label each scatter plot
for country in life_dict:
    fig.add_subplot(rows, cols, i)
    plt.scatter(x=life_dict[country], y=gdp_dict[country], color=colors_list[i-1])
    plt.xlabel('Life Expectancy')
    plt.ylabel('GDP')
    plt.title(country, loc='right')
    plt.subplots_adjust(hspace=0.5, wspace=1)
    i += 1

## making sure plt.show() and supertitle is OUTSIDE the loop so that only one window is shown.
plt.suptitle("Life Expectancy vs. GDP")
plt.savefig('gdp_life_plt.png')
plt.show()
plt.clf()

## calculating pearson correlation, storing p value and correlations in respective dictionaries.
corr_gdp_life_dict = {

    "Chile": [],
    "China": [],
    "Germany": [],
    "Mexico": [],
    "America": [],
    "Zimbabwe": []

}
p_gdp_life_dict = {

    "Chile": [],
    "China": [],
    "Germany": [],
    "Mexico": [],
    "America": [],
    "Zimbabwe": []

}

## looping through correlation calculations for each entry in the dictionary
for country in gdp_dict:
    corr_gdp_life_dict["{0}".format(country)], p_gdp_life_dict["{0}".format(country)] = pearsonr(life_dict[country], gdp_dict[country])



#### Reports ####
with open('life_gdp_data_report.txt', 'w') as f:

    # averages
    f.write(" ==== GDP AVERAGES ==== ")
    f.write("\n")
    for country in gdp_avgs:
        f.write(f"{country}: {gdp_avgs[country]}")
        f.write("\n")
    f.write("\n")
    f.write(" ==== LIFE SPAN AVERAGES ==== ")
    f.write("\n")
    for country in life_avgs:
        f.write(f"{country}: {life_avgs[country]}")
        f.write("\n")
    f.write("\n")

    # correlations
    f.write(" ==== GDP vs. TIME CORRELATION ==== ")
    f.write("\n")
    for country in corr_gdp_time_dict:
        f.write(f"{country}: {corr_gdp_time_dict[country]}")
        f.write("\n")
    f.write("\n")
    f.write(" ==== LIFE SPAN vs. TIME CORRELATION ==== ")
    f.write("\n")
    for country in corr_life_time_dict:
        f.write(f"{country}: {corr_life_time_dict[country]}")
        f.write("\n")
    f.write("\n")
    f.write(" ==== GDP vs. LIFE SPAN CORRELATION ==== ")
    f.write("\n")
    for country in corr_gdp_life_dict:
        f.write(f"{country}: {corr_gdp_life_dict[country]}")
        f.write("\n")