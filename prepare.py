import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sklearn.preprocessing
from sklearn import metrics
from sklearn.model_selection import train_test_split
import acquire

def split_military(df):
    '''
    This function performs split on zillow data.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123)

    print('Train: %d rows, %d cols' % train.shape)
    print('Validate: %d rows, %d cols' % validate.shape)
    print('Test: %d rows, %d cols' % test.shape)
    return train, validate, test

#####################################################################################################

def handle_zero(df):
    mean_active_pers = df['active_personnel'].mean(skipna=True)
    
    df['active_personnel']=df.active_personnel.mask(df.active_personnel == 0,mean_active_pers)
    
    return df

#####################################################################################################

def prep_military(df):
    '''
    returns a clean dataframe
    '''
    # renames the columns
    df = df.rename(columns={'Active Personnel': 'active_personnel', 'Aircraft Carriers': 'aircraft_carriers',
                   'Armored Vehicles':'armored_vehicles','Attack Helicopters':'attack_helicopters',
                   'Available Manpower':'avail_manpower','Coastline Coverage':'coastal_coverage','Corvettes':'corvettes',
                  'Dedicated Attack':'dedicated_attack_aircraft','Defense Budget':'defense_budget','Destroyers':'destroyers',
                  'External Debt':'external_debt','Fighters/Interceptors':'fighters_interceptors','Fit-for-Service':
                  'fit_for_service','Foreign Exchange/Gold':'gold_foreign_ex','Frigates':'frigates',
                  'Helicopter Carriers':'helo_carriers','Helicopters':'helos','Labor Force':'labor_force',
                  'Merchant Marine Fleet':'merch_marine_fleet','Mine Warfare':'mine_warfare','Navy Ships':'navy_ships',
                  'Oil Consumption':'oil_consumption','Oil Production':'oil_production','Oil Proven Reserves':'oil_reser',
                  'Paramilitary':'paramilitary','Patrol Vessels':'patrol_vess','Ports / Trade Terminals':'ports',
                  'Purchasing Power Parity':'purchasing_power','Railway Coverage':'railway_coverage',
                  'Reaching Mil Age Annually':'mil_age','Reserve Personnel':'res_personnel','Roadway Coverage':'road_coverage',
                  'Rocket Projectors':'rocket_proj','Self-Propelled Artillery':'self_arty','Shared Borders':'shared_borders',
                  'Special-Mission':'special_mission','Square Land Area':'square_land_area','Submarines':'subs',
                  'Tanker Fleet':'tanker_fleet','Tanks':'tanks','Total Aircraft Strength':'total_aircraft_strength',
                  'Total Population':'total_pop','Towed Artillery':'towed_arty','Trainers':'trainers',
                   'Transports':'transports','Waterways (usable)':'waterways'})
    df = handle_zero(df)
    df['active_personnel'] = df['active_personnel'].astype(int)
    df['arty'] = df['self_arty']+df['towed_arty']
    df = df.replace(2022,{'aircraft_carriers':0})
    df['attack_aircraft'] = df['attack_helicopters']+df['dedicated_attack_aircraft']
    df['air_carriers'] = df['aircraft_carriers']+df['helo_carriers']
    df['total_air_strength'] = df['fighters_interceptors']+df['helos']+df['attack_aircraft']+df['transports']+df['trainers']+df['special_mission']+df['tanker_fleet']
    df['total_sea_strength'] = df['air_carriers']+df['destroyers']+df['frigates']+df['corvettes']+df['subs']+df['patrol_vess']+df['mine_warfare']
    df['total_land_strength'] = df['tanks']+df['armored_vehicles']+df['arty']+df['rocket_proj']
    df['total_strengths'] = df['total_air_strength']+df['total_land_strength']+df['total_sea_strength']
    df =df.drop(columns= ['self_arty', 'towed_arty','attack_helicopters','dedicated_attack_aircraft','helo_carriers','aircraft_carriers','total_aircraft_strength',
         'coastal_coverage', 'fit_for_service','gold_foreign_ex','labor_force','ports','mil_age','shared_borders','waterways','railway_coverage'], axis=1) 
    df = df[['country', 'country_code', 'active_personnel', 'air_carriers', 'armored_vehicles', 'arty', 'attack_aircraft', 'avail_manpower', 'corvettes', 
         'defense_budget','destroyers','external_debt', 'fighters_interceptors', 'frigates', 'helos', 'merch_marine_fleet', 'mine_warfare', 
         'navy_ships', 'oil_consumption', 'oil_production','oil_reser', 'paramilitary', 'patrol_vess', 'purchasing_power', 
         'res_personnel', 'road_coverage','rocket_proj', 'special_mission', 'square_land_area', 
         'subs', 'tanker_fleet', 'tanks', 'total_pop', 'trainers', 'transports',  'total_air_strength', 
         'total_sea_strength', 'total_land_strength', 'total_strengths']]
    # let only focus on top 25 defense budgets
    df = df.sort_values(by=['defense_budget'], ascending=False).head(25)
    return df

    ######################################################################################################

def scale_data(train, validate, test):
    train = train.drop(['country','country_code'], axis=1)
    validate = validate.drop(['country','country_code'], axis=1)
    test = test.drop(['country','country_code'], axis=1)

    # Create the Scaling Object
    scaler = sklearn.preprocessing.MinMaxScaler()

    # Fit to the train data only
    scaler.fit(train)

    # use the object on the whole df
    # this returns an array, so we convert to df in the same line
    train_scaled = pd.DataFrame(scaler.transform(train))
    validate_scaled = pd.DataFrame(scaler.transform(validate))
    test_scaled = pd.DataFrame(scaler.transform(test))

    # the result of changing an array to a df resets the index and columns
    # for each train, validate, and test, we change the index and columns back to original values

    # Train
    train_scaled.index = train.index
    train_scaled.columns = train.columns

    # Validate
    validate_scaled.index = validate.index
    validate_scaled.columns = validate.columns

    # Test
    test_scaled.index = test.index
    test_scaled.columns = test.columns

    return train_scaled, validate_scaled, test_scaled

    #######################################################################################################

def percentage_stacked_plot(columns_to_plot, title, df):
    
    '''
    Returns a 100% stacked plot of the response variable for independent variable of the list columns_to_plot.
    Parameters: columns_to_plot (list of string): Names of the variables to plot
    '''
    
    number_of_columns = 2
    number_of_rows = math.ceil(len(columns_to_plot)/2)

    # create a figure
    fig = plt.figure(figsize=(12, 5 * number_of_rows)) 
    fig.suptitle(title, fontsize=22,  y=.95)
 

    # loop to each column name to create a subplot
    for index, column in enumerate(columns_to_plot, 1):

        # create the subplot
        ax = fig.add_subplot(number_of_rows, number_of_columns, index)

        # calculate the percentage of observations of the response variable for each group of the independent variable
        # 100% stacked bar plot
        prop_by_independent = pd.crosstab(df[column], df['defense_budget']).apply(lambda x: x/x.sum()*100, axis=1)

        prop_by_independent.plot(kind='bar', ax=ax, stacked=True,
                                 rot=0, color=['#94bad4','#ebb086'])

        # set the legend in the upper right corner
        ax.legend(loc="upper right", bbox_to_anchor=(0.62, 0.5, 0.5, 0.5),
                  title='country', fancybox=True)

        # eliminate the frame from the plot
        spine_names = ('top', 'right', 'bottom', 'left')
        for spine_name in spine_names:
            ax.spines[spine_name].set_visible(False)

    return percentage_stacked_plot