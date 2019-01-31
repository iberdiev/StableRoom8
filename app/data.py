CHOICES = []
for i in range(10):
    CHOICES.append((i+1,str(i+1)))


COUNTRIES = tuple()
countries = ['Kyrgyzstan','Tajikistan','Kazakhstan','Pakistan']
for i in range(len(countries)):
    COUNTRIES += ((i,countries[i]),)

year = ['Preparatory','Freshman','Sophomore','Junior','Senior']
YEAR = ((0,'Preparatory'),(1,'Freshman'),(2,'Sophomore'),(3,'Junior'),(4,'Senior'))

sleep_time = ['8:30PM or earlier','9PM', '9:30PM', '10PM', '10:30PM','11PM', '11:30PM','12AM', '12:30AM','1AM', '1:30AM or later']
SLEEP_TIME = []
for i in range(len(sleep_time)):
    SLEEP_TIME.append((i,sleep_time[i]))

wake_time=['5AM','5:30AM','6AM','6:30AM','6AM','7:30AM','8AM','8:30','9','9:30','10:00 or later']
WAKE_TIME = []
for i in range(len(wake_time)):
    WAKE_TIME.append((i,wake_time[i]))

SIZE = tuple()
size = ['XS','S','M','L','XL','XXL']
for i in range(len(size)):
    SIZE += ((i,size[i]),)

CAMPUSES = tuple()
campuses = ['Naryn','Khorog','Tekeli']
for i in range(len(campuses)):
    CAMPUSES += ((i,campuses[i]),)

gender = ['male', 'female']

yes_no = ['No','Yes']
