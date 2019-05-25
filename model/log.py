class Log:
    date = None
    url = None
    status = None

    def __init__(self, date=None, url=None, status=None):
        self.date = date
        self.url = url
        self.status = status

    def __str__(self):
        return "date => %s url => %s status => %s." % (self.date, self.url, self.status)
