class Knas:
    def __init__(self, delay_time_in_days: int, percent: int) -> None:
        """
        Define a fruit object.

        :param delay_time_in_days: int.
        :param percent: int.
        """
        # define the default percent
        self._default_percent = 110

        self.delay_time_in_days = delay_time_in_days
        # replace the given percent by the default if the default is greater
        self.percent = self._default_percent if percent < self._default_percent else percent

    def __call__(self, details_knas: str, original_knas: int):
        # define general messages
        details_message = f"Knas details: {details_knas}"
        original_message = f"The original knas was: {original_knas}"
        passed_days_message = f"{self.delay_time_in_days} days have passed since the deadline time to pay. "

        # calculate the new kans and generate message
        new_knas = original_knas * self.percent / 100
        new_knas_message = f"The new knas to is now {new_knas}"

        # define deadline message
        default_deadline_in_days = 30
        new_deadline_message = f"You should pay this within {default_deadline_in_days} days. Thank you"

        # represent all messages, one after each other with line space
        messages = [details_message, original_message, passed_days_message, new_knas_message, new_deadline_message]
        print("\n".join(messages))
        print("-" * 50)
        print("-" * 50)


if __name__ == '__main__':
    one_month_delay_115 = Knas(30, 115)
    one_month_delay_125 = Knas(30, 125)
    two_months_delay_150 = Knas(60, 150)
    one_month_delay_115("Parking in an unauthorized area", 300)
    one_month_delay_125("Driving above the speed limit", 500)
    two_months_delay_150("Parking on red-white area", 400)
