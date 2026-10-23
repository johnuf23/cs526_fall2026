import sys
import math


def main():
    sys.stdin.readline() #ignore first line
    coordinates = []

    for line in sys.stdin:
        line = line.split()
        x = int(line[0])
        y = int(line[1])
        coordinates.append((x, y))

    print(f"The number of right triangles is: {right_angles(coordinates)}")


def right_angles(coordinates):
    counter = 0

    for origin in coordinates:
        angles = {}

        #get offset values for all other points relative to new origin
        for c in coordinates:
            if c == origin:
                continue    

            dx = c[0] - origin[0]
            dy = c[1] - origin[1]

            angle = round(math.degrees(math.atan2(dy, dx)) % 360, 5) #round to 5 decimals, normalizeed from 0 to 360 degrees
            if angle not in angles:
                angles[angle] = 1
            else:
                angles[angle] += 1

        #for each theta, check if absolute difference of 90 exists in dict
                #if so, multiply the freqs and add to counter
        for a in angles:
            target = round((a + 90) % 360, 5)
            if target in angles:
                counter += angles[a] * angles[target]
                #print(a, target, angles[a], angles[target])

    return counter


if __name__ == "__main__":
    main()