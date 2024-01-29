from model.neuron import Neuron
from tests.utils.line import Line
from tests.utils.point import Point


def test_outputs_between_zero_and_one():
    neuron = Neuron()
    activation = neuron.calculate_activation(0.5)
    assert activation >= 0 and activation <= 1


def test_outputs_scale_with_input():
    neuron = Neuron()

    input_output_points = [
        Point(0.25, neuron.calculate_activation(0.25)),
        Point(0.5, neuron.calculate_activation(0.5)),
        Point(0.75, neuron.calculate_activation(0.75)),
    ]

    activation_line = Line(input_output_points[0], input_output_points[1])
    assert activation_line.is_point_on_line(input_output_points[2])
