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
fn part_two(turns: &[LockTurn]) -> i32 {
    let dial_size: i64 = 100;
    let mut hits: i64 = 0;
    // positions are 0..=99, starting at 50 (same as part_one)
    let mut pos: i64 = 50;

    for turn in turns {
        let dist = turn.distance as i64;
        let d = match turn.direction {
            Direction::Left => -dist,
            Direction::Right => dist,
        };

        if d != 0 {
            // How far to go (in single steps) until we *first* hit 0,
            // in this direction, starting from `pos`.
            let (abs_step, offset) = if d > 0 {
                // moving right: pos + k ≡ 0 (mod 100)
                // smallest k > 0 is (100 - pos) % 100, but treat 0 as 100
                let abs_step = d;
                let mut offset = (dial_size - pos) % dial_size;
                if offset == 0 {
                    offset = dial_size;
                }
                (abs_step, offset)
            } else {
                // moving left: pos - k ≡ 0 (mod 100)
                // smallest k > 0 is pos % 100, but treat 0 as 100
                let abs_step = -d;
                let mut offset = pos % dial_size;
                if offset == 0 {
                    offset = dial_size;
                }
                (abs_step, offset)
            };

            if abs_step >= offset {
                // First hit at `offset`, then every 100 steps
                hits += 1 + (abs_step - offset) / dial_size;
            }
        }

        // Final position after the whole move (same semantics as part_one)
        pos = (pos + d).rem_euclid(dial_size);
    }

    hits as i32
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

    let e2_sol = part_two(&example_turns);
    let q2_sol = part_two(&q1_turns);

    println!("Part Two Example Solution: {}", e2_sol);
    assert!(e2_sol == 6);
    println!("Part Two Actual Solution: {}", q2_sol);
    assert!(q2_sol == 1086);

    Ok(())
}
