import diffractsim
diffractsim.set_backend("CUDA") #Change the string to "CUDA" to use GPU acceleration
from cupyx.profiler import benchmark
import os
import cupyx

from diffractsim import PolychromaticField,ApertureFromImage, cf, mm, cm

F = PolychromaticField(
    spectrum=2 * cf.illuminant_d65, extent_x=18 * mm, extent_y=18 * mm, Nx=1024, Ny=1024
)
hexagon_path = os.path.join("examples","apertures","hexagon.jpg")
F.add(ApertureFromImage(hexagon_path, image_size=(5.6 * mm, 5.6 * mm), simulation = F))

for i in range(100):
    F.propagate(z=80*cm)
    rgb =F.get_colors()


#F.plot_colors(rgb, xlim=[-7* mm, 7* mm], ylim=[-7* mm, 7* mm])
