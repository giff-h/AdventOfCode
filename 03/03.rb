
GRAPHICS = false

def main
  input = File.read("input.txt").chomp
  input = input.split("\n") if input.include?("\n")
  data = process_input(input)
  part1 = evalp1(data, GRAPHICS)
  puts("Part 1:", part1[0])
  puts("Part 2:", evalp2(data, part1[1], GRAPHICS))
end

def process_input(input)
  return input
end

def evalp1(data, graphics)
  house = [0, 0]
  houses = [house]
  houses += data.each_char.collect { |d| house = step(house, d) }
  return [houses.uniq.size, nil]
end

def evalp2(data, part1, graphics)
  santahouse = [0, 0]
  robothouse = [0, 0]
  houses = [santahouse]
  data.each_char.each_with_index do |d, i|
    if i.even?
      houses << santahouse = step(santahouse, d)
    else
      houses << robothouse = step(robothouse, d)
    end
  end
  return houses.uniq.size
end

def step(house, direction)
  case direction
  when '>' then return [house[0]+1, house[1]]
  when '<' then return [house[0]-1, house[1]]
  when '^' then return [house[0], house[1]+1]
  when 'v' then return [house[0], house[1]-1]
  end
end

main
