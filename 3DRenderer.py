import turtle as t

t.title("Turt")

screen = t.getscreen()
screen.screensize(300, 300)

t.speed("fastest")
t.width(1)

screen.bgcolor("#2F2F2F")
t.color("white")

camera = [0, -250, -50]  #L/R, F/B, U/D

coordinates_3D = [
  [100, 0, 100],  # A
  [-100, 0, 100],  # B
  [-100, 200, 100],  # C
  [100, 200, 100],  # D
  [100, 200, -100],  # E
  [100, 0, -100],  # F
  [-100, 0, -100],  # G
  [-100, 200, -100] # H
]


def getSystem(coordinates: list) -> list:
  a = camera[0]
  b = camera[1]
  c = camera[2]

  d = coordinates[0]
  e = coordinates[1]
  f = coordinates[2]

  try:
    t = -b / e
  except:
    return [d, f]

  x = a + (t * d)
  y = c + (t * f)

  return [x, y]


def connectedVerticies(coordinate: list) -> list:

  vertices = []

  for cord in coordinates_3D:
    similar = 0
    for i in range(3):
      if (cord[i] == coordinate[i]):
        similar += 1

    if similar == 2:
      vertices.append(cord)

  return vertices


def calculateBounds(coord_list: list) -> list:
  lower_x = 0
  upper_x = 0

  lower_y = 0
  upper_y = 0

  for coord in coord_list:
    if coord[0] < lower_x:
      lower_x = coord[0]
    elif coord[0] > upper_x:
      upper_x = coord[0]

    if coord[1] < lower_y:
      lower_y = coord[1]
    elif coord[1] > upper_y:
      upper_y = coord[1]

  return [[lower_x, upper_x], [lower_y, upper_y]]


def main():
  t.clear()

  render_coordinates = coordinates_3D
  unrendered_points = []

  coordinates_2D = [getSystem(coordinate) for coordinate in render_coordinates]

  x_bounds = calculateBounds(coordinates_2D)[0]
  y_bounds = calculateBounds(coordinates_2D)[1]

  print(x_bounds)
  print(y_bounds)

  for enum, coordinate in enumerate(coordinates_2D):
    x = coordinate[0]
    y = coordinate[1]
    if x > x_bounds[0] and x < x_bounds[1] and y > y_bounds[0] and y < y_bounds[1]:
      unrendered_points.append(coordinate)

  print(coordinates_2D)

  for point in unrendered_points:
    render_coordinates.pop(coordinates_2D.index(point))
    coordinates_2D.remove(point)

  print(coordinates_2D)

  t.penup()

  for coordinate in coordinates_2D:
    coordinate[0] += camera[0]
    coordinate[1] += camera[2]
    t.goto(coordinate)
    t.pendown()

    vertices = connectedVerticies(
      render_coordinates[coordinates_2D.index(coordinate)])

    for vert in vertices:
      vert_2D = getSystem(vert)
      vert_2D[0] += camera[0]
      vert_2D[1] += camera[2]
      t.goto(vert_2D)
      t.goto(coordinate)

  t.hideturtle()


if __name__ == "__main__":
  main()

console = "CONSOLE: "
help = "-HELP - Open help menu\n-X n - Move camera on x-axis by n\n-Y n - Move camera on y-axis by n\n-Z n - Move camera on the z-axis by n\n-QUIT - Quit the program"
while True:
  command = input(console)
  command = command.upper()

  if command == "-HELP":
    print(help)
  elif "-X" in command:
    camera[0] -= int(command[2:])
  elif "-Y" in command:
    camera[1] += int(command[2:])
  elif "-Z" in command:
    camera[2] += int(command[2:])
  elif command == "-QUIT":
    break

  main()
