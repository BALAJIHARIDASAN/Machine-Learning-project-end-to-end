import os
import sys

class HousingException(Exception):
    
    def __init__(self, error_message:Exception,error_detail:sys):
        super().__init__(error_message) # Inherite from the exception base class
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message,
                                                                       error_detail=error_detail
                                                                        ) # Inilizing the error messagge


    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:  #Output is string
        """
        error_message: Exception object
        error_detail: object of sys module
        """
        _,_ ,exec_tb = error_detail.exc_info()  # This will get the traceback of the error
        exception_block_line_number = exec_tb.tb_frame.f_lineno  # This will print the block line number
        try_block_line_number = exec_tb.tb_lineno   # This will give the line number of the error
        file_name = exec_tb.tb_frame.f_code.co_filename # This will give the file name of the error
        error_message = f"""
        Error occured in script: 
        [ {file_name} ] at 
        try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] 
        error message: [{error_message}]
        """     # The template for the error message
        return error_message 

    def __str__(self):
        return self.error_message


    def __repr__(self) -> str:
        return HousingException.__name__.str()