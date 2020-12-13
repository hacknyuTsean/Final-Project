# Standard Compaction Test Analysis Program

*This is the final project for CE-UY 3013 Computing In Civil Engineering.*


This program analyzes the data obtained in a standard compaction test and
return the maximum dry unit weight for the given soil sample with a graph
of Dry Unit Weight vs Moisture Content that would help determine the optimal
moisture content, and a graph of ZAV Unit Weight vs Moisture Content for
verification that the maximum dry unit weight is in acceptable range, if the
Max Dry graph is on the left of the ZAV graph.

Assumptions:
* The data for weight input is assumed to be in units of pound (lb)
* The data for volume input is assumed to be in units of cubic feet (ft^3)
* There should be multiple trials, and thus, multiple sets of data
* The number of trials should be the same for each input

Inputs:
* preliminaries, including total weight of mold and the plate, volume of the mold, specific gravity of the soil
* total weight of the mold, base plate, and wet soil in each trial
* total mass of the can and wet soil in each trial
* total mass of the can and dry soil in each trial
* mass of the moisture can in each trial

Outputs:
* Demonstrations of the array of data that is inputted in the program
* A printed message that tells the user the data is already inputted
* Max dry unit weight
* Graph of Dry Unit Weight vs Moisture Content
* Graph of ZAV Unit Weight vs Moisture Content

## Setup
create a virtual environment first:
```
py -m venv venv
```
Run the virtual environment:
```
venv\Scripts\activate
```
Install the required libraries for this program:
```
pip install -r requirements.txt
```

## How to use the Program

First instantiate a new object of "Compaction_Test";

```python
>>> CompactionTest = Compaction_Test('Compaction Test')
```

Then, we can input the preliminary data

```python
>>> CompactionTest.add_PreData(10.35,1/30,2.68)
```

Next, we input data obtained in the experiment for each trial.

"add_weightandwetSoil" is where we input data of total weight of the mold, base plate, and wet soil in each trial

"add_masscanandwetSoil" is where we input data of total mass of the can and wet soil in each trial

"add_masscananddrySoil" is where we input data of total mass of the can and dry soil in each trial

"add_massmoistcan" is where we input data of mass of the moisture can in each trial


```python
>>> CompactionTest.add_weightandwetSoil((14.19,14.41,14.53,14.63,14.51,14.47))
```

```python
>>> CompactionTest.add_masscanandwetSoil((253,354,439,490,422.8,243))
```

```python
>>> CompactionTest.add_masscananddrySoil((237,326,401,441.5,374.7,211.1))
```

```python
>>> CompactionTest.add_massmoistcan((54,53.3,53.3,54,54.8,40.8))
```


Then, we calculate the moist soil unit Weight
```python
>>> CompactionTest.cal_moistsoilUW()
```

Next, we calculate the moisture content in each trial
```python
>>> CompactionTest.cal_moistC()
```


Then, we calculate the dry unit weight of soil in each trial
```python
>>> CompactionTest.cal_dryUW()
```

Next, we calculate the zav unit weight of soil in each trial
```python
>>> CompactionTest.cal_zav()
```

Finally, we graph the Unit weight vs Moisture Content and print the result
```python
>>> CompactionTest.draw_UWvsMC()
```
