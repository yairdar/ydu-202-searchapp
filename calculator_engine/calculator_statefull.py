from typing import Callable, List, Tuple
from unittest import result

def get_logger():
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging
    return logger
logger = get_logger()


class Calculator:
    def __init__(self, total=0) -> None:
        self.total: int = total
        
    def set_total(self, value: int):
        self.total = value
        return self

    def do_add(self, x: int) -> 'Calculator':
        self.total += x
        return self

    def do_multiply(self, x: int) -> 'Calculator':
        self.total *= x
        return self

    def get_total(self) -> int:
        return self.total
    
    def do_op_line(self, opt_line: str) -> List[int]:
         op_sign, operand = self.parse_opt_val(opt_line)
         total_prev: int = self.get_total()
         self.do_op_tup(op_sign=op_sign, operand=operand)
         total_new: int = self.get_total()
         return [total_prev, total_new]
    
    def do_op_tup(self, op_sign:str, operand: int):
        if not op_sign or op_sign == ' ':
            self.set_total(operand)
        elif op_sign == '+':
            self.do_add(operand)
        elif op_sign == '-':
            self.do_add(-operand)
        elif op_sign == '*':
            self.do_multiply(operand)
        else:
            _err_msg = f"unsupported operator sign op_sign: {op_sign}"
            raise  ValueError(_err_msg)
        return self
    
    def process_text_block(self, txt_block: str) -> List[List[int]]:
        lines = txt_block.strip().splitlines()
        results: List[List[int]] = [list(self.do_op_line(line)) for line in lines]
        return results

        
    @staticmethod
    def parse_opt_val(opt_line: str)-> Tuple[str, int]:
        """Parses input line

        Args:
            opt_line (str): line with operator

        Returns:
            Tuple[str, int]: parsted sign
        
        Examples:
            >>> parse_opt_val('+ 3')
            ('+', 3)
            >>> parse_opt_val('6')
            (' ', 6)
        """
        # input data validation
        if not opt_line:
            _err_msg = f"op_str is too short: {opt_line}"
            raise ValueError(_err_msg)
        
        # extract parts from line
        parts: List[str] = opt_line.strip().split()
        
        # extracted data validation
        if len(parts) > 2:
            _err_msg = f"op_str is too long: {opt_line}"
            raise  ValueError(_err_msg)
        # single element means no operaion only set. sample '3'
        elif len(parts) == 1:
            op_sign = ' '
            operand: int = int(parts[0])
        # two element means line have format sample'+ 3'
        elif len(parts) == 2:
            operand: int = int(parts[1])
            op_sign = parts[0]
        # just in case refuse to process other formats of input
        else:
            raise Exception("Unexcpected error")
        return op_sign, operand

def test_calc_direct_data():
    proc = Calculator(total=0)
    lines = [
        '+ 4',
        '- 5',
        '+ -6',
        '+ 9',
    ]
    expected_results = [
        [0, 4],
        [4, -1],
        [-1, -7],
        [-7, 2]
    ]
    actual_results: Tuple[int, int] = [list(proc.do_op_line(line)) for line in lines]
    assert actual_results == expected_results
    # name: type = list of size as lines where each item is tuple prev, next
    

def test_calc_embeded_data():
    inp_data = """
    0
    - 4
    * 2
    - -8
    """
    expected_results = [
        [0, 0],
        [0, -4],
        [-4, -8],
        [-8, 0],
    ]    
    proc = Calculator(total=0)
    actual_results = proc.process_text_block(inp_data)
    assert expected_results == actual_results
    

# --- Test Sute ---

def test_sute_minimal():
    logger.info("Start Tests")
    test_calc_direct_data()
    test_calc_embeded_data()
    logger.info("Finish Tests")
    
def evalute_test_list(list_of_tests_in_this_suite: List[Callable]):
    logger.info("Start Tests")
    import time
    for test_func in list_of_tests_in_this_suite:
        logger.info(f"init evalutate {test_func.__name__}")
        ts_start = time.time()
        test_func()
        ts_end = time.time()
        metrics = dict(
            duration=ts_end - ts_start
        )
        logger.info(f"over evalutate {test_func.__name__} with metrics {metrics}")
    logger.info("Finish Tests")
        
def run_medium_test_suite():
    list_of_tests_in_this_suite = [
        test_calc_direct_data,
        test_calc_embeded_data
    ]
    evalute_test_list(list_of_tests_in_this_suite)

# === Common Code ===


def main():
    import os
    is_debug = bool(os.getenv('DEBUG_CALC'))
    if is_debug:
        import ipdb
        ipdb.set_trace()
    test_sute_minimal()
    run_medium_test_suite()


if __name__ == '__main__':
    main()