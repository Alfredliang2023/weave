import numpy as np
import math

from sympy.codegen.ast import continue_

from .matrix_operations import fraction_matrix, fly_transform

def zigzag_twill(numerators, denominators, k_type, k_value, s_value):
    """
    锯齿形斜纹组织生成函数
    
    参数:
        numerator: 整数，分子
        denominator: 整数，分母
        k_type: 字符串，'Kj'或'Kw'，表示经向或纬向
        k_value: 整数，K的值
        s_value: 整数，飞数S的值
    
    返回:
        生成的锯齿形斜纹组织矩阵
    """
    # 检查飞数S是否满足条件：1 ≤ S ≤ K-2
    if not (1 <= s_value <= k_value - 2):
        raise ValueError(f"飞数S必须满足条件：1 ≤ S ≤ K-2，当前K={k_value}，S={s_value}")
    
    # 计算最大公约数
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # 计算最小公倍数
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    # 计算个数num
    total = sum(numerators) + sum(denominators)
    if total % s_value == 0:
        num = total // s_value
    else:
        num = lcm(total, s_value) // s_value

    # print(f"计算得到的num值: {num}")

    # 根据k_type选择不同的生成方式
    if k_type.lower() == 'kj':
        # 生成第1列
        first_column = fraction_matrix(numerators, denominators, 'J')
        # print("第1列:")
        # print(first_column)
        
        # 生成基准列
        base_column = fly_transform(first_column, s_value)

        # 初始化结果矩阵
        result_rows = first_column.shape[0]
        result_cols = 0  # 将在循环中计算总列数
        
        # 临时存储所有生成的列
        all_columns = []
        current_column = first_column.copy()
        all_columns.append(current_column)
        # print("\n添加第1列到结果中")
        
        # 计数器
        count = len(all_columns[0])
        #总列数
        count_all_columns = ((2*k_value-2)-s_value)*num
        
        # 生成所有列
        while count<count_all_columns:

            # 从当前列开始，使用fly_transform(n=1)
            for i in range(k_value - 1):
                current_column = fly_transform(current_column, 1)
                all_columns.append(current_column)
                # 计数器+1
                count=count+1

            # 继续使用fly_transform(n=-1)生成列，直到与基准列相同
            while not np.array_equal(current_column, base_column):
                current_column = fly_transform(current_column, -1)
                all_columns.append(current_column)
                # 计数器+1
                count = count + 1

            # 生成基准列
            base_column = fly_transform(current_column, s_value)

        # 创建结果矩阵，只保留count_all_columns列
        result_cols = count_all_columns
        result = np.zeros((result_rows, result_cols), dtype=int)

        # 填充结果矩阵（只使用count_all_columns列）
        for i, col in enumerate(all_columns[:count_all_columns]):
            result[:, i] = np.array(col).flatten()
        
        return result
    
    elif k_type.lower() == 'kw':
        # 生成第1行
        first_row = fraction_matrix(numerators, denominators, 'W')
        # print("第1行:")
        # print(first_row)
        
        # 生成基准行
        base_row = fly_transform(first_row, s_value)

        # 初始化结果矩阵
        result_cols = first_row.shape[1]
        result_rows = 0  # 将在循环中计算总行数
        
        # 临时存储所有生成的行
        all_rows = []
        current_row = first_row.copy()
        all_rows.append(current_row)
        # print("\n添加第1行到结果中")
        
        # 计数器
        count = len(all_rows[0])
        # 总行数
        count_all_rows = ((2*k_value-2)-s_value)*num
        
        # 生成所有行
        while count < count_all_rows:
            # 从当前行开始，使用fly_transform(n=1)
            for i in range(k_value - 1):
                current_row = fly_transform(current_row, 1)
                all_rows.append(current_row)
                # 计数器+1
                count = count + 1

            # 继续使用fly_transform(n=-1)生成行，直到与基准行相同
            while not np.array_equal(current_row, base_row):
                current_row = fly_transform(current_row, -1)
                all_rows.append(current_row)
                # 计数器+1
                count = count + 1

            # 生成基准行
            base_row = fly_transform(current_row, s_value)
        
        # 创建结果矩阵，只保留count_all_rows行
        result_rows = count_all_rows
        result = np.zeros((result_rows, result_cols), dtype=int)
        
        # 填充结果矩阵（只使用count_all_rows行，从下往上填充）
        rows_to_fill = all_rows[:count_all_rows]  # 只使用count_all_rows行
        for i, row in enumerate(reversed(rows_to_fill)):  # 反转行的顺序，从下往上填充
            result[i, :] = row.flatten()
        
        return result
    
    else:
        raise ValueError("k_type必须是'Kj'或'Kw'")

# 测试函数
if __name__ == "__main__":
    # 测试用例
    numerator = [2,1]
    denominator = [1,2]
    k_type = "Kj"
    k_value = 9
    s_value = 4
    
    try:
        result = zigzag_twill(numerator, denominator, k_type, k_value, s_value)
        print("生成的锯齿形斜纹组织矩阵:")
        print(result)
    except ValueError as e:
        print(f"错误: {e}")