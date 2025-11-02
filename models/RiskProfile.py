class RiskProfile:
    def __init__(self,
                 age: int,
                 profession: str,
                 marital_status: str,
                 decision_style: int,
                 information_style: int,
                 time_preference: str):
        """
        Initializes an instance of the class
        :param age: The age of the test person
        :param profession: The profession of the test person
        :param marital_status: The marital status of the test person
        :param decision_style: The decision style of the test person
        :param information_style: The information style of the test person
        :param time_preference: The time preference of the test person
        """
        self.age = age
        self.profession = profession
        self.marital_status = marital_status
        self.decision_style = decision_style
        self.information_style = information_style
        self.time_preference = time_preference