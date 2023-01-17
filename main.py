import pandas as pd

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

# Does GDP correlate with time?

# Does life span correlate with time?

# Does life span correlate with gdp?



