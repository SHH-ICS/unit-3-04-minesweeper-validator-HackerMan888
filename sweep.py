import numbers

# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invalid)
def validate( block_data ):
  isValid = 'Valid'
 
  # Check whether the centre block is a bomb, a number, or an invalid input
  # Skip bombs, send an error on invalid input, verify numbers
  
  # Grid is 3 x 3, so the centre block is [1][1]
  x = 1
  y = 1
  if not isinstance(grid[x][y], numbers.Number):
    print("Input is not a number")
    isValid = 'Invalid'
    return (isValid)
  
  # is the centre a bomb?
  if grid[x][y] == -1:
    centreIsBomb = True
  else:
    centreIsBomb = False

  # check if the other numbers are valid by looping over the grid array elements
  if centreIsBomb:
    expectedValue = 1
  else:
    expectedValue = 0

  for x in range(0, len(grid)):
    # loop over each array element of each array
    for y in range(0, len(grid[x])):
      if x == 1 and y == 1:
        continue

      if grid[x][y] != expectedValue and grid[x][y] != -1:
        print('Found ', grid[x][y], ' but expected ', expectedValue, ' at grid[', x, '][', y, ']')
        isValid = 'inValid'
        return(isValid)     
      else:
        if grid[x][y] == -1:
          print('Found another bomb!')
  return (isValid)


#grid = [
#  [1,1,1],
#  [1,-1,1],
#  [1,1,1]
#]

#grid = [
#  [1,1,1],
#  [1,-1,1],
#  [1,1,-1]
#]

#grid = [
#  [0,0,0],
#  [0,0,0],
#  [0,0,0]
#]

grid = [
  [0,0,1],
  [0,-1,0],
  [1,0,0]
]

isValid = (validate(grid))
print(isValid)
if isValid == 'Valid':
  print("The grid is Valid! Congratulations!")
else:
  print("The grid is Invalid! Try again!")
