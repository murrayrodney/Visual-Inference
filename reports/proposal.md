# STAA 556: Visual Project Proposal

#### Team Members
- [Rodney Murray](mailto:Rodney.Murray@colostate.edu)
- [Brendon Stanley](mailto:Brendon.Stanley@rams.colostate.edu)

## Introduction

<p style="text-indent: 40px;">
    Hurricane Ian swept through the Hurricane Belt in 2022 leaving behind 149 deaths in Florida
and an estimated $113 Billion USD in damages (Florida Department of Law Enforcement; National Centers for Environmental Information).
Concerns were raised regarding the readability of the hurricane forecast maps and the "cone" used to predict the path of the hurricane (Dance and Ajasa).
News outlets have suggested that the cone is misleading and that the public may not understand the information presented (Pulver and Doyle).
This project aims to provide background to better understand how vision works and how to produce informative data visualizations.
The project will be a stepping stone for continued research of data visualization and how to communicate hurricane forecast data effectively.
</p>

<p style="text-indent: 40px;">
    Data for this project was collected in an experiment of 52 subjects enrolled in psychology 100 at CSU. Subjects were shown an image of dots via an online survey (see figure one) and 
asked to select the quadrant where the centroid of the dots was located (see figure two); i.e., where is the middle of the dots? Each image was show to the subject for less than a second before the
screen would change. Asking the subject to select the quadrant the centroid of the dots was in. The subjects' response was recorded along with metadata about the image. Each subject was 
randomly shown 200 images from a pool of 400 images. For each image there were 90 dots total with 30 red dots, 30 big dots, and 30 dots with black outlines.
</p>

The data were recorded in a CSV file with the following columns:

- `currImage`: the image ID (factor: 1-400)
- `subjID`: the subject ID (factor: 1-52)
- `resp`: subject response quadrant (factor: A, B, C, D)
- `corrQuad`: the correct quadrant (factor: A, B, C, D)
- `distToMiddle`: the distance from the centroid to the center of the screen (numeric)
- `meanSD`: the standard deviation of all the dots (numeric)
- `isColSame`: whether the quadrant for the mean of the red dots is the same quadrant as the mean of all the dots (boolean: 0, 1)
- `isSizeSame`: whether the quadrant for the mean of the big dots is the same quadrant as the mean of all the dots (boolean: 0, 1)
- `isPulseSame`: whether the quadrant for the mean of the dots with black outlines is the same quadrant as the mean of all the dots (boolean: 0, 1)
- `howManyCorr`: how many of the special groups (red, big, black outlines) have their mean in the same quadrant as the quadrant for the full group of dots (factor: 0-3) 

![Figure 1: Experiment Visual Stimulus](../references/figures/image_dots_example.png "Figure 3: Experiment Visual Stimulus")

<p align="center">
  Figure 1: Experiment Visual Stimulus Example
</p>

![Figure 2: Experiment Quadrants](../references/figures/quad_options_example.png "Figure 2: Experiment Quadrants")

<p align="center">
  Figure 2: Experiment Centroid Quadrant Options
</p>

Explain the study design. Include details such as sample size, whether this is an observational
study or experiment, etc.
Include other details as needed.

## Proposed Methods
* Response and predictor variables
* What analyses will be conducted
* How will assumptions be checked
* Results to be reported
* Other details

## Summary Statistics and Exploratory Analysis

<p style="text-indent: 40px;">
    Figure three shows the total number of times each quadrant appeared, and the
total number of times each quadrant was selected by the subjects. Quadrant `B` appeared
almost twice as often as the other quadrants combined biasing the data in favor of
quadrant `B`.
</p>

<p style="text-indent: 40px;">
    Looking at figure four, the accuracy for how often the subjects selected the correct
is shown. This is presented as the overall percentage of correct selections across all
subjects based on factors such as `isColSame`, `isPulseSame`, and `isSizeSame`, and `howManyCorr`.
Of the special factors, `isColSame`, `isPulseSame` and, `isSizeSame` the largest impact was `isPulseSame`.
Not only did this improve the median accuracy but also appears to reduce variability.
</p>

<p style="text-indent: 40px;">
    However, the larger question is what happens when multiple factors are combined. The `howManyCorr` factor shows that 
the more factors that are simultaneously true the higher the accuracy. There may be a potential interaction between 
the variables `isColSame`, `isPulseSame` and, `isSizeSame`. When `howManyCorr` is 3 the accuracy improves dramatically 
but so does the variability. Model selection will need to investigate this further.
</p>

![Figure 3: Quadrant Counts](../references/figures/Quad_Counts.png "Figure 3: Quadrant Counts")

<p align="center">
  Figure 3: Quadrant Counts
</p>

![Figure 4: Subject Accuracy](../references/figures/BoxPlots.png "Figure 4: Subject Accuracy")

<p align="center">
  Figure 4: Subject Accuracy
</p>

## References

Dance, Scott and Amudalat, Ajasa. "Cone of Confusion: Why Some Say Iconic Hurricane Map Misled Floridians, www.washingtonpost.com/climate-environment/2022/10/04/hurricane-cone-map-confusion/. Accessed 22 May 2024.

Florida Department of Law Enforcement. "Update: Florida Medical Examiners Commission Hurricane Ian Deaths." FDLE, February 2023, www.fdle.state.fl.us/News/2023/February/Update-Florida-Medical-Examiners-Commission-Hurric.

National Centers for Environmental Information (NCEI). "Billion-Dollar Weather and Climate Disasters." NOAA, 2022, www.ncei.noaa.gov/access/billions/events/US/2022?disasters%5B%5D=tropical-cyclone.

Pulver, Voyles, and Doyle, Rice. “Many People Misunderstand This Famous Hurricane Forecast Graphic. It Can Be a Deadly Mistake.” USA Today, Gannett Satellite Information Network, 20 Oct. 2022, www.usatoday.com/story/news/2022/10/19/hurricane-ian-new-criticism-for-the-cone-of-uncertainty/10529838002/. 
