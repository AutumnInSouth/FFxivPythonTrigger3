match 'sub', 2:
    case ('run', func_key) | ('sub', func_key):
        print(f"run {func_key}")
    case 'sub', event_key:
        print(f"subscribe {event_key}")
    case 'unsub', event_key:
        print(f"unsubscribe {event_key}")
    case other, _:
       print(f"invalid message type '{other}'")
