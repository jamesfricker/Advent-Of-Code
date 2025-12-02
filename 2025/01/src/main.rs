use std::fs::File;
use std::io::{self, BufRead, ErrorKind};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

#[derive(Debug)]

enum Direction {
    Left,
    Right,
}

#[derive(Debug)]
struct LockTurn {
    direction: Direction, // first charater in line
    distance: u32,        // rest of charaters in line
}

fn read_contents<P: AsRef<Path>>(file_name: P) -> io::Result<Vec<LockTurn>> {
    let lines = read_lines(file_name)?;

    let mut turns: Vec<LockTurn> = Vec::new();

    for line in lines {
        let line = line?; // own the String
        let line = line.trim(); // &str that borrows from the owned string
        if line.is_empty() {
            continue;
        }

        let mut chars = line.chars();
        let dir = match chars.next().unwrap() {
            'L' => Direction::Left,
            'R' => Direction::Right,
            other => {
                return Err(io::Error::new(
                    ErrorKind::InvalidData,
                    format!("bad dir {other}"),
                ));
            }
        };
        let distance: u32 = chars
            .as_str()
            .parse::<u32>()
            .map_err(|e| io::Error::new(ErrorKind::InvalidData, e))?;

        turns.push(LockTurn {
            direction: dir,
            distance,
        });
    }
    Ok(turns)
}

fn part_one(turns: &[LockTurn]) -> u32 {
    let dial_size = 100;
    let mut hits = 0;
    // starts at 50
    let mut pos = 50;
    // the number of times the dial is left pointing at 0 after any rotation in the sequence.
    for turn in turns {
        pos = match turn.direction {
            Direction::Left => (pos + dial_size - (turn.distance % dial_size)) % dial_size,
            Direction::Right => (pos + turn.distance) % dial_size,
        };
        if pos == 0 {
            hits += 1;
        }
    }
    hits
}

fn main() -> io::Result<()> {
    let example_turns = read_contents("example.txt")?;
    let q1_turns = read_contents("input.txt")?;
    println!("Turns: {:?}", example_turns);
    let e1_sol = part_one(&example_turns);
    let q1_sol = part_one(&q1_turns);

    println!("Part One Example Solution: {}", e1_sol);
    assert!(e1_sol == 3);
    println!("Part One Actual Solution: {}", q1_sol);
    assert!(q1_sol == 1086);

    Ok(())
}
