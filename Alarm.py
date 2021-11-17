class Alarm:
    name = None
    alarm_type = None
    limit = None
    state = 'Passive'
    message = None
    light_intensity = 1
    previous_limit = None
    signal = False
    value = None
    def __init__(self, name, alarm_type, limit):
        """
        :param name: Name of the alarm
        :param alarm_type: Either 'High' or 'Low'
        :param limit: The limit to cross before setting off the alarm
        """

        self.name = name
        self.alarm_type = alarm_type
        self.limit = limit
        self.state = 'Passive'

    def check_value(self, value):
        """
        Checks if the value crosses the limit
        :param value: The process measurement to be checked
        :return:
        """

        self.value = value
        if self.state == 'Passive':
            if self.alarm_type == 'High':
                if value > self.limit:
                    self.state = 'Active'
                    self.message = 'High Alarm'


            elif self.alarm_type == 'Low':
                if value < self.limit:
                    self.state = 'Active'
                    self.message = 'Low Alarm'

            if self.state == 'Active':
                print(self.name, ' ', self.message, ' :', self.value)


        self.lighting()

    def acknowledge(self, signal):

        if self.state == 'Active' and signal:
            self.signal = True
            self.state = 'Acknowledged'
            print(self.state)


        if self.state == 'Acknowledged':
            if self.value < self.limit and self.alarm_type == 'High':
                self.state = 'Passive'
                print(self.state)
            elif self.value > self.limit and self.alarm_type == 'Low':
                self.state = 'Passive'
                print(self.state)

        self.lighting()

    def lighting(self):
        if self.state == 'Passive':
            self.light_intensity = 0.1

        elif self.state == 'Acknowledged':
            self.light_intensity = 0.5

        elif self.state == 'Active':
            self.light_intensity = 1