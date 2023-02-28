import datetime


def calc_date_diff(date1: datetime.date, date2: datetime.date):
    return abs((date2 - date1).days)


date1_sample = datetime.date.today()
date2_sample = datetime.date(2024, 2, 25)
days_diff = calc_date_diff(date1_sample, date2_sample)
print(f"days diff for dates({date1_sample}, {date2_sample}) = {days_diff}")
