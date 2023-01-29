n = int(input())

hashmap = {"tetrahedron": 4, "cube": 6, "octahedron": 8,
           "dodecahedron": 12, "icosahedron": 20}
faces = 0

for i in range(n):
    faces += hashmap[input().lower()]
print(faces)
