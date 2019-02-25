import craigalist as crag
import googlemap as map
import Yelp as yelp
import apartment as ap
import pandas as pd
import numpy as np
import time
import re


def find_apartment(neighbor_index, neighborhoods):
    neighbor_name = str(neighborhoods.loc[neighbor_index, 'Neighborhood'])
    result_crag = crag.scrp_craigs(neighbor_name)
    df_result_crag = pd.DataFrame(result_crag, columns= ["Name", "Price", "Address", "URL"])
    result_apart = ap.scrp_apartment(neighbor_name)
    df_result_apart = pd.DataFrame(result_apart, columns=["Name", "Price", "Address", "URL"])
    df_result = pd.concat([df_result_apart, df_result_crag],axis=0,ignore_index=True)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('max_colwidth', 100)
    addresses_series = df_result["Address"]
    address = [str(i) for i in addresses_series]
    distance = []
    duration = []
    for i in address:
        if i != 'N/A':
            distance_i, duration_i = map.distance_to_school(i)
            distance.append(distance_i)
            duration.append(duration_i)
        else:
            distance.append(None)
            duration.append(None)

    df_result['Distance'] = distance
    df_result['Duration'] = duration
    df_result.sort_values(by='Distance', ascending=True)
    df_transposed = df_result.T
    # for i in df_transposed.columns.tolist():
    #     print(df_transposed.columns.tolist())
    #     print(df_transposed[i])
    print(df_transposed)

    # df_transposed.style.set_properties(**{'text-align': 'right'})
    # pd.set_option('display.width', 100)
    # print(df_transposed)
    return df_result

def find_yelp(index, apart_result):
    address = apart_result.loc[index, 'Address']
    print(str(address))
    yelp_list = yelp.restaurant(str(address))
    df_yelp = pd.DataFrame(yelp_list, columns=['Name', 'Rating', 'URL'])
    df_yelp.sort_values(by='Rating', ascending=False)
    print(df_yelp)


def load_neighborhood():
    neighborhoods = pd.read_csv('crime score.csv', skip_blank_lines=True)
    neighborhoods = pd.DataFrame(neighborhoods)
    # neighborhoods = neighborhoods.sort_values(by='Total', ascending=True)
    # neighborhoods = neighborhoods.rename(index=[0,1,2,3,4])
    # neighborhoods = neighborhoods['Total', 'Incident rate']
    print(neighborhoods)
    return neighborhoods

while(True):
    neighbors = load_neighborhood()
    # # find_apartment(0, neighbors)
    input1 = int(input('Choose a neighborhood index'))

    apartments = find_apartment(input1, neighbors)
    while True:
        n = int(input('Choose an option:\n'
                      '0. Show average distance\n'
                      '1. Look into one item\n'
                      '2. Back'))
        if n == 2:
            break
        elif n == 1:
            index = int(input("Input the item number"))
            yelp_result = find_yelp(index, apartments)
            continue

        elif n == 0:
            print(np.nanmean(apartments['Distance']))
            continue





