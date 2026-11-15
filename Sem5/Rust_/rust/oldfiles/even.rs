
fn even_numbers(array: &Vec<i32>, number: usize) -> Vec<i32> {
    
    let mut res = array.into_iter().filter(|x: &&i32| {*x%2==0}).rev().take(number).copied().collect::<Vec<i32>>();
    res.reverse();
    res

    



}

    

fn main()
{
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_even_numbers()
    {
        assert_eq!(even_numbers(&vec!(1, 2, 3, 4, 5, 6, 7, 8, 9), 3), vec!(4, 6, 8));
    }
    #[test]
    fn test_even_numbers2()
    {
        assert_eq!(even_numbers(&vec!(6, -25, 3, 7, 5, 5, 7, -3, 23), 1), vec!(6));
    }
    #[test]
    fn test_even_numbers3()
    {
        assert_eq!(even_numbers(&vec!(-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26), 2), vec!(-8, 26))
    }
    #[test]
    fn test_even_numbers4()
    {
        assert_eq!(even_numbers(&vec!(1, 2, 3, 4, 5, 6, 7, 8, 9), 1), vec!(8));
    }
    #[test]
    fn test_even_numbers5()
    {
        assert_eq!(even_numbers(&vec!(2,4,6), 3), vec!(2, 4, 6));

    }
}