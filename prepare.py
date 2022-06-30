import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sklearn.preprocessing
from sklearn import metrics
import acquire


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
                  'Reaching Mil Age Annually':'mil_age','Reserve Personnel':'res_personnel','Roadway Coverage':'road_cov',
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
    df =df.drop(columns= ['self_arty', 'towed_arty','attack_helicopters','dedicated_attack_aircraft',
                      'helo_carriers','aircraft_carriers','total_aircraft_strength'], axis=1) 
    df = df[['country', 'country_code', 'active_personnel', 'air_carriers', 'armored_vehicles', 'arty', 
         'attack_aircraft', 'avail_manpower', 'coastal_coverage', 'corvettes', 'defense_budget','destroyers', 
         'external_debt', 'fighters_interceptors','fit_for_service', 'gold_foreign_ex', 'frigates', 'helos', 
         'labor_force', 'merch_marine_fleet', 'mine_warfare', 'navy_ships', 'oil_consumption', 'oil_production', 
         'oil_reser', 'paramilitary', 'patrol_vess', 'ports', 'purchasing_power', 'railway_coverage', 'mil_age', 
         'res_personnel', 'road_cov', 'rocket_proj', 'shared_borders', 'special_mission', 'square_land_area', 
         'subs', 'tanker_fleet', 'tanks', 'total_pop', 'trainers', 'transports', 'waterways',  'total_air_strength', 
         'total_sea_strength', 'total_land_strength']]
    return df

    ######################################################################################################