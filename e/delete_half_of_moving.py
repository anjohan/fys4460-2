def delete_half_of_moving(lmpptr):
    import traceback
    try:
        from lammps import lammps
        import numpy as np

        lmp = lammps(ptr=lmpptr)
        ids = lmp.extract_atom("id", 1)
        is_moving = lmp.extract_variable("is_moving", "all", 1)

        moving_ids = ids[is_moving == 1]
        delete_ids = moving_ids[::2]

        cmd = "group deletethese id " + " ".join(map(str, delete_ids))
        lmp.command(cmd)

        cmd = "delete_atoms group deletethese"
        lmp.command(cmd)

    except Exception:
        traceback.print_exc()
