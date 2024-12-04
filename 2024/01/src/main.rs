use std::{env, fs};


fn main() {
    let args: Vec<String> = env::args().collect();
    let file_path: &String = &args[1];

    let contents: String = fs::read_to_string(file_path).expect("Should be able to read an input file");
    let lines: Vec<&str> = contents.lines().collect();

    let (mut list_a, mut list_b): (Vec<i32>,Vec<i32>) = (Vec::new(),Vec::new());

    for line in lines{
        let nums: Vec<&str> = line.split_whitespace().collect();
        let parsed: Vec<Option<i32>>= nums.iter().map(|s| s.parse().ok()).collect();
        if let [Some(a), Some(b)] = &parsed[..]{
            list_a.push(*a);
            list_b.push(*b);
        } else {
            println!("The vector does not contain exactly two valid integers.");
        }
    }
    list_a.sort();
    list_b.sort();

    let mut distances: Vec<u32> = Vec::new();
    for (a, b) in list_a.iter().zip(list_b.iter()) {
        distances.push(a.abs_diff(*b));
    }

    println!("Part 1: {}", distances.iter().sum::<u32>());

    let mut similarities: Vec<i32> = Vec::new();
    
    for a in list_a {
        let count: usize = list_b.iter().filter(|&&x| x == a).count();
        similarities.push(a * count as i32)
    }

    println!("Part 2: {}", similarities.iter().sum::<i32>())

}
