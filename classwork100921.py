# возвращает обратную строку
def reverse(s): 
    return s[::-1] 
def is_palindrome(s): 
    rev = reverse(s) 
    # проверка на совпадение 2х строк
    if (s == rev): 
        return True
    return False


