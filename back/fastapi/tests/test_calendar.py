from ics import Calendar
from ics import event

import requests

url = 'http://adelb.univ-lyon1.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=10107&projectId=2&calType=ical&firstDate=2020-11-09&lastDate=2020-11-14'





if __name__ == "__main__":
    
    data = requests.get(url).text

    c = Calendar(data)

    parsed_times = []

    for t in c.timeline.today(True):
        if len(parsed_times) < 1:
            parsed_times.append((t.begin.time(), t.end.time()))
            continue

        last_time = parsed_times.pop()
        diff = abs(last_time[1].hour - t.begin.time().hour)

        if diff < 1:
            # fusion
            last_time = (last_time[0], t.end.time())
            parsed_times.append(last_time)
        else:
            parsed_times.append(last_time)
            parsed_times.append((t.begin.time(), t.end.time()))

    result  = []
    for t in parsed_times:
        result.append((str(t[0]), str(t[1])))

    print(result)