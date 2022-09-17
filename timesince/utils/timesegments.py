from timesince.utils.timeunit import TimeUnit

class TimeSegments:
    def __init__(self, total_seconds, units_locale, value_converter=None):
        self.years = TimeUnit(int(total_seconds // 31536000), "year", units_locale, value_converter)
        self.months = TimeUnit(int((total_seconds % 31536000) // 2592000), "month", units_locale, value_converter)
        self.weeks = TimeUnit(int((total_seconds % 2592000) // 604800), "week", units_locale, value_converter)
        self.days = TimeUnit(int((total_seconds % 604800) // 86400), "day", units_locale, value_converter)
        self.hours = TimeUnit(int((total_seconds % 86400) // 3600), "hour", units_locale, value_converter)
        self.minutes = TimeUnit(int((total_seconds % 3600) // 60), "minute", units_locale, value_converter)
        self.seconds = TimeUnit(int(total_seconds % 60), "second", units_locale, value_converter)
