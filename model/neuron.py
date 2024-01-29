import random


class Neuron:
    INITIAL_WEIGHT_MINIMUM = 0.0
    INITIAL_WEIGHT_MAXIMUM = 0.1

    def __init__(self):
        self._input_weight = random.uniform(self.INITIAL_WEIGHT_MINIMUM,
                                            self.INITIAL_WEIGHT_MAXIMUM)
        self._bias = 0.0

    def calculate_activation(self, input: float) -> float:
        return input * self._input_weight + self._bias
