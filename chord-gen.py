import matplotlib.pyplot as plt
import json


def find_smallest_fret_number(finger_positions):
    smallest_fret_number = 30

    # Iterate over the finger positions
    for string, fret in finger_positions.items():
        if fret != 'x' and fret < smallest_fret_number:
            smallest_fret_number = fret

    return smallest_fret_number

def draw_chord(chord_name, finger_positions):
    # Define the number of strings and frets on the guitar
    num_strings = 6
    num_frets = 4
    smallest_fret_number =  find_smallest_fret_number(finger_positions)
    print(smallest_fret_number)
    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(6, 8))

    # Set the title of the plot
    ax.set_title(chord_name, fontsize=46, fontweight='bold')




    ax.set_xlim(.8, num_strings+.2)
    ax.set_ylim(0, num_frets)

    # Draw horizontal lines for each fret
    for i in range(num_frets + 1):
        ax.axhline(y=i, xmin=0.0457, xmax=0.9553, color='black',linewidth=1 )

    # Draw vertical lines for each string
    for i in range(num_strings + 1):
        line_color = 'black'
        line_width = 4.0
        if i > 0:
            line_width = 4.5 - i*.5
        ax.axvline(i, color=line_color, linewidth=line_width)

    #Draw minimum fret
    if smallest_fret_number>0:
        ax.text( .5, num_frets - .5 , smallest_fret_number , fontsize=24, ha='center', va='center')

    # Plot the finger positions on the fretboard
    for string, fret in finger_positions.items():
        if fret == 'x':
            ax.text( num_strings - int(string) + .1 + .7 + .2, num_frets +.2 , 'x', fontsize=14, ha='center', va='center')
            # ax.scatter(1, num_strings - int(string) + 1, color='black', edgecolors='black', s=150)
        elif fret == 0:
            continue
        elif smallest_fret_number>0:
            fret = str(int(fret) - smallest_fret_number + 1) 
            ax.scatter(num_strings - int(string) + 1, num_frets - int(fret) + .5, color='blue', edgecolors='black', s=450)
        else:
            ax.scatter(num_strings - int(string) + 1, num_frets - int(fret) + .5, color='blue', edgecolors='black', s=450)

    # Hide the axis labels
    ax.set_axis_off()

    # Save the figure with the chord name as the filename
    plt.savefig(f"chords-image/{chord_name}.png")

    # Show the plot
    # plt.show()

# Read chord data from JSON file
with open('chords.json') as f:
    chord_data = json.load(f)

# Iterate over the chord data
for chord_name, finger_positions in chord_data.items():
    # Call the draw_chord function for each chord
    draw_chord(chord_name, finger_positions)
