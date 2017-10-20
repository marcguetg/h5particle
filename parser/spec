# File specification:
x, y, z are defined in [m]
xp, yp, p are in Momentum defined as: gamma*beta


## File
 - Attribute
   - Header Describing the file structure
  - Groups with individual names

For each writing of a group the parser checks if the attribute *Header* exists if not it creates a header file containg info about the individual values and columns.

## Group
The parser creates the following attributes for the group. It first tries to get them from the structure. If this fails it calculates them according to the definition below.
### Attributes
Names | dtype | shape | How to calc when not given | Description  
:---:|:---:|:---:|:---|:---
Reference | double | (6) | Mean for each dimension | Reference position in [*x, xp, y, yp, z, p*]
Min | double | (6) | Minimum for each dimension | Minumum for each dimension in [*x, xp, y, yp, z, p*]
Max | double | (6) | Maximum for each dimension | Minumum for each dimension in [*x, xp, y, yp, z, p*]
2. Momentum | double | (6, 6) | According to description, note that we remove the offset of each dimension to make it independen of the reference particle. | Second order momentum eg: <(x - <x>)(delta - <delta>)>
s | double | (1) | NaN | Distance from beginning
q | double | (1) | NaN | Total charge
n particles | uint 64 | (1) | number of particles| Number of particles
Description | string | max 255 | '' | Descriptive string, will be converted to ASCII

### Datasets
Names | dtype | description  
:---:|:---:|:---
x  | double  | Offset in *x* [m]
xp  | double | Momentum offset in *y*
y  | double  | Offset in *y* [m]
yp  | double | Momentum offset in *y*
z | double | Offset in *z* [m]
delta | double | Momentum offset in *z*
ID | uint 64 | Unique particle ID

The dumper is assured to raise an exception when writing if:
- Data is not 1D (ValueError)
- Data is not castable to the defind datatype (TypeError)
- All vectors have the same length (ValueError)
 
## Proposed implementation in Python:
Sublcass *H5py.File*
### create_group(name='Bunch', **data)
##### Input
Name | Description
:---:| ---
Name | Name of the group, if group already exist dumper is assured to raise an exception (ValueError). 
Data | Is required to have at least all the values defined in *Datasets*. If attributes are decleared they are taken otherwhise they are calculated according their definition in *Attributes*
##### Output
Like for the baseclass it returns the group.

