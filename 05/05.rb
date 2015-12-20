
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
  return [data.select { |word| p1rule1(word) && p1rule2(word) && p1rule3(word) }.size, nil]
end

def evalp2(data, part1, graphics)
  data.select { |word| p2rule1(word) && p2rule2(word) }.size
end

def p1rule1(word)
  return word =~ /([aoeui].*){3}/
end

def p1rule2(word)
  return (0...word.size).any? { |i| word[i] == word[i+1] }
end

def p1rule3(word)
  return %w{ab cd pq xy}.all? { |x| !word.include?(x) }
end

def p2rule1(word)
  return (0...(word.size-2)).any? { |i| word[i+2..-1].include?(word[i..i+1]) }
end

def p2rule2(word)
  return (0...(word.size-1)).any? { |i| word[i] == word[i+2] }
end

main
