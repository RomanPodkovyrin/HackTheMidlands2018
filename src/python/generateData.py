import csv
import random
api_key = 'fddb1aa2d4034f6d105a0dd0defd9cd2'
with open('synthetic_data.csv', mode='w') as datafile:

data_writer = csv.writer(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

fromvalue = 1262304000 #01/01/2010 @ 12:00am (UTC)
tovalue = 1541286798    #11/03/2018 @ 11:13pm (UTC)


for i in range (400):
    randomUnix = random.randint(fromvalue,tovalue)
    temp =
    humidity=
    preci=
    wind=
    data_writer.writerow(['John Smith', 'Accounting', 'November'])