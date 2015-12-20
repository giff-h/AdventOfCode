
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
  return input.collect { |line| line.split('x').collect { |i| i.to_i }.sort }
end

def evalp1(data, graphics)
  return [data.inject(0) { |sum, box| sum + wrapping(box) }, nil]
end

def evalp2(data, part1, graphics)
  return data.inject(0) { |sum, box| sum + 2*box[0] + 2*box[1] + box.inject(:*) }
end

def wrapping(box)
  h, l, w = box
  return 3*h*l + 2*h*w + 2*l*w # 3hl because adding another for slack
end

main
