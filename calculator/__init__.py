# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from .calculation import Calculation
from .calculations import Calculations
from .operations import add, subtract, multiply, divide
from decimal import Decimal
from typing import Callable
#from calculation import Calculation
#from .calculation import Calculation
#from .operations import add, subtract, multiply, divide
#from .calculations import Calculations  
#from .operations import add, subtract, multiply, divide  
#from decimal import Decimal  
#from typing import Callable  

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, subtract)
    
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, multiply)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, divide)
    