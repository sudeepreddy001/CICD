from unittest import TestCase
import unittest
from unittest.mock import MagicMock


class InvalidInput(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.message = kwargs.get("message")
    
    def __str__(self):
        return self.message
    
class DivisionByZero(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.message = kwargs.get("message")
    
    def __str__(self):
        return self.message

class Calculator:
    
    @staticmethod
    def addition(var1, var2):
        return var1 + var2

    @staticmethod
    def subtraction(var1, var2):
        return var1 - var2
    
    @staticmethod
    def multiplication(var1, var2):
        return var1 * var2
    
    @staticmethod
    def division(var1, var2):
        
        if var2 == 0:
            raise DivisionByZero(message = 'Division with Zero')
        
        return var1/var2
    
    @staticmethod
    def perform_operation(operator, var1, var2):
        if var1 is None or var2 is None or type(var1) == str or type(var2) == str:
            raise InvalidInput(message = "please enter valid values")

        if operator == '+':
            return Calculator.addition(var1, var2)
        elif operator == '-':
            return Calculator.subtraction(var1, var2)
        elif operator == '*':
            return Calculator.multiplication(var1, var2)
        elif operator == '/':
            return Calculator.division(var1, var2)
        else:
            raise InvalidInput(message = "Dont support other calculations")

class CalculatorTest(TestCase):
    def setUp(self):
        pass

        """ 
        We are using mocking function to mock the response of the addition function in Calculator
        """
    def test_perform_operation1(self):
        Calculator.addition = MagicMock(return_value=6)
        self.assertEqual(Calculator.perform_operation('+', 3, 3), 6)
    
    def test_perform_operation2(self):
        Calculator.subtraction = MagicMock(return_value=6)
        self.assertEqual(Calculator.perform_operation('-', 9, 3), 6)
        
    def test_perform_operation3(self):
        self.assertEqual(Calculator.perform_operation('*', 9, 3), 27)
    
    def test_perform_operation4(self):
        with self.assertRaises(DivisionByZero):
            Calculator.perform_operation('/', 9, 0)
    
    def test_perform_operation5(self):
        self.assertEqual(Calculator.perform_operation('/', 9, 3), 3)
        
    def test_perform_operation6(self):
        with self.assertRaises(InvalidInput):
            Calculator.perform_operation('%', 9, 3)