def make_spheres(lmpptr):
    import traceback
    try:
        from lammps import lammps
        import numpy as np

        num_spheres = 20
        lmp = lammps(ptr=lmpptr)
        sigma = lmp.extract_variable("sigma", "all", 0)
        radius = lmp.extract_variable("radius", "all", 0) / sigma
        num_spheres = int(lmp.extract_variable("num_spheres_int", "all", 0))
        print("PYTHON: radius = %g" % radius)
        print("PYTHON: num_spheres = %g" % num_spheres)

        lx = lmp.get_thermo("lx")
        ly = lmp.get_thermo("ly")
        lz = lmp.get_thermo("lz")

        xs = np.random.uniform(0, lx, size=num_spheres)
        ys = np.random.uniform(0, ly, size=num_spheres)
        zs = np.random.uniform(0, lz, size=num_spheres)

        for sphere in range(num_spheres):
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    for k in [-1, 0, 1]:
                        x = xs[sphere] + i * lx
                        y = ys[sphere] + j * ly
                        z = zs[sphere] + k * lz
                        cmds = [
                            "region mysphere sphere %g %g %g %g units box" %
                            (x, y, z, radius), "group matrix region mysphere",
                            "region mysphere delete"
                        ]
                        lmp.commands_list(cmds)
    except Exception:
        traceback.print_exc()
