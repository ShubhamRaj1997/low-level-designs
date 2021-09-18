class ParkingChargeCalculator(object):
    def __init__(self):
        pass
    def calculate(self, time_in_hour):
        return self.tier1_cal() + self.tier2_cal(time_in_hour-5) + self.tier3_cal(time_in_hour-2)

    def tier1_cal(self):
        """
        for first hour
        :return:
        """
        return 5

    def tier2_cal(self, time_in_hour):
        """
        for next 5 hrs
        :param time_in_hour:
        :return:
        """
        return max(0, time_in_hour * 5)

    def tier3_cal(self, time_in_hour):
        return max(0, time_in_hour * 10)
