from home.models import RealEstate
import pandas as pd

real = RealEstate.objects.all()

realDf = pd.DataFrame(real)

print(realDf)