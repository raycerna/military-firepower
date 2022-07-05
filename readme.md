# Top Military Strengths by Country using PCA

## Project Description and Goals

### This is an analysis of the top militaries by country with the highest defense budget. This can deliver insight into current and future capabilities at a glance. My overall goal here is to show the features that are related to defense budget and how this makes a force not to be reckoned with. In the future with more available data, we can deliver critical insight into the current and future size, shape, and capabilities of the world's key military powers.


### Initial thoughts:
- The strongest military power has the highest defense budget.
- Smaller countries in square land area have less of a defense budget.
- The more a country has in debt, the more the country has in defense budget
- The greater the population of a country, the higher the defense budget.

## data dictionary:

### A complete listing of every feature can be found here: https://www.globalfirepower.com/country-military-strength-detail.php?country_id=united-states-of-america

| Feature                       | Definition                               
|-------------------------------|----------------------------------------------------------------------------|
|'Country'                      | Countries of the World considered                                          |
|'country_code'                 | Three-digit country code                                                   |           
|'active_personnel'             | all those personnel considered under active service status                 |
|'air_carriers'                 | Aircraft carrier fleet strength                                            |
|'armored_vehicles'             | Armored Fighting Vehicle fleet strength                                    |
|'arty'                         | Artillery fleet strength                                                   |
|'attack_aircraft'              | aircraft elements dedicated to ground strike                               |
|'avail_manpower'               | Military manpower in form of combat personnel and labor force              |
|'corvettes'                    | Warships typically smaller than frigates                                   |
|'defense_budget'               | Annual defense spending budget capability                                  |
|'destroyers'                   | Warships type is an advanced, multi-role surface vessel                    |
|'external_debt'                | both public and private debt carried as owed to outside parties            |
|'fighters_interceptors'        | Aircraft fighters (multirole, interceptors), trainers (basic, advanced),   |
|                               | transports (fixed-wing and helos), dedicated bombers and ground-attackers, |
|                               | special-missions platforms, etc.                                           |
|'frigates'                     | Frigate ship type is a multi-role, general purpose ocean-going vessel      |
|                               | utilized for fleet surface ship protection against enemy surface combatants|
|                               | or incoming aerial threats.                                                |
|'helos'                        | Total Helicopter strength                                                  |           
|'merch_marine_fleet'           | Force of ships operating under civilian banners in peace time and, in times|
|                               | of war, commissioned by the naval branch of service to augment the main    |
|                               | surface fighting force.                                                    |
|'mine_warfare'                 | Mine / countermine warfare ships                                           |
|'navy_ships'                   | Total Naval vessels                                                        |
|'oil_consumption'              | Applied as a penalty to each nation, the higher its consumption the worse  |
|                               | effect on a theoretical war effort.                                        |
|'oil_production'               | Total oil production                                                       |
|'oil_reser'                    | oil reserves of a given country based on its recognized reservoirs         |
|'paramilitary'                 | semi-military entities that can strengthen a given nation's fighting       |
|                               | capability on the ground.                                                  |
|'patrol_vess'                  | number of offshore patrol / missileboat / riverine combat warcraft         |
|'purchasing_power'             | economic adjustor to satisfy exchange rates between countries in relation  | 
|                               | to exhange of similar goods.                                               |
|'res_personnel'                | personnel considered under 'reserve status', these elements being          |
|                               | available, on-call for service at any given moment.The total tax assessed  |
|                               | value of the parcel                                                        |
|'road_coverage'                | total useable/useful Roadways                                              |
|'rocket_proj'                  | total self-propelled Multiple Launch Rocket Projector (MLRS) vehicle fleet |
|                               | strength.                                                                  |           
|'special_mission'              | Special Mission Aircraft are those platforms specifically developed to     |
|                               | undertake an over-battlefield role by utilization of advanced onboard      |
|                               | equipment or specialized trait.                                            |
|'square_land_area'             | Total square land coverage of a country.                                   |
|'subs'                         | Total modern attack submarines capable of sea- and land-attack through     |
|                               | conventional and nuclear means.                                            |
|'tanker_fleet'                 | Total aerial tanker aircraft fleet.                                        |
|'tanks'                        | Total combat tank fleet strength                                           |
|'total_pop'                    | Total population by country.                                               |
|'trainers'                     | Includes all training platform types serving to cover basic, advanced,     |
|                               | fighter, attack, helicopter, and general flight training of airmen.        |
|'transports'                   | Total Transport fleet strength - moves man and machines.                   |
|'total_air_strength'           | Total of all air capabilities.                                             |
|'total_sea_strength'           | Total of all sea capabilities.                                             |
|'total_land_strength'          | Total of all land capabilities.                                            |
|'total_strengths'              | Total of all air, land, and sea capabilities into one feature.             |



## project planning:
- Acquire
    - Acquired data from Kaggle: https://www.kaggle.com/datasets/prasertk/military-power-by-country-2022
        - Note: Functions to acquire data are built into the acquire.py file.
        - Loaded and inspected dataset.

- Prepare (can be viewed in prepare.py file)
    1. renamed columns (avoided spacing for easier coding)
    2. inspected data frame and found zeros or outliers where they likely should not be such as:
        1. changed to mean of entire feature.
        2. replaced outliers with zero.
    3. created additional features by grouping some that could be fit into one feature such as:
        1. attack_aircraft = any attack type aircraft.
        2. air_carriers = any air type carriers.
        3. arty = any type artillery.
        4. grouped air, land, and sea strengths into each individual category.
    4. Dropped columns that were not neccessary for this quick analysis (please see prepare.py file for feature drops)
    5. resorted the column titles.
    6. Only took the top 25 countries by highest defense budget.

- Explore
    - Performed univariate analysis on individual predictors of defense budget.
    - Performed bivariate and multivariate exploration on several features to find recommendations that drive defense budget.
    - Further explored features that I questioned in my initial thoughts.
    - Visualized features of defense budget by using heatmap, kdeplot, scatterplot.

- Model
    - Scaled data
    - Performed Principal Component Analysis (PCA)


## instructions on how to reproduce this project and findings

- Download acquire.py module and use it to acquire the data. 
- Download prepare.py module and use its functions to prepare the data.
- Explore on your own.

## Conclusion, key findings, recommendations, and takeaways from project:


### Reducing the number of variables by combining them into larger and more meaningful features was our overall goal and from the graph we can observe the separate clusters. The difference between components is now as large as possible. When we began, the data set had many features so reducing the dimensionality, using PCA we found out we only need three components to separate the data.
### Now we can see that USA, China, and Russia occupy their own clusters which means they have very strong militaries and definitely outnumber any other countries defense budget.