import sys
from pprint import pprint
from operator import itemgetter
import operator


def build_g(map):
    graph = {}

    cs = map.split(";")
    cs = [c.strip('\n').replace(" ", "") for c in cs if len(
    c.strip('\n').replace(" ", "")) != 0]

    for c_nbors in cs:
        c, nbors = c_nbors.split(":")
        nbors = nbors.replace("[", "").replace("]", "").replace("\n", "").split(",")
        nbors = [(nbor, '') for nbor in nbors if nbor != '']
        graph[(c, False)] = nbors

    return graph

def diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

def get_allowed_clrs(graph, c, clrs):
    not_allowed_clrs = [c[1] for c in graph[(c, False)] if c[1] is not '']
    allowed_clrs = diff(clrs, not_allowed_clrs)
    return allowed_clrs

def deg_h(graph):
    id_nbor_len = [(index, len(l[1])) for index, l in enumerate(graph.items()) if l[0][1] is False]
    max_nbor = max(id_nbor_len, key=itemgetter(1))[1]
    max_id_nbor_len = [t[0] for t in id_nbor_len if t[1] == max_nbor]
    cs = [list(graph)[index][0] for index in max_id_nbor_len]
    return cs

def mrv(graph, clrs):
    cs_wo_clr = [(c[0]) for c, clred in graph.items() if c[1] is False]
    allowed_clr_eachc = {}
    for c in cs_wo_clr:
        allowed_clr_eachc[c] = get_allowed_clrs(graph, c, clrs)

    min_ava_clr_len = min([len(allowed_clrs) for c, allowed_clrs in allowed_clr_eachc.items()])
    cs = [c for c, clrs in allowed_clr_eachc.items() if len(clrs) is min_ava_clr_len]
    return cs


def lcv(graph, clrs):
    c_clr = []
    clr_no = {}

    for nbors in graph.values():
        [c_clr.append(c) for c in nbors if c[1] is not '']

    all_used_clrs = list(dict.fromkeys(c_clr))

    if not all_used_clrs:
        return clrs

    for cc in all_used_clrs:
        if cc[1] not in clr_no:
            clr_no[cc[1]] = 1
        else:
            clr_no[cc[1]] += 1

    no_max = max(clr_no.items(), key=operator.itemgetter(1))[1]
    clrs = [key for (key, value) in clr_no.items() if value is no_max]

    return clrs


def clring(graph, c, clr):

    nbors = graph[(c, False)]
    del graph[(c, False)]
    graph[(c, True)] = nbors

    for nei_list in graph.values():

        for n in nei_list:
            if n[0] == c:
                l = list(n)
                l[1] = clr
                t = tuple(l)
                nei_list.remove(n)
                nei_list.append(t)

if __name__ == "__main__":

    map = """Tallahassee: [San Diego, Boston, Chicago];
            San Diego: [Tallahassee, Kentucky];
            Boston: [Denver, Tallahassee];
            Chicago: [Tallahassee];
            New York: [Kentucky];
            Kentucky: [San Diego, New York];
            Vancouver: [];
            Denver: [Boston, Oklahoma];
            Oklahoma: [Denver];"""

    clrs = ['VIOLET', 'INDIGO', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE','RED']

    graph = build_g(map)

    for _ in range(len(graph)):
        max_deg_c = deg_h(graph)
        cs_min_rem_clrs = mrv(graph, clrs)
        much_used_clrs = lcv(graph, clrs)

        sel_c = set(max_deg_c).intersection(set(cs_min_rem_clrs)).pop()

        clrs_of_sel_c = get_allowed_clrs(graph, sel_c, clrs)

        common_clr = set(much_used_clrs).intersection(set(clrs_of_sel_c))

        try:
            if common_clr:
                clr = common_clr.pop()
            else:
                clr = clrs_of_sel_c.pop()

            clring(graph, sel_c, clr)
        except IndexError:
            sys.exit("Error. Try putting more colors.")

    alone_cities = [graph[c].append("Is separated from the others. Can use any color.") for c, nbors in graph.items() if len(nbors) == 0]
    for city, neighbors in graph.items():
        print (city,"Neighboured by :", neighbors)