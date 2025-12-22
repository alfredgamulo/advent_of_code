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
    // the lines represent a 2-dimensional grid of some sort
    // '.' represents open space
    // '@' represents an object
    // count the number of '@' characters with fewer than 4 adjacent '@' characters
    let mut count: usize = 0;
    let directions: Vec<(isize, isize)> = vec![
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ];
    let height: isize = lines.len() as isize;
    let width: isize = lines[0].len() as isize;
    for (y, line) in lines.iter().enumerate() {
        for (x, c) in line.chars().enumerate() {
            if c == '@' {
                let mut adjacent_count: usize = 0;
                for (dx, dy) in directions.iter() {
                    let nx: isize = x as isize + dx;
                    let ny: isize = y as isize + dy;
                    if nx >= 0 && nx < width && ny >= 0 && ny < height {
                        if lines[ny as usize].chars().nth(nx as usize).unwrap() == '@' {
                            adjacent_count += 1;
                        }
                    }
                }
                if adjacent_count < 4 {
                    count += 1;
                }
            }
        }
    }
    count.to_string().into()
}

fn part2(lines: &Vec<&str>) -> Option<String> {
    // the lines represent a 2-dimensional grid of some sort
    // '.' represents open space
    // '@' represents an object
    // count the number of '@' characters with fewer than 4 adjacent '@' characters
    // if the number of surrounding characters is less than 4, then remove the character from the 2-d array and start over, removing until no more can be removed
    // count how many '@' characters were removed

    let mut grid: Vec<Vec<char>> = lines.iter().map(|line| line.chars().collect()).collect();
    let directions: Vec<(isize, isize)> = vec![
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ];
    let height: isize = grid.len() as isize;
    let width: isize = grid[0].len() as isize;
    let mut removed_count: usize = 0;
    loop {
        let mut to_remove: Vec<(usize, usize)> = Vec::new();
        for y in 0..height {
            for x in 0..width {
                if grid[y as usize][x as usize] == '@' {
                    let mut adjacent_count: usize = 0;
                    for (dx, dy) in directions.iter() {
                        let nx: isize = x + dx;
                        let ny: isize = y + dy;
                        if nx >= 0 && nx < width && ny >= 0 && ny < height {
                            if grid[ny as usize][nx as usize] == '@' {
                                adjacent_count += 1;
                            }
                        }
                    }
                    if adjacent_count < 4 {
                        to_remove.push((x as usize, y as usize));
                    }
                }
            }
        }
        if to_remove.is_empty() {
            break;
        }
        for (x, y) in to_remove.iter() {
            grid[*y][*x] = '.';
            removed_count += 1;
        }
    }
    let remaining_lines: Vec<String> = grid.iter().map(|row| row.iter().collect()).collect();
    let remaining_str_lines: Vec<&str> = remaining_lines.iter().map(|s| s.as_str()).collect();
    log::debug!("{:?}", remaining_str_lines);
    removed_count.to_string().into()
}
