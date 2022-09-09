from enum import Enum


class UsersEnum(Enum):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    STANDARTUSER = 'standard_user', 'secret_sauce'
    LOCKEDOUTUSER = 'locked_out_user', 'secret_sauce'
    PROBLEM_USER = 'problem_user', 'secret_sauce'
    PERFORMANCE_GLITCH_USER = 'performance_glitch_user', 'secret_sauce'



