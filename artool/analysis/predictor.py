"""
Predictor class

"""
from artool.error.custom import PredictorError


role_increment = {
    "F8": 0.05,
    "F9": 0.06,
    "F10": 0.07,
    "F11": 0.08,
    "F12": 0.09,
    "F13": 0.10
}

supported_type = [
    "salary",
    "kpi",
    "retrenchment",
    "on-bench",
    "promotion"
]


class Predictor:
    """Predictor class
    Used to run predictions on salary, kpi, retrenchment, on-bench, promotion
    """

    def __init__(self, p_type: str = "inflation", dept: str = "JDU-AS"):
        """initialize method
        """
        # set default to inflation predictor
        self.type = p_type
        self.department = dept

    def set_type(self, p_type: str):
        """type setter

        Args:
            p_type (str): predictor type
        """
        self.type = p_type
        self.validate_type()

    def predict_salary(self, current_salary: float, role_level: str):
        """predict salary in 2 years

        Args:
            current_salary (float): _description_
            role_level (str): _description_
        """
        self.validate_salary_input(current_salary, role_level)
        predicted_salary = (
            current_salary * role_increment[role_level]) + current_salary
        return predicted_salary

    def validate_salary_input(self, current_salary: float, role_level: str):
        """Function to validate the predict salary input 

        Raises:
            PredictorError: on invalid salary
        """
        if current_salary > 1000000:
            raise PredictorError("The current salary doesn't make sense!\
                            Fuj**** doesn't pay that much to their employees!")

        valid = False
        for role_level in role_increment:
            valid = True

        if not valid:
            raise PredictorError(f"Invalid role level {role_level}")

    def validate_type(self):
        """validate Predictor type

        Raises:
            PredictorError: on invalid type
        """
        if self.type not in supported_type:
            raise PredictorError(f"Invalid Predictor type {self.type}")
