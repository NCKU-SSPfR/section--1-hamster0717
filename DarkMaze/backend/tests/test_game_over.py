from judge_code import game_over

def test_game_over_0():
    """測試當 health = 0 時，game_over 應該返回 True"""
    assert game_over(0) is True

def test_game_over_666():
    """測試當 health = 666 時，game_over 應該返回 True"""
    assert game_over(666) is True

def test_game_over_positive():
    """測試當 health 為正數（非 666）時，game_over 應該返回 False"""
    assert game_over(100) is False

def test_game_over_negative():
    """測試當 health 為負數時，game_over 應該返回 False"""
    assert game_over(-5) is False
