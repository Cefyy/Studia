
fn multiples(num: i32) -> i32 {
    
    (1..num).filter(|a| { a%3==0 || a%5==0}).sum()
}

    

fn main()
{
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_multiply()
    {
        assert_eq!(multiples(10500),25719750);
    }
    #[test]
    fn test_multiply2()
    {
        assert_eq!(multiples(6),8);
    }
    #[test]
    fn test_multiply3()
    {
        assert_eq!(multiples(33),225);
    }
    #[test]
    fn test_multiply4()
    {
        assert_eq!(multiples(10),23);
    }
    #[test]
    fn test_multiply5()
    {
        assert_eq!(multiples(11),33);

    }
}