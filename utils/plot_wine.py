import textwrap
from scipy import spatial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from math import pi
import pandas as pd


import random

def create_text(gs, n, pairing_description):
    ax = plt.subplot(gs[n])
    ax_h, ax_w = ax.bbox.height/72, ax.bbox.width/72

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.invert_yaxis()

    # Manually break the text into multiple lines
    lines = textwrap.wrap(pairing_description)

    # Join the lines with newline characters
    wrapped_text = '\n'.join(lines)

    # Display the wrapped text vertically
    text = f'Wine full description:\n\n{wrapped_text}'
    ax.text(x=0, y=1, s=text, fontsize=12, color='grey')

def make_spider(gs, n, data, title, color):

    occasion_attributes = {'romantic': '', 'moody': '', 'casual': '', 'fancy': ''}
    # number of variable
    categories = list(occasion_attributes.keys())
    N = len(categories)
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    # Initialise the spider plot
    ax = plt.subplot(gs[n], polar=True,)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=11)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0.25, 0.5, 0.75, 1.0], ["0.25","0.50","0.75", "1.00"], color="grey", size=0)
    plt.ylim(0, 1)

    # Ind1
    values = list(data.values())
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)

    # Add a title
    # Insert a line break in the title if needed
    title_split = str(title).split(',')
    new_title = []
    for number, word in enumerate(title_split):
        if (number % 2) == 0 and number > 0:
            updated_word = '\n' + word.strip()
            new_title.append(updated_word)
        else:
            updated_word = word.strip()
            new_title.append(updated_word)
    new_title = ', '.join(new_title)

    title_incl_pairing_type = new_title

    plt.title(title_incl_pairing_type, size=13, color='black', y=1.2)

def plot_wine_recommendations(pairing_wines, pairing_occasion_attributes, pairing_description):

    subplot_rows = 3
    subplot_columns = len(pairing_wines)
    fig = plt.figure(figsize=(30, 7), dpi=96)
    fig_height, fig_width = fig.get_size_inches()

    gs = gridspec.GridSpec(subplot_rows, subplot_columns, height_ratios=[3, 0.5, 1])

    spider_nr = 0
    number_line_nr = 4
    descriptor_nr = 8

    for w in range(len(pairing_wines)):
        make_spider(gs, spider_nr, pairing_occasion_attributes[w], pairing_wines[w], 'red')
        create_text(gs, descriptor_nr, pairing_description[w])
        spider_nr += 1
        number_line_nr += 1
        descriptor_nr += 1
    return fig


def process_input(occasion) :
    #random_input = [random.randint(1, 4) for i in range(4)]
    input_occasion = dict()
    input_labels = ["romantic_input", "moody_input", "casual_input", "fancy_input"]
    for i,j  in zip(input_labels, occasion) :
        input_occasion[i] = j
    input_occasion["romantic_sc_norm"] = input_occasion.pop('romantic_input')
    input_occasion["moody_sc_norm"] = input_occasion.pop('moody_input')
    input_occasion["fancy_sc_norm"] = input_occasion.pop('fancy_input')
    input_occasion["casual_sc_norm"] = input_occasion.pop('casual_input')
    print(input_occasion)
    return(input_occasion)

def filter_wine(data, input_occasion) :
    filtered = data.loc[(data["romantic_sc_norm"] == input_occasion["romantic_sc_norm"]) &
             (data["moody_sc_norm"] == input_occasion["moody_sc_norm"]) &
            (data["fancy_sc_norm"] == input_occasion["fancy_sc_norm"]) &
            (data["casual_sc_norm"] == input_occasion["casual_sc_norm"])]
    print(filtered.shape)
    return(filtered)

def pair_wine(data, filtered, input_occasion) :
    try :
        final_selection = filtered.sample(4)
    except ValueError :
        if len(filtered) == 0 :
            print("no wine matched found, using average of input")
            input_occasion_values = [i for i in input_occasion.values()]
            input_average = np.mean(input_occasion_values)
            # Input value
            input_value = input_average
            data["avg_sc"] = data[["romantic_sc_norm", "fancy_sc_norm", "moody_sc_norm", "casual_sc_norm"]].mean(axis=1)
            # Calculate absolute differences
            data['abs_diff'] = abs(data['avg_sc'] - input_value)
            # Find the row with the minimum absolute difference
            closest_row = data.loc[data['abs_diff'].idxmin()]
            # Filter the DataFrame for the closest row(s)
            closest_rows = data[data['abs_diff'] == closest_row['abs_diff']]
            default_key = 'casual_sc'
            # Sort the dictionary items based on values
            sorted_items = sorted(input_occasion.items(), key=lambda x: x[1], reverse=True)
            max_value = sorted_items[0][1]
            # Check if there are multiple maximum values
            multiple_max_values = [key for key, value in sorted_items if value == max_value]
            # If there are multiple maximum values, return the default key
            if len(multiple_max_values) > 1:
                max_pair = (default_key, max_value)
            else:
                max_pair = sorted_items[0]
            # Slice the string up to the index of the special character
            input_highest_sc = max_pair[0]
            index = input_highest_sc.index("sc")
            input_highest_sc = input_highest_sc[:index+2]
            final_selection = closest_rows.sort_values(input_highest_sc, ascending=False)[:4]
        else :
            final_selection = filtered

    desired_order_list = ["romantic", "moody", "casual", "fancy"]
    occasion_attributes = {'romantic': '', 'moody': '', 'casual': '', 'fancy': ''}
    occasion_attributes = {k: occasion_attributes[k] for k in desired_order_list}

    pairing_id = list(final_selection.index)
    occasion_scores = data.loc[pairing_id, ["romantic_sc", "moody_sc", "casual_sc", "fancy_sc"]]
    pairing_occasion_attributes = occasion_scores[["romantic_sc", "moody_sc", "casual_sc", "fancy_sc"]].to_dict('records')
    print(pairing_occasion_attributes)
    pairing_description = list(data.loc[pairing_id, ["description"]].description)
    print(occasion_scores)

    plot_wine_recommendations(pairing_id, pairing_occasion_attributes, pairing_description)
