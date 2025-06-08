use std::{
    fmt::format,
    fs::File,
    io::{self, BufRead, BufReader},
    ops::Index,
    path::Path,
};

#[derive(Debug)]
struct PasswordPolicy {
    min_occ: usize,
    max_occ: usize,
    target: char,
    full_string: String,
}

fn read_file<P>(filename: P) -> io::Result<io::Lines<BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(BufReader::new(file).lines())
}

fn main() -> io::Result<()> {
    let test_a_solution = 2;
    match part_a("test_a.txt") {
        Ok(test_a_actual) => {
            assert!(
                test_a_actual == test_a_solution,
                "Expected solution {} for test_a, got {}",
                test_a_solution,
                test_a_actual
            );
            println!("Test passed: test_a returned {}", test_a_actual);
        }
        Err(e) => {
            eprintln!("Error: {}", e);
            std::process::exit(1); // Exit with error code on failure
        }
    }
    let sol_a = part_a("input.txt")?;
    println!("Part A Solution: {}", sol_a);
    let test_b_solution = 1;
    match part_b("test_a.txt") {
        Ok(test_b_actual) => {
            assert!(
                test_b_actual == test_b_solution,
                "Expected solution {} for test_a, got {}",
                test_b_solution,
                test_b_actual
            );
            println!("Test passed: test_b returned {}", test_b_actual);
        }
        Err(e) => {
            eprintln!("Error: {}", e);
            std::process::exit(1); // Exit with error code on failure
        }
    }
    let sol_b = part_b("input.txt")?;
    println!("Part B Solution: {}", sol_b);
    Ok(())
}

fn get_policies(file_name: &str) -> io::Result<Vec<PasswordPolicy>> {
    let lines = read_file(file_name)?;
    let mut policies = Vec::new();

    for line in lines {
        let line = line?; // Unwrap each line (handle potential read errors)
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() != 3 {
            return Err(io::Error::new(
                io::ErrorKind::InvalidData,
                format!("Invalid Line Format: {}", line),
            ));
        }

        // parse the min-max range
        let range: Vec<&str> = parts[0].split("-").collect();
        if range.len() != 2 {
            return Err(io::Error::new(
                io::ErrorKind::InvalidData,
                format!("Invalid Range Format: {}", parts[0]),
            ));
        }

        let min_occ: usize = range[0]
            .parse()
            .map_err(|e| io::Error::new(io::ErrorKind::InvalidData, e))?;
        let max_occ: usize = range[1]
            .parse()
            .map_err(|e| io::Error::new(io::ErrorKind::InvalidData, e))?;

        // parse the target char
        let target = parts[1]
            .trim_end_matches(":")
            .chars()
            .next()
            .ok_or_else(|| io::Error::new(io::ErrorKind::InvalidData, "No target character"))?;

        let full_string = parts[2].to_string();

        policies.push(PasswordPolicy {
            min_occ,
            max_occ,
            target,
            full_string,
        });
    }

    Ok(policies)
}

fn count_chars(x: char, y: &str) -> usize {
    y.chars().filter(|&c| c == x).count()
}

fn part_a(file_name: &str) -> io::Result<u16> {
    let policies = get_policies(file_name)?;
    let mut count = 0;
    for p in policies {
        let seen = count_chars(p.target, &p.full_string);
        if p.min_occ <= seen && seen <= p.max_occ {
            count += 1
        }
    }
    return Ok(count);
}

fn part_b(file_name: &str) -> io::Result<u16> {
    let policies = get_policies(file_name)?;
    let mut count = 0;
    for p in policies {
        let index_at_max = p.full_string.chars().nth(p.max_occ - 1) == Some(p.target);
        let index_at_min = p.full_string.chars().nth(p.min_occ - 1) == Some(p.target);

        if (index_at_max && !index_at_min) || (!index_at_max && index_at_min) {
            println!(
                "Found {} as valid with max {}, min {}, target {}",
                p.full_string, p.max_occ, p.min_occ, p.target
            );
            count += 1
        }
    }
    return Ok(count);
}
