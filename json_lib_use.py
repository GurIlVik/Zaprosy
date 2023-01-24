# json libary

from datetime import datetime
import json

mydict = {
    "one":   1,
    "two":   2,
    #"three": datetime.now(),
    "four":  [255, 255, 255, 255],
    datetime.now().strftime('%Y%m%d%H%M%S'): 3,
}

print(json.dumps(mydict))
