use regex::Regex;
use std::fs;
use std::path::Path;

pub fn read_values(file_path: &str) -> String {
    let input = fs::read_to_string(Path::new(file_path)).expect("Failed to read input file");

    return input;
}

pub fn part_one(input_file: &str) -> i32 {
    let input = read_values(input_file);
    // println!("{}", input);

    let re = Regex::new(r"mul\((\-?\d+),\s*(\-?\d+)\)").unwrap();

    let mut total = 0;

    for cap in re.captures_iter(&input) {
        let x: i32 = cap[1].parse().unwrap();
        let y: i32 = cap[2].parse().unwrap();
        total += x * y;
    }

    return total;
}

pub fn part_two(input_file: &str) -> i32 {
    let input = read_values(input_file);
    // println!("{}", input);

    let re = Regex::new(r"(mul\((\-?\d+),\s*(\-?\d+)\))|(do\(\))|(don't\(\))").unwrap();

    let mut total = 0;

    let mut is_mul = true;

    for cap in re.captures_iter(&input) {
        if let Some(_) = cap.get(1) {
            // this is a mul group
            let x: i32 = cap[2].parse().unwrap();
            let y: i32 = cap[3].parse().unwrap();
            if is_mul {
                total += x * y;
            }
        } else if let Some(_) = cap.get(4) {
            // do group
            is_mul = true;
        } else if let Some(_) = cap.get(5) {
            is_mul = false;
        }
    }

    total
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let test_file = "test.txt";
        let result = part_one(test_file);
        assert_eq!(result, 161, "Test Incorrect");
    }

    #[test]
    fn test_part_two() {
        let test_file = "test_2.txt";
        let result = part_two(test_file);
        assert_eq!(result, 48, "Test Incorrect");
    }
}
