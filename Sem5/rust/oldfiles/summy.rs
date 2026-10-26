
fn summy(strng: &str) -> i32 {
    strng.split_whitespace().map(|c:&str| {c.parse::<i32>().unwrap()
    }).sum()

}

    

fn main()
{
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_summy()
    {
        assert_eq!(summy("1 2 3"),6);
    }
    #[test]
    fn test_summy2()
    {
        assert_eq!(summy("0 0 0 "),0);
    }
    #[test]
    fn test_summy3()
    {
        assert_eq!(summy("  "),0);
    }
    #[test]
    fn test_summy4()
    {
        assert_eq!(summy("1 2 3"),6);
    }
    #[test]
    fn test_summy5()
    {
        assert_eq!(summy("5 4 "),9);

    }
}