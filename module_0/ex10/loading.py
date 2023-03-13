import time

def ft_progress(lst):
    start_time = time.time()
    lst_len = len(lst)
    for x in lst:
        elapsed= time.time() - start_time
        print("\x1b[0K", end='')
        print(f"ETA: {(elapsed * lst_len / (x + 1) if (x + 1) != 0 else 1) - elapsed:.2f}s "
              f"[{(x + 1) * 100 // lst_len if lst_len != 0 else 1:3d}%]"
              f"[{((x + 1) * 20 // lst_len if lst_len != 0 else 1) * '=' + '>':21}] "
              f"{x + 1}/{lst_len} "
              f"| elapsed_time {elapsed:.2f}s", end='\r')
        yield x
