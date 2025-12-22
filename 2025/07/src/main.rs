use std::{env, fs};

fn main() {
    let args: Vec<String> = env::args().collect();
    env_logger::init();
    if args.len() < 2 {
        eprintln!("Usage: {} <input_file>", args[0]);
        std::process::exit(1);
    }
    let file_path: &String = &args[1];

    let contents: String = fs::read_to_string(file_path).unwrap();
    let lines: Vec<&str> = contents.lines().collect();

    log::debug!("{:?}", lines);
    println!("Part 1: {}", part1(&lines).unwrap());
    println!("Part 2: {}", part2(&lines).unwrap());
}

use std::collections::{HashMap, HashSet};

fn part1(lines: &Vec<&str>) -> Option<String> {
    let grid: Vec<Vec<char>> = lines.iter().map(|line| line.chars().collect()).collect();
    let height = grid.len();
    let width = grid[0].len();

    let mut beams: HashSet<(usize, usize)> = HashSet::new();

    // Find start
    for r in 0..height {
        for c in 0..width {
            if grid[r][c] == 'S' {
                beams.insert((r, c));
            }
        }
    }

    let mut splits = 0;

    while !beams.is_empty() {
        let mut next_beams: HashSet<(usize, usize)> = HashSet::new();

        for &(r, c) in &beams {
            let nr = r + 1;
            if nr >= height {
                continue;
            }

            let cell = grid[nr][c];
            if cell == '^' {
                splits += 1;
                if c > 0 {
                    next_beams.insert((nr, c - 1));
                }
                if c + 1 < width {
                    next_beams.insert((nr, c + 1));
                }
            } else {
                next_beams.insert((nr, c));
            }
        }
        beams = next_beams;
    }

    Some(splits.to_string())
}

fn part2(lines: &Vec<&str>) -> Option<String> {
    let grid: Vec<Vec<char>> = lines.iter().map(|line| line.chars().collect()).collect();
    let height = grid.len();
    let width = grid[0].len();

    let mut beams: HashMap<(usize, usize), u128> = HashMap::new();

    // Find start
    for r in 0..height {
        for c in 0..width {
            if grid[r][c] == 'S' {
                beams.insert((r, c), 1);
            }
        }
    }

    let mut total_splits: u128 = 0;

    while !beams.is_empty() {
        let mut next_beams: HashMap<(usize, usize), u128> = HashMap::new();

        for (&(r, c), &count) in &beams {
            let nr = r + 1;
            if nr >= height {
                continue;
            }

            let cell = grid[nr][c];
            if cell == '^' {
                total_splits += count;
                if c > 0 {
                    *next_beams.entry((nr, c - 1)).or_insert(0) += count;
                }
                if c + 1 < width {
                    *next_beams.entry((nr, c + 1)).or_insert(0) += count;
                }
            } else {
                *next_beams.entry((nr, c)).or_insert(0) += count;
            }
        }
        beams = next_beams;
    }

    Some((total_splits + 1).to_string())
}
