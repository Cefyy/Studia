
fn xo(s: &str) -> bool {
    

    s.chars().fold(0,|counter,c| { match c {'x' | 'X' => counter+1, 'o' | 'O' => counter -1, _ => counter}}) == 0
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
        assert_eq!(xo("xo"), true);
    }
    #[test]
    fn test_even_numbers2()
    {
        assert_eq!(xo("Xo"),true);
    }
    #[test]
    fn test_even_numbers3()
    {
        assert_eq!(xo("xxxm"), false);
    }
    #[test]
    fn test_even_numbers4()
    {
        assert_eq!(xo("Oo"), false);
    }
    #[test]
    fn test_even_numbers5()
    {
        assert_eq!(xo("xxooooxxxo"), true);

    }
}