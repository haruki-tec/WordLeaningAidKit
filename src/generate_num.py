import random

def randomize_array(target_array):
    random.shuffle(target_array)
    
    return target_array


def gen_nums(start,stop,gen_num):
    if(start < 0 or stop < 0 or gen_num < 0):
        return unexpected_arguments_error()
    
    consecutive_nums = list(range(start,stop+1))
    discrete_nums = randomize_array(consecutive_nums)
    
    return discrete_nums[0:gen_num]

def gen_nums_with_char(start,stop,gen_num):
    nums = gen_nums(start,stop,gen_num)
    
    if nums == -1:
        return ["-1"]
    
    return [str(num) for num in nums]


def gen_aligned_nums(start,stop,gen_num):
    messy_nums = gen_nums(start,stop,gen_num)
    
    if messy_nums == -1:
        return -1
    messy_nums.sort()
    
    aligned_nums = messy_nums
    
    return aligned_nums

def gen_aligned_nums_with_char(start,stop,gen_num):
    nums = gen_aligned_nums(start,stop,gen_num)
    
    if nums == -1:
        return ["-1"]
    
    return [str(num) for num in nums]
         


def unexpected_arguments_error():
    print("入力を見直してください")
    return -1
        

