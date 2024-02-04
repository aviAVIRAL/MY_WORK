# remove dublicates 

# i/p =  "aviaviXYZ"

# o/p = 'aviXYZ'


def f(s):

    str = ""  # impo  No space between " "

    freq = [0] * 200

    for x in s : 
        freq[ord(x)] += 1

        if freq[ord(x)] == 1 and  x != " " :
            str += x

    return str 

if __name__=="__main__":

    s = "aviaviXYZZZZ"
    print(f(s))


