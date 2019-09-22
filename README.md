# Digit-Index 
<a href="https://pypi.org/project/digit-index/"><img alt="" src="https://img.shields.io/badge/pypi-1.0-blue.svg"></a>

This package contains an effective algorithm for finding what
digit is placed on certain 0-based index in string
of numbers from zero to infinity or from one to infinity

# Install
    pip install digit-index
   
# Usage

    import digit_index
    
    digit = digit_index.get_digit_zero_based(0) # get digit on index in string of numbers from zero to infinity 
    print(digit) # 0
    
    digit = digit_index.get_digit_one_based(0) # get digit on index in string of numbers from one to infinity
    print(digit) # 1
    
# License

MIT
