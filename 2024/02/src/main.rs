use std::{env, fs};


fn main() {
    let args: Vec<String> = env::args().collect();
    let file_path: &String = &args[1];

    let contents: String = fs::read_to_string(file_path).unwrap();
    let lines: Vec<&str> = contents.lines().collect();

    let mut count: i32 = 0;

    for line in lines {
        println!("{line}");
        let levels:Vec<i32> = line.split_whitespace().map(|l: &str|l.parse().unwrap()).collect();
        if is_safe(&levels) {
            count += 1
        }
        
    }
    println!("Part 1: {count}");
    println!("Part 2: ");

}

fn is_safe<T>(vec: &[T]) -> bool 
where T: Ord + std::ops::Sub<Output = T> + Copy + PartialOrd + From<i32>,
{
    is_safe_increasing(vec) || is_safe_decreasing(vec) 
}

fn is_safe_increasing<T>(vec: &[T]) -> bool 
where T: Ord + std::ops::Sub<Output = T> + Copy + PartialOrd + From<i32>,
{
    vec.windows(2).all(|w: &[T]| {
        let diff = w[0]-w[1];
        diff >= T::from(1) && diff <= T::from(3)
    })
}

fn is_safe_decreasing<T>(vec: &[T]) -> bool 
where T: Ord + std::ops::Sub<Output = T> + Copy + PartialOrd + From<i32>,
{
    vec.windows(2).all(|w: &[T]| {
        let diff = w[1]-w[0];
        diff >= T::from(1) && diff <= T::from(3)
    })
}