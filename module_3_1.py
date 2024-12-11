calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    l = len(string)
    u = string.upper()
    lo = string.lower()
    return (l, u, lo)
def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    list_to_search = [s.upper() for s in list_to_search]
    if string in list_to_search:
        return True
    else:
        return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)