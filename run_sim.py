import time
import numpy as np

import simulation_object as so
import visualizations as v

from input import parameter_dict

if __name__ == '__main__':
    
    delta_t = parameter_dict.pop('delta_t', 0.02)
    total_time = parameter_dict.pop('sim_time', 15)
    output_file = parameter_dict.pop('output_file', 'output.mp4')

    steps = np.ceil(total_time / delta_t)
    t = np.linspace(0, total_time, steps)

    st = time.time()
    X = []
    V = []
    
    sim = so.SimulationObject(parameter_dict, **parameter_dict)

    print('...running simulation...')
    for i in xrange(len(t) - 1):
        ti = t[i]
        ti1 = t[i + 1]
        sim.run_step_alt(ti, ti1)
        X.append(sim.current_points)
        V.append(sim.current_v)

        if i == len(t) - 2:
            et = time.time()

    print('time per step', (et - st) / len(t))

    print('...creating movie...')
    writer = v.initialize_movie_writer()
    data = np.array([X, V, t, sim.box_size, sim._max_dist])
    #v.write_movie(data, writer, movie_path_and_name=args.output_file)
    v.write_movie(data, writer, movie_path_and_name=output_file)
    print('...done!')
