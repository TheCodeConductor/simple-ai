from model.neuron import Neuron


def test_outputs_between_zero_and_one():
    neuron = Neuron()
    activation = neuron.calculate_activation(0.5)
    assert activation >= 0 and activation <= 1
