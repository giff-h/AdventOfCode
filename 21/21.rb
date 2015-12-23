
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
  boss = input.map do |line|
    line = line.split(": ")
    [line[0][0...3].downcase, line[1].to_i]
  end
  boss = boss.to_h
  return [boss['hit'], boss['dam'], boss['arm']]
end

def evalp1(data, graphics)
  shop = {"Weapons" => [[8,   4, 0],
                        [10,  5, 0],
                        [25,  6, 0],
                        [40,  7, 0],
                        [74,  8, 0]],
          "Armor" =>   [[13,  0, 1],
                        [31,  0, 2],
                        [53,  0, 3],
                        [75,  0, 4],
                        [102, 0, 5],
                        [0,   0, 0]],
          "Rings" =>   [[25,  1, 0],
                        [50,  2, 0],
                        [100, 3, 0],
                        [20,  0, 1],
                        [40,  0, 2],
                        [80,  0, 3],
                        [0,   0, 0]]}
  hitpoints = 100
  combinations(shop).sort_by { |combo| combo[0] }.each do |combo|
    return [combo[0], shop] if battle(data, [hitpoints] + combo[1..-1])
  end
end

def evalp2(data, part1, graphics)
  hitpoints = 100
  combinations(part1).sort_by { |combo| combo[0] }.reverse_each do |combo|
    return combo[0] unless battle(data, [hitpoints] + combo[1..-1])
  end
end

def combinations(shop)
  combos = []
  shop["Weapons"].each do |weapon|
    shop["Armor"].each do |armor|
      shop["Rings"].each do |ring1|
        shop["Rings"].each do |ring2|
          next if ring2 != [0, 0, 0] && ring1 == ring2
          shop["Rings"].each do |ring3|
            next if ring3 != [0, 0, 0] && (ring1 == ring3 || ring2 == ring3)
            combos << [weapon, armor, ring1, ring2, ring3].transpose.map { |stat| stat.inject(:+) }
          end
        end
      end
    end
  end
  return combos
end

def battle(boss, player)
  bh, bd, ba = boss
  ph, pd, pa = player
  playerturn = true
  loop do
    if playerturn
      damage = pd-ba
      damage = 1 if damage < 1
      bh -= damage
      return true if bh <= 0
    else
      damage = bd-pa
      damage = 1 if damage < 1
      ph -= damage
      return false if ph <= 0
    end
    playerturn = !playerturn
  end
end

main
