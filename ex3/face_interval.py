def face_interval(list):
    interval = max(list) - min(list)
    for number in list:
        if number == interval:
            return ":)"
            continue
