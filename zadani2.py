def print_dict(d):
    for key in samolot:
        print("{0}:{1}".format(key,d[key]))
if __name__ == "__main__":
    samolot = {'name': 'boening',
    'przebieg':1000, 'type':'pasazerski'}
    print_dict(samolot)
