import pytest
import src.exercise

def test_exercise():
    input_values = ["Hello there!"]
    output = []

    def mock_input(s):
        output.append(s)
        return input_values[0]

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ['Write a message...', input_values[0]]
