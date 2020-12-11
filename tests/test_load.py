from discretizer.io import load_tunnel_from_pdb

from conftest import data_path


def test_load_pdb():
    tunnel = load_tunnel_from_pdb(data_path("tunnel1.pdb"))
    assert len(tunnel.spheres) == 13
    assert list(tunnel.spheres[0].center) == [3.77, 67.705, 64.323]
    assert tunnel.spheres[0].radius == 3.22
