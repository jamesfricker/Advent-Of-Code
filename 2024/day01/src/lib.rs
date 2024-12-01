use std::collections::HashMap;
use std::fs;
use std::path::Path;

pub fn read_values(file_path: &str) -> (Vec<i32>, Vec<i32>) {
    let input = fs::read_to_string(Path::new(file_path)).expect("Failed to read input file");

    let mut column1 = Vec::new();
    let mut column2 = Vec::new();

    for line in input.lines() {
        // Split each line into two parts
        let parts: Vec<i32> = line
            .split_whitespace()
            .filter_map(|num| num.parse::<i32>().ok())
            .collect();

        // Push the numbers into the respective arrays
        if parts.len() == 2 {
            column1.push(parts[0]);
            column2.push(parts[1]);
        } else {
            panic!("Each line must have exactly two numbers");
        }
    }

    return (column1, column2);
}

pub fn calculate_solution(file_path: &str) -> i32 {
    let (mut column1, mut column2) = read_values(file_path);

    column1.sort();
    column2.sort();

    let mut diffs = 0;

    for i in 0..column1.len() {
        diffs += (column1[i] - column2[i]).abs();
    }

    return diffs;
}

pub fn part_two(file_path: &str) -> i32 {
    let (column1, column2) = read_values(file_path);

    let mut occurrence2: HashMap<i32, usize> = HashMap::new();

    for &val in &column2 {
        *occurrence2.entry(val).or_insert(0) += 1;
    }

    let mut similarity: i32 = 0;

    // Compute similarity using occurrences
    for &val in &column1 {
        // Get count1 and count2, defaulting to 0 if the key doesn't exist
        let count2 = *occurrence2.get(&val).unwrap_or(&0);

        // Compute contribution for the current value
        let v = val * count2 as i32;
        similarity += v;
    }

    similarity
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_calculate_solution() {
        let test_file = "test1.txt";
        let result = calculate_solution(test_file);
        assert_eq!(result, 11, "Expected solution to be 11");
    }

    #[test]
    fn test_part_two() {
        let test_file = "test1.txt";
        let result = part_two(test_file);
        assert_eq!(result, 31, "Expected solution to be 11");
    }
}
