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
    let mut point: i32 = 50;
    let mut count: i32 = 0;

    for line in lines {
        let value: i32 = line[1..].parse().unwrap();
        if line.starts_with("R") {
            point = (point + value) % 100;
            log::debug!("Moving right by {}: {}", value, point);
        } else if line.starts_with("L") {
            point = (point - value + 100) % 100;
            log::debug!("Moving left by {}: {}", value, point);
        }
        if point == 0 {
            count += 1;
            log::debug!("Landed on 0, count: {}", count);
        }   
    }
    count.to_string().into()
}

fn part2(lines: &Vec<&str>) -> Option<String> {
    let mut point: i32 = 50;
    let mut count: i32 = 0;

    for line in lines {
        let value: i32 = line[1..].parse().unwrap();
        if line.starts_with("R") {
            let crosses = crosses_zero(point, value, true);
            count += crosses;
            
            point = (point + value) % 100;
            log::debug!("Moving right by {}: {} (crosses: {})", value, point, crosses);
            
        } else if line.starts_with("L") {
            let crosses = crosses_zero(point, value, false);
            count += crosses;
            
            point = ((point - value) % 100 + 100) % 100;
            log::debug!("Moving left by {}: {} (crosses: {})", value, point, crosses);
        }
        if point == 0 {
            count += 1;
            log::debug!("Landed on 0, count: {}", count);
        }   
    }
    count.to_string().into()
}

fn crosses_zero(from: i32, rotation: i32, clockwise: bool) -> i32 {
    let mut crosses = 0;
    
    if rotation >= 100 {
        // Multiple full rotations - these always cross
        crosses += rotation / 100;
        let remainder = rotation % 100;
        
        // For the partial rotation, check if it crosses 0 but doesn't land on it
        let (would_cross, to) = if clockwise {
            (from + remainder >= 100, (from + remainder) % 100)
        } else {
            (from - remainder < 0, ((from - remainder) % 100 + 100) % 100)
        };
        
        if from != 0 && would_cross && to != 0 {
            crosses += 1;
        }
    } else {
        let (would_cross, to) = if clockwise {
            (from + rotation >= 100, (from + rotation) % 100)
        } else {
            (from - rotation < 0, ((from - rotation) % 100 + 100) % 100)
        };
        
        if from != 0 && would_cross && to != 0 {
            crosses += 1;
        }
    }
    
    crosses
}
