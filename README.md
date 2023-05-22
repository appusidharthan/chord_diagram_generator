# Guitar Chord Diagram Generator

This project generates guitar chord diagrams based on chord data provided in a JSON file. It uses Matplotlib library to visualize chord shapes on a guitar fretboard and saves them as image files. The script also displays the smallest fret number on the diagram.

## Features

- Read chord data from a JSON file.
- Plot chord shapes on a guitar fretboard.
- Save chord diagrams as image files.
- Display the smallest fret number on the diagram.
- Simplify the process of visualizing and learning guitar chords.

## Requirements

- Python 3.x
- Matplotlib library

## Usage

1. Prepare a JSON file containing chord data in the following format:
```json
{
"chord_name": {
"string1": position1,
"string2": position2,
...
"string6": position6
},
...
}
```

2. Run the script `chord_diagram_generator.py` and it will generate chord diagrams for each chord defined in the JSON file.

## Example

Refer to the provided `chords.json` file for an example of chord data format. The generated chord diagrams will be saved as image files in the `chords-image` directory.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and enhance the script to suit your specific needs.


  