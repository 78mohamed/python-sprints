def mutate_string(x):
    word , id , c = x.split('\n')[0] , int(x.split('\n')[1].split()[0]) , x.split('\n')[1].split()[1]
    return word[:id] + c + word[id + 1:]
    
if __name__ == '__main__':
    
    inp = '''abracadabra
    5 k'''

    if mutate_string(inp)=='abrackdabra':
        print('it works')