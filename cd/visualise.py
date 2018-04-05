import ovito
import ovito.modifiers

pipeline = ovito.io.import_file("data/dump.lammpstrj", multiple_frames=True)

num_frames = pipeline.source.num_frames

velocitycomputer = ovito.modifiers.ComputePropertyModifier(
    output_property="v",
    expressions=[
        "sqrt(Velocity.X*Velocity.X"
        "+Velocity.Y*Velocity.Y+Velocity.Z*Velocity.Z)"
    ])
pipeline.modifiers.append(velocitycomputer)

gradient = ovito.modifiers.ColorCodingModifier.Grayscale()
velocitycolour = ovito.modifiers.ColorCodingModifier(
    property="v", gradient=gradient)
pipeline.modifiers.append(velocitycolour)

pipeline.add_to_scene()
