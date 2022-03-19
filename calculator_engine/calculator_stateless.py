from typing import List, Tuple

class StateLessCalc:
    
    @staticmethod
    def add(el1, el2):
        return el1 + el2

    @staticmethod
    def sub(el1, el2):
        return el1 - el2

    @staticmethod
    def mul(el1, el2) -> int:
        return el + el2
    

class BulckCalc:

    @staticmethod
    def dispatch_exp(el1: int, op_sign: str, el2: int):
        if op_sign == '+':
            res = StateLessCalc.add(el1, el2)
        elif op_sign == '*':
            res = StateLessCalc.mul(el1, el2)
        elif op_sign == '-':
            res =  StateLessCalc.sub(el1, el2)
        return res

    @staticmethod
    def process_bulck(txt_block: str) -> List[int]:
        lines = txt_block.strip().splitlines()
        results = BulckCalc.process_lines_list(lines=lines)
        return results
    
    @staticmethod
    def process_lines_list(lines: List[str]) -> List[int]:
        results: List[int] = []
        for line in lines:
            el1, op_sign, el2 = BulckCalc.parse_opt_val(line)
            res = BulckCalc().dispatch_exp(el1, op_sign, el2)
            results.append(res)
        return results
        
    @staticmethod
    def parse_opt_val(opt_line: str)-> Tuple[int, str, int]:
        """Parses input line

        Args:
            opt_line (str): line with operator

        Returns:
            Tuple[str, int]: parsted sign
        
        Examples:
            >>> parse_opt_val('+ 3')
            (1, '+', 3)
            >>> parse_opt_val('6')
            (2, '-', 6)
        """
        # input data validation
        if not opt_line:
            _err_msg = f"op_str is too short: {opt_line}"
            raise ValueError(_err_msg)
        
        # extract parts from line
        parts: List[str] = opt_line.strip().split()
        
        # extracted data validation
        if len(parts) > 3:
            _err_msg = f"op_str is too long: {opt_line}"
            raise  ValueError(_err_msg)
        if len(parts) < 3:
            _err_msg = f"op_str is too short: {opt_line}"
            raise  ValueError(_err_msg)
        
        op_sign = parts[1]
        el1: int = int(parts[0])
        el2: int = int(parts[-1])

        return el1, op_sign, el2

def test_calc_direct_data():
    proc = BulckCalc()
    lines = [
        '1 + 4',
        '2 - 5',
        '3 + -6',
    ]
    expected_results = [
        5,
        -3,
        -3,
    ]
    actual_results: List[int] = proc.process_lines_list(lines)
    # actual_results: List[int] = proc.process_bulck(txt_block)
    assert actual_results == expected_results
    # name: type = list of size as lines where each item is tuple prev, next
    
# === Common Code ===


def main():
    import os
    is_debug = bool(os.getenv('DEBUG_CALC'))
    if is_debug:
        import ipdb
        ipdb.set_trace()
    test_calc_direct_data()
    # run_medium_test_suite()


if __name__ == '__main__':
    main()