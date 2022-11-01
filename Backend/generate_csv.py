import csv
import random

records = 100
print("Making %d records\n" % records)

fieldnames = ["time", "flips", "result"]
# writer = csv.DictWriter(open("alzheimers.csv", "w"), fieldnames=fieldnames)

# writer.writerow(dict(zip(fieldnames, fieldnames)))

MAX_TIME = 120
MAX_FLIPS = 70
MIN_FLIPS = 16
MIN_TIME = 100
final = []
res = []


def createDS():
    for i in range(0, records):
        time = random.randint(0, MAX_TIME)
        flips = random.randint(0, 70)
        result = 0
        if flips >= MIN_FLIPS and (time > MIN_TIME and time < MAX_TIME):
            result = 1
        elif flips < 16:
            result = 0
        else:
            result = 0

        final.append([time, flips])
        res.append(result)
        # writer.writerow(
        #     dict(
        #         [
        #             ("time", time),
        #             ("flips", flips),
        #             ("result", result),
        #         ]
        #     )
        # )

    return final, res
