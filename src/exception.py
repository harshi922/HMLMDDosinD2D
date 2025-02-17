import sys
import logging

def error_message_details(error, error_detail:sys):
    _,_,exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    line_no = exec_tb.tb_lineno
    error_message = "Error occures in py script:[{0}] in line number:[{1}] with error message:[{2}]".format(file_name, line_no, str(error)) 
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
  
# if __name__=="main":

#     try:
#         a = 10/0 
#     except Exception as e:
#         logging.info("Division by zero error")
#         raise CustomException(e, sys)