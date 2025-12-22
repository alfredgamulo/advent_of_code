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
    let mut result: Vec<u32> = Vec::new();
    for line in lines {
        log::debug!("Processing line: {}", line);
        let digits: Vec<u32> = line.chars().filter_map(|c| c.to_digit(10)).collect();
        log::debug!("Digits: {:?}", digits);
        let mut greatest: u32 = 0;
        for i in 0..digits.len() {
            for j in i + 1..digits.len() {
                let num = digits[i] * 10 + digits[j];
                if num > greatest {
                    greatest = num;
                }
            }
        }
        log::debug!("Greatest two-digit number: {}", greatest);
        result.push(greatest);
    }
    Some(result.iter().sum::<u32>().to_string())
}

fn part2(lines: &Vec<&str>) -> Option<String> {
    lines.len().to_string().into()
}
