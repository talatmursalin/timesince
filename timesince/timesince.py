import json
from datetime import datetime
from timesince.utils.timesegments import TimeSegments


class TimeSince:
    def __init__(self, previous_time, current_time = datetime.now(), locale='en', value_converter=None):
        self.total_seconds = current_time.timestamp() - previous_time.timestamp()
        self.future = self.total_seconds < 0
        self.time_segmnets = TimeSegments(abs(self.total_seconds), value_converter)
        self.load_locale(locale)
    
    def load_locale(self, locale):
        try:
            with open(f"timesince/locale/{locale}.json") as f:
                self.load_locale = json.load(f)
        except FileNotFoundError:
            raise Exception(f"Locale {locale} not found")
    
    def all_repr(self):
        ret = f""
        if self.
        return f"{self.time_units.years} {self.load_locale['year'][1]}, {self.time_units.months} {self.load_locale['month'][1]}, {self.time_units.weeks} {self.load_locale['week'][1]}, {self.time_units.days} {self.load_locale['days'][1]}, {self.time_units.hours} {self.load_locale['hours']}, {self.time_units.minutes} {self.load_locale['minutes']}, {self.time_units.seconds} {self.load_locale['seconds']}"