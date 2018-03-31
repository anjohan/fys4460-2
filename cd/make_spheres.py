def make_spheres(lmpptr):
    import traceback
    try:
        from lammps import lammps
        import numpy as np

        num_spheres = 20
        lmp = lammps(ptr=lmpptr)
        sigma = lmp.extract_variable("sigma", "all", 0)
        rmin = 20 / sigma
        rmax = 30 / sigma

        lx = lmp.get_thermo("lx")
        ly = lmp.get_thermo("ly")
        lz = lmp.get_thermo("lz")

        xs = np.random.uniform(0, lx, size=num_spheres)
        ys = np.random.uniform(0, ly, size=num_spheres)
        zs = np.random.uniform(0, lz, size=num_spheres)
        rs = np.random.uniform(rmin, rmax, size=num_spheres)

        counter = 0
        for sphere in range(num_spheres):
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    for k in [-1, 0, 1]:
                        x = xs[sphere] + i * lx
                        y = ys[sphere] + j * ly
                        z = zs[sphere] + k * lz
                        r = rs[sphere]
                        cmd = "region s%d sphere %g %g %g %g units box" % (
                            counter, x, y, z, r)
                        lmp.command(cmd)
                        cmd = "group matrix region s%d" % counter
                        lmp.command(cmd)
                        counter += 1
    except Exception:
        traceback.print_exc()
