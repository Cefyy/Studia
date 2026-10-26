
fn two_to_one(a1: &str, a2: &str) -> String  {
    let mut result: String = a1.to_owned();
    result.push_str(a2);

    let mut vec: Vec<char>= result.chars().collect();

    vec.sort();
    vec.dedup();
    vec.into_iter().collect()





}

    

fn main()
{
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_two_to_one()
    {
        assert_eq!(two_to_one("a", "bc"),"abc");
    }
    #[test]
    fn test_two_to_one2()
    {
        assert_eq!(two_to_one("aaaaa", "aaa"),"a");
    }
    #[test]
    fn test_two_to_one3()
    {
        assert_eq!(two_to_one("abc", "abc"),"abc");
    }
    #[test]
    fn test_two_to_one4()
    {
        assert_eq!(two_to_one("aretheyhere", "yestheyarehere"),"aehrsty");
    }
    #[test]
    fn test_two_to_one5()
    {
        assert_eq!(two_to_one("loopingisfunbutdangerous", "lessdangerousthancoding"),"abcdefghilnoprstu");

    }
}