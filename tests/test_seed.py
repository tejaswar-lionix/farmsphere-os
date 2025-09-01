
def test_seed_generation():
    from apps.farms.seed_data import generate
    data=generate()
    assert len(data["farms"])==180
    assert sum(len(f["plots"]) for f in data["farms"])==540
    assert len(data["readings"])==500
