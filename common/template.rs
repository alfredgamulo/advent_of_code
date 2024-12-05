use std::{env, fs};


fn main() {
    let args: Vec<String> = env::args().collect();
    let file_path: &String = &args[1];

    let contents: String = fs::read_to_string(file_path).unwrap();
    let lines: Vec<&str> = contents.lines().collect();

    for line in lines {
        println!("{line}");
    }
    println!("Part 1: ");
    println!("Part 2: ");

}
