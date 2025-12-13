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
    println!("Part 2: {:?}", part2(&lines));
}

fn part1(lines: &Vec<&str>) -> Option<String> {
    let mut invalid_numbers: Vec<i64> = Vec::new();
    for line in lines {
        let ranges: Vec<&str> = line.split(',').collect();
        for range in ranges {
            let bounds: Vec<&str> = range.split('-').collect();
            if bounds.len() != 2 {
                continue;
            }
            let start: i64 = bounds[0].parse().unwrap();
            let end: i64 = bounds[1].parse().unwrap();
            for num in start..=end {
                let num_str = num.to_string();
                let len = num_str.len();
                if len % 2 == 0 {
                    let half = len / 2;
                    if &num_str[0..half] == &num_str[half..len] {
                        log::debug!("Found repeating sequence: {}", num);
                        invalid_numbers.push(num);
                    }
                }
            }
        }
    }
    let sum: i64 = invalid_numbers.iter().sum();
    sum.to_string().into()
}

fn part2(_lines: &Vec<&str>) -> Option<String> {
    None
}
