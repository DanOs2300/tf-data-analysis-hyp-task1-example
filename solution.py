import pandas as pd
import numpy as np


chat_id = 630197911 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    result = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='smaller')
    return result[1] < 0.06
