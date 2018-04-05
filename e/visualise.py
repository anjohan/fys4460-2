import ovito
import ovito.modifiers
import ovito.vis

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
    property="v", gradient=gradient, start_value=0, end_value=1E-10)
pipeline.modifiers.append(velocitycolour)

pipeline.add_to_scene()
"""
vp = ovito.vis.Viewport(type=ovito.vis.Viewport.Type.ORTHO)
vp.zoom_all()
vp.render_image(
    filename="data/vis.png",
    size=(1920, 1080),
    renderer=ovito.vis.TachyonRenderer())
"""
