
class Flight(object):
    def __init__(self, flight_company, flight_number, departure_from, terminal, ETA, updated_ETA, status):
        self.status = status
        self.updated_ETA = updated_ETA
        self.ETA = ETA
        self.terminal = terminal
        self.departure_from = departure_from
        self.flight_number = flight_number
        self.flight_company = flight_company

