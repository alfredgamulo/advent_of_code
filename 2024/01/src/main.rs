use std::{env, fs};


fn main() {
    let args: Vec<String> = env::args().collect();
    let file_path: &String = &args[1];

    let contents: String = fs::read_to_string(file_path).expect("Should be able to read an input file");
    let lines: Vec<&str> = contents.lines().collect();

    let mut left_values: Vec<i32> = Vec::new();
    let mut right_values: Vec<i32> = Vec::new();

    for line in lines{
        let nums: Vec<&str> = line.split_whitespace().collect();
        let parsed: Vec<Option<i32>>= nums.iter().map(|s| s.parse().ok()).collect();
        if let [Some(left), Some(right)] = &parsed[..]{
            left_values.push(*left);
            right_values.push(*right);
        } else {
            println!("The vector does not contain exactly two valid integers.");
        }
    }
    left_values.sort();
    right_values.sort();

    let mut distances: Vec<u32> = Vec::new();
    for (left, right) in left_values.iter().zip(right_values.iter()) {
        distances.push(left.abs_diff(*right));
    }

    println!("Part 1: {}", distances.iter().sum::<u32>());
        

}
