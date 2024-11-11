from typing import Literal


class Stepper(object):
    """
    A class to manage a step counter with basic operations such as advancing to the next step, 
    moving back to the previous step, and resetting the step counter.
    Attributes:
        STEP (int): The current step count.
        MAX_STEP (int): The maximum step count.
    Methods:
        next() -> None:
        reset() -> None:
        back() -> None:
        command(command: Literal['next', 'back', 'reset']) -> None:
    """

    STEP: int = 0
    MAX_STEP: int = 2

    @staticmethod
    def next() -> None:
        """
        Advances the stepper to the next step if it has not reached the maximum step.
        Increments the `STEP` attribute of the `Stepper` class by 1 if it is not equal to `MAX_STEP`.
        """
        if Stepper.STEP != Stepper.MAX_STEP:
            Stepper.STEP += 1

    @staticmethod
    def reset() -> None:
        """
        Resets the step counter to its initial value.
        This method sets the class attribute `STEP` of the `Stepper` class to 0.
        """
        Stepper.STEP = 0

    @staticmethod
    def back() -> None:
        """
        Moves the stepper back by one step if it is not already at the initial step.
        Decreases the current step count by one if the current step is greater than zero.
        """
        if Stepper.STEP != 0:
            Stepper.STEP -= 1

    @staticmethod
    def get_step() -> int:
        """
        Returns the current step count.
        Returns:
            int: The current step count.
        """
        return Stepper.STEP

    @staticmethod
    def command(command: Literal['next', 'back', 'reset']) -> None:
        """
        Executes a command to control the stepper.
        Args:
            command (Literal['next', 'back', 'reset']): The command to execute. 
                - 'next': Move the stepper to the next step.
                - 'back': Move the stepper to the previous step.
                - 'reset': Reset the stepper to the initial state.
        Raises:
            ValueError: If an invalid command is provided.
        """
        if command == 'next':
            Stepper.next()
        elif command == 'back':
            Stepper.back()
        elif command == 'reset':
            Stepper.reset()
        else:
            raise ValueError('Invalid command')
