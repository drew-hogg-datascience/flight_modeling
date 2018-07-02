# flight_modeling
Analysis of historical United flights and prediction of future air traffic at Dulles

## Data and Directory Structure
Once downloaded, the project expects to have all Python files in a "code" subdirectory and all data in a "data" subdirectory on the same level.  The data can be downloaded here: https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236

I downloaded data back to 2013.  Each file has a random name, which the reduction code can handle.  

## Requirements

Python version 2.4.14
Pandas version 0.23.1
Sklearn version 0.19.1

## Running the reduction code

To run the reduction script reduce_data.py, first import it

`import reduce_data`

then run the script

`reduce_data.main()`

It will then produce a file named united_flight_data.csv that will be a csv text file.
