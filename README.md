# Preface
This data container should be follow the ideas outlined by [openPMD](https://github.com/openPMD/openPMD-standard/blob/latest/STANDARD.md), as such comparability is desirable, but not strictly required. However it is deliberately planned to be more explicit to allow easy parsing and comparison between outputs from different simulation codes used in the accelerator world.

- strings may only contain ascii chars to increase portability.
- an example is given in the main in this repo

# Root
The root consists of the [Dump Groups](#Dump-Groups), with names following this format %06i, note that the standart does not enforce continious names, eg. [000000, 000001, 000055] is fine. In addition to those groups it consists of the following header attributes.

Path | Type |  Description | Required
:---|:---:|:---|:---:
/README | string | A top level attribute explaining the datastructure and how to use it. Will probaply be definedin the very end. | yes
/openPMD | string | version of the format in "MAJOR.MINOR.REVISION", see section "The versions of this standard", minor and revision must not be neglected | yes
/openPMDextension | uint32 | The bit-mask of unique IDs of applied extensions of the openPMD standard (see: Domain-Specific Extensions); to test for a specific extension ID perform a bit-wise AND operation on openPMDextension. **Would be great if we get our own number.** | yes
/software | string | the software/code/simulation that created the file including its version | yes | yes
/author | string | Author and contact for the information in the file | optional
/date | string | Date of creation in format "YYYY-MM-DD HH:mm:ss tz" | yes
/timestamp | uint64 |  Posix timestamp. **I know this is redundandent info but it mackes sorting of data easier.** | yes

# Dump Group
The dump group consists two optional subgroups being the [Mesh Group]{#Mesh-Group) and the [Particle Group](#Particle-Group). In addition it defines the following header attributes:

Path | Type |  Description | Required
:---|:---:|:---|:---:
../s | double | Distance traveld from the source. | optional
../ElementDescription | string | Name or description of particle dump. | optional
../ElementIndex | uint64 | Element index | optional

# Particle Group
The particle group should consists of different [Particle Items](#Particle-Item) and , [Particle Map Items](#Particle-Map-Item). The standart defines the following sub-groups:

##### Required
- 6D coordinates, [Particle Offset Item](#Particle-Offset-Item): They should consist of *x/px/y/py/z or t/pz* and have those names. Each quantity dimension should be independent of the others. This excludes definition momentum in  of px in radians and pz in terms of (pz - <pz>)/<pz>. If desired this columns can still be supplied. To increase accuracy use offset.

- status, [Particle Map Item](#Particle-Map-Item): valueMap[0] is required to be 'Alive' and valueMap[1] is required to be 'InValid'.
- charge, [Particle Offset Item](#Particle-Offset-Item): This defines the macro particle charge
- species, [Particle Map Item](#Particle-Map-Item): needs to define the valueMap. Allowed values are non-capital names of elementary particles (eg: electron, proton, positron, ...) or molecules (eg: H3O+ [hydronium], #235U-- [double negatively charged Uranium 235], M15.2+ [undefined particle with charge +elementary charge and 15.2 proton mass])

##### Optional, but defined
- Spin, [Particle Offset Item](#Particle-Offset-Item): They should be defined by the following names: spinX/spinY/spinZ. Definition of one, requires definition off all three of them.

In addition it defines the following header attributes:
Path | Type |  Description | Required
:---|:---:|:---|:---:
../charge | double | Total bunch charge in [C]. **This is redundandent information but still convinient**. | yes
../NumberOfParticles | uint64 | Total number of particles. **This is redundandent information but still convinient** | yes

# Particle Offset Item
Relative Path | Data type | Dimension | Description | Required
:---|:---:|:---:|:---|:---:
.../value | 1D Numeric | Attribute/Data set | Position in *x* with respect to .../offset. If constant along all the values it can optinally be replaced by an Attribute instead of a data set. |  yes
.../offset | Same type as ../value | Attribute | Offset which is added to value. | yes
.../max | Same type as ../value | Attribute | Maximum of .../value. NaN are ignored +inf is not. | yes
.../min | Same type as ../value | Attribute | Minimum of .../value. NaN are ignored -inf is not. | yes
.../unitConversion | double | Attribute | Conversion factor to SI base units. | yes
.../unitDescription | string | Attribute | Description of the unit. | yes
.../unitSymbol | string | Attribute | Required even if base unit. **I think it would be great if we could enfore an encoding. I would suggest Latex but would be open to things like html or others.** | yes

# Particle Map Item
Relative Path | Data type | Dimension | Description | Required
:---|:---:|:---:|:---|:---:
.../index | 1D unsigned integer | Attribute/Data set | If constant along all the values it can optinally be replaced by an Attribute instead of a data set. |  yes
.../valueMap | 1D string | Attribute/Data set | Holds the values to the indexes. | yes


# Mesh Group
**Somebody with more experience in that topic should write this section.**