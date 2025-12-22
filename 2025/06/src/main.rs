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
    // the lines actually repreesent a 2D grid of numbers separated by spaces
    // the last line are arithmetic operators that should be applied to each column
    // add up the results of each column after applying the operator
    let mut result = 0;
    let num_cols = lines[0].split_whitespace().count();
    for col in 0..num_cols {
        let mut col_values: Vec<i64> = Vec::new();
        for row in 0..lines.len() - 1 {
            let value: i64 = lines[row]
                .split_whitespace()
                .nth(col)
                .unwrap()
                .parse()
                .unwrap();
            col_values.push(value);
        }
        let operator: &str = lines[lines.len() - 1].split_whitespace().nth(col).unwrap();
        let col_result = match operator {
            "+" => col_values.iter().sum(),
            "*" => col_values.iter().product(),
            _ => 0,
        };
        result += col_result;
    }
    result.to_string().into()
}

fn part2(lines: &Vec<&str>) -> Option<String> {
    let height = lines.len();
    if height < 2 {
        return Some("0".to_string());
    }
    let width = lines.iter().map(|l| l.len()).max().unwrap_or(0);

    let grid: Vec<Vec<char>> = lines.iter().map(|l| l.chars().collect()).collect();

    let mut total: i64 = 0;
    let mut current_numbers: Vec<i64> = Vec::new();
    let mut current_operator: Option<char> = None;

    for col in (0..width).rev() {
        let mut has_digit = false;
        let mut num_str = String::new();

        for row in 0..height - 1 {
            if col < grid[row].len() {
                let c = grid[row][col];
                if c.is_digit(10) {
                    has_digit = true;
                    num_str.push(c);
                }
            }
        }

        if has_digit {
            if let Ok(num) = num_str.parse::<i64>() {
                current_numbers.push(num);
            }

            if col < grid[height - 1].len() {
                let op_char = grid[height - 1][col];
                if op_char == '+' || op_char == '*' {
                    current_operator = Some(op_char);
                }
            }
        } else {
            if !current_numbers.is_empty() {
                let op = current_operator.unwrap_or('+');
                let val = match op {
                    '+' => current_numbers.iter().sum(),
                    '*' => current_numbers.iter().product(),
                    _ => 0,
                };
                total += val;

                current_numbers.clear();
                current_operator = None;
            }
        }
    }

    if !current_numbers.is_empty() {
        let op = current_operator.unwrap_or('+');
        let val = match op {
            '+' => current_numbers.iter().sum(),
            '*' => current_numbers.iter().product(),
            _ => 0,
        };
        total += val;
    }

    Some(total.to_string())
}
