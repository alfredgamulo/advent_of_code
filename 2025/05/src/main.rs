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

fn part1(lines: &Vec<&str>) -> Option<String> {
    // lines is a actually two separate lists separated by a blank line
    // the first set is a list of ranges
    // the second set are individual numbers
    // for each number in the second set, determine if it falls within any of the ranges
    // no need to determine if it falls within multiple ranges, just if it falls within any range
    // count how many numbers fall within any of the ranges
    let mut ranges: Vec<(i64, i64)> = Vec::new();
    let mut numbers: Vec<i64> = Vec::new();
    let mut in_ranges: bool = true;
    for line in lines {
        if line.trim().is_empty() {
            in_ranges = false;
            continue;
        }
        if in_ranges {
            let parts: Vec<&str> = line.split('-').collect();
            if parts.len() == 2 {
                let start: i64 = parts[0].trim().parse().unwrap();
                let end: i64 = parts[1].trim().parse().unwrap();
                ranges.push((start, end));
            }
        } else {
            let number: i64 = line.trim().parse().unwrap();
            numbers.push(number);
        }
    }
    let mut count: usize = 0;
    for number in numbers {
        for (start, end) in &ranges {
            if number >= *start && number <= *end {
                count += 1;
                break;
            }
        }
    }
    count.to_string().into()
}

fn part2(lines: &Vec<&str>) -> Option<String> {
    // lines is a actually two separate lists separated by a blank line
    // the first set is a list of ranges
    // the second set are individual numbers. ignore this set for part 2
    // count how many numbers are in the first set of ranges inclusively
    let mut ranges: Vec<(i64, i64)> = Vec::new();
    for line in lines {
        if line.trim().is_empty() {
            break;
        }
        let parts: Vec<&str> = line.split('-').collect();
        if parts.len() == 2 {
            let start: i64 = parts[0].trim().parse().unwrap();
            let end: i64 = parts[1].trim().parse().unwrap();
            ranges.push((start, end));
        }
    }

    // Sort ranges by start position
    ranges.sort_by_key(|r| r.0);

    // Merge overlapping ranges
    let mut merged: Vec<(i64, i64)> = Vec::new();
    for (start, end) in ranges {
        if merged.is_empty() {
            merged.push((start, end));
        } else {
            let last_idx = merged.len() - 1;
            let (last_start, last_end) = merged[last_idx];
            // If current range overlaps or is adjacent to last range, merge them
            if start <= last_end + 1 {
                merged[last_idx] = (last_start, end.max(last_end));
            } else {
                merged.push((start, end));
            }
        }
    }

    // Calculate total count by summing up the size of each merged range
    let total: i64 = merged.iter().map(|(start, end)| end - start + 1).sum();
    total.to_string().into()
}
