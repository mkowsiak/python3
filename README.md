# Python3 - notes on Python Programming Specialization (Coursera)

This repository contains set of simple Python files that demonstrate how to use Python3.

# Structure of repository

    .
    |-- LICENSE.md                               - license of the project
    |-- README.md                                - this README.md file
    |-- data
    |   `-- simple.csv                           - simple input data
    `-- src
        |-- basic_python.py                      - very basic concepts of Python
        |-- classes.py                           - samples illustrating usage of classes
        |-- csv_files.py                         - some fun stuff related to CSV
        |-- dictionaries.py                      - dictionaries - [key, value] concept
        |-- exceptions.py                        - samples explaining exceptions
        |-- file_operations.py                   - samples related to dealing with files
        |-- frames.py                            - helper file with fancy frames in Unicode
        |-- functions.py                         - functions, lambas, arguments, etc.
        |-- map_filter.py                        - illustration of map/filter usage
        |-- nested_lists.py                      - nested lists in various falvors
        |-- rest_json.py                         - basics related to REST and JSON
        |-- sorting.py                           - sorting related samples
        |-- tuples_packing_and_unpacking.py      - playing with tuples
        `-- while_loops.py                       - towards infinity and beyond

# Running the code

    git clone https://github.com/mkowsiak/python3
    cd python3
    find . -name "*.py" -exec python3 {} \;

# Docker for this project

If you want to test `rest_json.py` locally, you can use another project created for this purpose: [JSONDocker](https://github.com/mkowsiak/JSONDocker)
