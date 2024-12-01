use day01::{calculate_solution, part_two};

fn main() {
    let result = calculate_solution("input.txt");
    println!("The solution is: {}", result);

    let p2 = part_two("input.txt");
    println!("Part 2 solution is {}", p2);
}
