def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(2):
    print('you may pass')
else:
    print("pay a fine")
