def get_flag():
    flag_with_extra = "cybercamp{1y1o1u1r_f1l1a1g_1h1e1r1e1}"  

    # The user needs to change the argument of rstrip() to correctly strip the extra characters which is 1
    print(flag_with_extra.replace('1',''))

if __name__ == "__main__":
    get_flag()

