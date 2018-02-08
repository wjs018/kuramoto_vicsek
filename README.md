# Kuramoto-Vicsek

This repository was originally written by [lisamnash](https://github.com/lisamnash). I have modified it to streamline it a bit for my purposes and make it run more efficiently. This code implements a Kuramoto-Viscek model to simulate flocking of self-propelled agents in two dimensions.

Details on the Kuramoto-Vicsek model can be found here: https://arxiv.org/abs/1306.3372

This code implements equations 2.1 and 2.2 from the paper above. Input parameters can be changed in the file `input.py` and the available parameters are detailed below.  If an output is set, then an .mp4 file is saved with the video of the simulation.

## Short Intro to the Kuramoto-Vicsek model:
Flocking is a familiar concept to all of us.  We've all seen flocks of birds, schools of fish, or herds of buffalo.  In all of the cases of flocking in nature, we see long range order emerge from short-range interactions.  Animals (let's call them birds) at opposite ends of the flock cannot communicate, but still seem to move together.  How can this be?

In fact, flocking can be explained in 2D by a very simple model, which has been dubbed the Vicsek model after its originator. The rules for the Vicsek model are simple:
- A large number of point particles (birds) move over time through a space of dimension d.  Each bird attempts to follow its neighbors.  That is to say, that the bird will adjust its orientation to match its neighbors
- The interactions are purely short ranged.  The birds can only see a finite distance around them. 
- Following is not perfect.  This means that each bird tries to match the orientation of its neighbor, but makes mistakes. 
- The underlying model has rotational symmetry: The flock is equally likely to move in any direction. In my model this means that I start the birds with random orientations.

The Kuramoto model describes synchronization of rotating objects in a similar manner.

In this repository you will find the two of these models together. Our birds will try to align with each other, but they all will want to travel in circles if there is no external alignment.


## Modifying the input parameters

The input parameters of the simulation can be modified in the file `input.py`. Below is an explanation of each of the available input parameters. 

- `sim_time` : The length of time that is simulated in the code.
- `delta_t` : The amount of time that each time step simulates. This is the delta_t used in Euler Method propagation.
- `output_file` : This is the filename of the .mp4 file that is created showing the simulation
- `save_movie` : Boolean that determines whether the resulting movie is saved or not. This is here because the movie creation is the most time intensive part of the code. So, by setting this to `False`, you can iterate other parts of the code more rapidly to see if the simulation is still running without errors.
- `initial_flocks` : You may either place birds randomly or place them in flocks.  If you set this parameter each entry in the master list represents a flock.  In this repository, an example is commented out in `input.py`. The first entry is [[5., 5.], 1., 50].  This says that the center of one flock is x = 5, y = 5.  The flock length is 1.  The number of birds in the flock is 50. This parameter will override `num_points` if given.
- `num_points` : Number of birds in simulation.  If no initial flocks are placed then the program will place this number of birds randomly in the starting box.
- `box_size` : The simulation box size.  The simulation has periodic boundary conditions and a square aspect ratio.
- `w_0` : If this or w_amp is non-zero then the birds will try to travel in circles. Birds will try to go in cirlces of radius speed/w. 
-  `w_amp`: Gives amplitude of randomness on circle sizes.
- `C` : Magnitude of noise in the orientation. This represents the mistake the bird makes in alignment.  The higher this number, the more likely it is that birds will make mistakes when trying to align.
- `nu` : Strength of the coupling between neighboring agents. The higher this coefficient, the quicker a bird will become aligned with its neighbors.  If set to 0, the birds will not align.
- `max_dist` : The maximum distance a bird looks to align.
- `max_num` : Some researchers have actually found that in starling flocks the birds only pay attention to their 7 nearest neighbors despite flock density!  Here you can set the maximum number of birds that each bird will pay attention to (will look at closest `max_num` birds).

## Running the simulation
To run the simulation, type the following from the directory containing the python scripts :

`python run_sim.py` 

## Interpreting the output
The output file is an mp4 of your simulation.  The colors of the birds correspond to their orientations.  If they all are the same color then they are aligned.

## Contact

- Walter Schwenger, wjs018@gmail.com
