import time
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as animation

import simulation_object as so
import isolum_rainbow

# Read in simulation parameters from input.py
from input import parameter_dict


def draw_frame(data, scaler, i, fig, ax, box_size):
    
    # Unpack the data
    x = data[0][i][:,0]
    y = data[0][i][:,1]
    u = scaler * data[1][i][:,0]
    v = scaler * data[1][i][:,1]
    
    # Calculate colors
    colors = (np.arctan2(v, u)) % (2 * np.pi)
    
    # Create the plot
    quiv = ax.quiver(x, y, u, v, colors, cmap='isolum_rainbow', angles='xy',
                     scale_units='xy', scale=1, headaxislength=9)
    
    # Format the plot
    ax.set_aspect(1)
    plt.xlim(-0, box_size)
    plt.ylim(-0, box_size)
    plt.xticks([])
    plt.yticks([])
    
    return fig, quiv
    

if __name__ == '__main__':
    
    # Get params from input that don't go into sim object
    delta_t = parameter_dict.pop('delta_t', 0.02)
    total_time = parameter_dict.pop('sim_time', 15)
    output_file = parameter_dict.pop('output_file', 'output.mp4')
    save_movie = parameter_dict.pop('save_movie', True)
    
    # Calculate simulation time parameters
    steps = np.ceil(total_time / delta_t)
    times = np.linspace(0, total_time, steps)
    
    # Some variable initialization
    st = time.time()
    positions = []
    velocities = []
    
    # Track a single particle
    p1_positions = np.zeros((len(times)-1, 2))
    
    # Create our simulation object
    sim = so.SimulationObject(parameter_dict, **parameter_dict)
    
    # Start our simulation
    print('...running simulation...')
    for i in xrange(len(times) - 1):
        
        # Looking ahead one time step for propagation
        ti = times[i]
        ti1 = times[i + 1]
        sim.run_step_alt(ti, ti1)
        
        # Record time step's array of positions and velocities
        positions.append(sim.current_points)
        velocities.append(sim.current_v)
        
        # Record position for first particle
        p1_positions[i, :] = positions[i][0,:]

        if i == len(times) - 2:
            et = time.time()

    print('real seconds per step: ' +  str((et - st) / len(times)))
    print('total elapsed time: ' +  str(et - st))

    # Define our scaler for plotting
    scaler = 1.2 * parameter_dict['box_size'] / 40.
    
    # Create the figure and axes to draw to
    fig = plt.figure(figsize=(10,10))
    ax = plt.axes([0,0,1,1])
    
    if save_movie:
        print('...creating movie...')
        
        # Pack our data
        data = []
        data.append(positions)
        data.append(velocities)
        
        # Create the movie writer
        writer = animation.FFMpegWriter(fps=40., bitrate=3000)
        
        with writer.saving(fig, output_file, 100):
            
            # Iterate through time steps
            for i in range(len(times) - 1):
                
                # Draw a frame of the movie
                fig, ca = draw_frame(data, scaler, i, fig, ax,
                                     parameter_dict['box_size'])
                writer.grab_frame()
                
                # Remove the arrows from previous frame
                ca.remove()
                
        print('...done!')
        print('movie writing time: ' + str(time.time() - et))
