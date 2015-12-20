
require 'digest'

GRAPHICS = false

def main
#  input = File.read("input.txt").chomp
#  input = input.split("\n") if input.include?("\n")
#  data = process_input(input)
  data = "yzbqklnj"
  part1 = evalp1(data, GRAPHICS)
  puts("Part 1:", part1[0])
  puts("Part 2:", evalp2(data, part1[1], GRAPHICS))
end

def process_input(input)
  
end

def evalp1(data, graphics)
  i = 0
  until Digest::MD5.hexdigest(data + i.to_s).start_with?("00000") do i += 1 end
  return [i, nil]
end

def evalp2(data, part1, graphics)
  i = 0
  until Digest::MD5.hexdigest(data + i.to_s).start_with?("000000") do i += 1 end
  return i
end

main
