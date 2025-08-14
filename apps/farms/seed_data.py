"""Seed: 180 farms x 3 plots, 500 soil readings correlated"""
import random, uuid, datetime
random.seed(123)
def generate():
    farms=[]
    for i in range(180):
        farm={"id": str(uuid.uuid4()), "name": f"Farm-{i}", "owner": f"Farmer {i}", "acreage": round(random.uniform(1.5,12.5),2)}
        plots=[]
        for p in range(3):
            ndvi=round(random.uniform(0.2,0.85),2)
            yld= round(ndvi*4.2 + random.uniform(-0.3,0.3),2)  # correlated yield
            payment_delay = "delayed" if ndvi<0.45 and yld<1.8 else "on_time"
            plots.append({"plot_id": str(uuid.uuid4()), "farm_id": farm["id"], "wkt": f"POLYGON(({random.uniform(75,77):.4f} {random.uniform(18,22):.4f},...))", "ndvi": ndvi, "yield": yld, "payment": payment_delay})
        farms.append({"farm": farm, "plots": plots})
    readings=[]
    for r in range(500):
        farm=random.choice(farms)
        plot=random.choice(farm["plots"])
        # low NDVI correlates with low nutrients
        base_n= 18 if plot["ndvi"]<0.45 else 32
        readings.append({"plot_id": plot["plot_id"], "ph": round(random.uniform(5.5,7.8),1), "nitrogen": round(random.gauss(base_n,4),1), "moisture": round(random.uniform(0.2,0.55),2), "ndvi": plot["ndvi"]})
    return {"farms": farms, "readings": readings}

if __name__=="__main__":
    data=generate()
    print(f"seeded {len(data['farms'])} farms, {sum(len(f['plots']) for f in data['farms'])} plots, {len(data['readings'])} readings")
