from datetime import date, timedelta

class DateRangeContainerIterable:

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
    
    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)

if __name__ == "__main__":

    DRCI_obj = DateRangeContainerIterable(date(2019, 1, 1), date(2019, 1, 5))

    for day in DRCI_obj:
        print(day)

    print()
    print("max_date: ", max(DRCI_obj))

    # difference with former script's object is..
    # first call iter() -> __iter__() -> make generator inside __iter__()
    # These shape's object call "Container Iterable" 
