from datetime import date, timedelta

class DateRangeIterable:
    """Iterable object that have built-in iterator method """

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration

        today = self._present_day
        self._present_day += timedelta(days=1)
        return today

if __name__ == "__main__":

    DRI_obj = DateRangeIterable(date(2019, 1, 1), date(2019, 1, 5))
    for day in DRI_obj:
        print(day) 

    # When 'for loop' starts with DateRangeIterable
    # First, call iter() in DateRangeIterable.
    # then, iter() will call __iter__().
    # __iter__ return self -> object itself is iterable.
    # In every step of for-loop, object will call next() -> __next__()
    # __next__ role is to decide how to make and return element.
    # If there is nothing to return, should let know StopIteration.
    # In summary, for-loop call next() until StopIteration raised.

    # However, there is one problem with above object.
    max(DRI_obj)

    # Only works first loop because StopIteration raised
    # It means that empty sequences

    

    


