# return masked string
def maskify(cc):
    total_len=len(cc)
    if total_len < 4:
        return (cc)
    else:
        return (('#'*(total_len-4))+cc[-4:])
