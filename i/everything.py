import numpy as np
import logplotter
import multiprocessing
import subprocess

equilibrium_frame = 30000
sigma = 3.405
b = 5.72 / sigma
n = 2 / b**3
a = 20 / sigma
Fx = 0.1


def simulate(num_spheres):
    cmd = "make data/porosity_%d.dat" % num_spheres
    print("Running `" + cmd + "`")
    subprocess.run(cmd.split(), stdout=subprocess.DEVNULL)
    data = logplotter.find_data(
        "data/log.flow_%d" % num_spheres, l0="Step v_mytime")
    steps = data["Step"]
    vxs = data["v_vcmx_moving"]

    equilibrium_index = np.searchsorted(steps, equilibrium_frame) + 1
    vx = np.mean(vxs[equilibrium_index:])

    viscosity = 0.62
    permeability = viscosity * vx / (n * Fx)

    with open("data/porosity_%d.dat" % num_spheres) as infile:
        porosity = float(infile.read())

    return porosity, permeability


num_spheres = list(range(10, 31))

result = np.zeros((len(num_spheres), 2))
with multiprocessing.Pool(4) as pool:
    result[:, :] = pool.map(simulate, num_spheres)

result = result[np.argsort(result[:, 0])]
porosities = result[:, 0]
np.savetxt("data/permeability.dat", result)

model = np.zeros((len(num_spheres), 2))
model[:, 0] = porosities
model[:, 1] = a**2 / 45 * porosities**3 / (1 - porosities)**2
np.savetxt("data/model.dat", model)
