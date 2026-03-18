"""
测试各组织生成器的基本功能
"""

from weave_generator import generate_weave


def test_twill():
    """测试斜纹生成"""
    matrix = generate_weave('斜纹', numerator=[3], denominator=[5], direction='右')
    assert matrix is not None
    assert len(matrix) > 0
    print("✓ 斜纹测试通过")


def test_satin():
    """测试缎纹生成"""
    matrix = generate_weave('缎纹', size=8, fly=3, direction='经面')
    assert matrix is not None
    assert len(matrix) == 8
    print("✓ 缎纹测试通过")


def test_diamond():
    """测试菱形斜纹生成"""
    matrix = generate_weave('菱形斜纹', numerator=[3], denominator=[5], kj=4, kw=4)
    assert matrix is not None
    assert len(matrix) > 0
    print("✓ 菱形斜纹测试通过")


if __name__ == '__main__':
    test_twill()
    test_satin()
    test_diamond()
    print("\n所有测试通过！")
