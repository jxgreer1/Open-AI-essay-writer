import keyboard
def blocked():
    for i in range(1,150):
        keyboard.block_key(i)
    keyboard.block_key('esc')
    keyboard.unblock_key('esc')

def unblocked():
    for i in range(1,150):
        keyboard.unblock_key(i)