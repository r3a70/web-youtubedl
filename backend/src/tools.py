
def human_bytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024

    if size == 0:
        return '0 B'

    if not size:
        return ""

    power = 2 ** 10
    n = 0
    dic_power = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + dic_power[n] + 'B'
