import json

def extract(string):
    l = []
    l[:0] = string
    l = l[4:-9]
    string = "".join(l)
    return string

def main():
    with open("airlines.csv") as f:
        headers = f.readline()
        airport_names = {}

        while True:
            line = f.readline()

            if not line:
                break
            
            city = extract(line)
            if city not in list(airport_names.keys()):
                airport_names.update({city:1})
            else:
                airport_names[city] += 1
    
    print(json.dumps(airport_names))
    
    most = max (airport_names, key=airport_names.get)
    least = min (airport_names, key=airport_names.get)
    
    print("{} : {}".format(most, airport_names[most]))
    print("{} : {}".format(least, airport_names[least]))


if __name__ == "__main__":
    main()
