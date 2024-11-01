class VeritasError(Exception):

    def __init__(self, message):
        super().__init__(f'VeritasError: {message}')
        self.message = message

class VeritasAssertionError(VeritasError):

    def __init__(self, left, right):
        super().__init__(f'Failed to validate assertion, the achived output {left} is not equal to {right}')
        self.left = left
        self.right = right
