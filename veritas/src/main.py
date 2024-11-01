from .veritas_error.errors import VeritasAssertionError

class VeritasTest:
    def expect(self, expected_result):
        found_result = self.callback(*self.options)

        try:
            assert found_result == expected_result
        except AssertionError:
            return "err"
        
        return "suc"

    def __init__(self, callback, options, result):
        self.callback = callback
        self.options = options
        self.result = result

class Veritas:
    def __init__(self, basePercentage=100):
        self.success = 0
        self.failure = 0
        self.tests: list[VeritasTest] = []
        self.basePercentage = basePercentage

    def on(self, callback: callable, result, **kwargs) -> VeritasTest:
        # Use kwargs to extract parameters and assign them to a list
        options = [kwargs.get(param) for param in sorted(kwargs)]
        test = VeritasTest(callback, options, result)
        self.tests.append(test)
        return test
    
    def runAll(self, descriptive=False):
        if descriptive: 
            print(f"VERITAS: running {len(self.tests)} {'test' if len(self.tests) == 1 else 'tests'}")
        
        for test in self.tests:
            if descriptive:  
                print(f"\tRUNNING: {test.callback.__name__} with {test.options} | ", end=" ")
            result = test.expect(test.result)
            if result == "err":
                if descriptive:  
                    print("\033[91mFAILED\033[0m")
                self.failure += 1
            elif result == "suc":
                if descriptive:  
                    print("\033[92mSUCCESS\033[0m")
                self.success += 1
        
        # Calculate success percentage
        success_percentage = (self.success / len(self.tests)) * 100 if self.tests else 0
        if success_percentage >= self.basePercentage:
            success_message = f'\033[42m{success_percentage:.2f}% success\033[0m'
        else:
            success_message = f'\033[41m{success_percentage:.2f}% success\033[0m'

        if descriptive:
            print(f"VERITAS: tests complete: {success_message}")
        
        return success_percentage