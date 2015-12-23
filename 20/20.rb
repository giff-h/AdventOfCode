
require 'prime'

GRAPHICS = false

def main
#  input = File.read("input.txt").chomp
#  input = input.split("\n") if input.include?("\n")
#  data = process_input(input)
  data = 36000000
  part1 = evalp1(data, GRAPHICS)
  puts("Part 1:", part1[0])
  puts("Part 2:", evalp2(data, part1[1], GRAPHICS))
end

def process_input(input)
  
end

def evalp1(data, graphics)
  n = 2
  until 10*divisorgen(n) >= data
    n += 1
  end
  return [n, nil]
end

def evalp2(data, part1, graphics)
  n = 2
  until 11*divisorgen(n, true) >= data
    n += 1
  end
  return n
end

def divisorgen(n, p2=false)
  # http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
  factors = Prime.prime_division(n)
  nfactors = factors.size
  f = Array.new(nfactors, 0)
  divisorsum = 0
  loop do
    divisor = nfactors.times.collect { |x| factors[x][0] ** f[x] }.reduce(:*)
    divisorsum += divisor if !p2 || n / divisor < 50
    i = 0
    loop do
      f[i] += 1
      break if f[i] <= factors[i][1]
      f[i] = 0
      i += 1
      return divisorsum if i >= nfactors
    end
  end
end

main
