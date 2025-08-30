
def test_api_import():
    # ensures api modules importable
    import importlib
    for m in ["apps.farms.api_farms","apps.mandi_pricing.api_mandi_pricing"]:
        mod=importlib.import_module(m)
        assert mod is not None
