import logging

import numpy as np

from .tunnel import Sphere, Tunnel


def load_tunnel_from_pdb(path: str) -> Tunnel:
    spheres = []
    with open(path) as file:
        for line in file:
            words = line.split()
            if words and words[0] == "ATOM":
                center = np.array([float(w) for w in words[6:9]])
                radius = float(words[9])
                spheres.append(Sphere(center, radius))

        logging.info(f"Tunnel loaded ({len(spheres)} spheres).")
    return Tunnel(spheres)
