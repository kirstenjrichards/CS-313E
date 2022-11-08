def follows_rule(s, r):
    if len(r) == 0:
        return len(s) == 0
    if len(s) == 0:
        if len(r.replace('*', '')) == 0:
            return True
        return False
    
    if r[0] == '*':
        return follows_rule(s[1:], r[1:]) or follows_rule(s[1:], r) or follows_rule(s, r[1:])
    elif r[0] == '?':
        return follows_rule(s[1:], r[1:])
    else:
        return r[0] == s[0] and follows_rule(s[1:], r[1:])

def main():
    s = input()
    r = input()

    print(follows_rule(s,r))

if __name__ == '__main__':
    main()