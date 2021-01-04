#
# Your previous Plain Text content is preserved below:
#
# This is just a simple shared plaintext pad, with no execution capabilities.
#
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
#
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/settings
#
# Enjoy your interview!
#
#
# "Me,Amsterdam,Barcelona,London,Prague"
#
# "U1,Amsterdam,Barcelona,London,Prague,U2,Shanghai,Hong Kong,Moscow,Sydney,Melbourne,U3,London,Boston,Amsterdam,Madrid,U4,Barcelona,Prague,London,Sydney,Moscow"
#
# U1
# U4
# U3

def ranking(me, others):
    # Error conditions
    mearr = me.split(",")
    if me[0] != "Me" and len(mearr) <= 2: return []
    mcities = mearr[1:]

    otherarr = others.split(",")
    othercitiesbyname = {}
    i = 0
    name = ""
    while i < len(otherarr):
        if otherarr[i].startswith("U") and otherarr[i][1:].isnumeric():
            name = otherarr[i]
            if name not in othercitiesbyname:
                othercitiesbyname[name] = set()
        else:
            othercitiesbyname[name].add(otherarr[i])
        i += 1

    res = {}
    for other in othercitiesbyname:
        count = 0
        for city in othercitiesbyname[other]:
            if city in mcities:
                count +=1
        if count not in res:
            res[count] = set()
            res[count].add(other)
        else:
            res[count].add(other)
    resarr = []
    for x in sorted(res.keys(), reverse=True):
        if x > 0:
            resarr.append(res[x])
    return resarr

print(ranking("Me,Amsterdam,Barcelona,London,Prague, London, London,London, London", "U1,Amsterdam,Barcelona,Prague,UCity,Amsterdam,Barcelona,London,Prague,City1,City2, U2,Shanghai,Hong Kong,Moscow,Sydney,Melbourne,U3,London,Boston,Amsterdam,Madrid,Amsterdam, Amsterdam, Amsterdam, Amsterdam,U4,Barcelona,Prague,London,Sydney,Moscow"))
