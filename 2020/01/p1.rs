use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() -> io::Result<()> {
    let filename = "input.txt";

    let lines = read_lines(filename)?;

    // read lines
    let lines: Vec<String> = lines.map(|x| x.unwrap()).collect();

    // convert lines to numbers
    let numbers: Vec<i32> = lines.iter().map(|x| x.parse().unwrap()).collect();

    // sort numbers
    let mut sorted_numbers = numbers.clone();

    sorted_numbers.sort();

    // two pointers, find two numbers that sum to 2020
    let mut i = 0;
    let mut j = sorted_numbers.len() - 1;

    while i < j {
        let sum = sorted_numbers[i] + sorted_numbers[j];
        if sum == 2020 {
            println!("{} + {} = 2020", sorted_numbers[i], sorted_numbers[j]);
            println!("{} * {} = {}", sorted_numbers[i], sorted_numbers[j], sorted_numbers[i] * sorted_numbers[j]);
            break;
        } else if sum < 2020 {
            i += 1;
        } else {
            j -= 1;
        }
    }


    Ok(())
}
