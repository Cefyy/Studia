fn string_to_int(abc : &str) -> i32
 {
    let res : i32 = abc.parse().unwrap();
    res
}



fn main()
{
    let res = string_to_int("3256");
    println!("{}",res)

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_string_to_int1()
    {
        assert_eq!(string_to_int("3256"),3256);
    }
    #[test]
    fn test_string_to_int2()
    {
        assert_eq!(string_to_int("0"),0);

    }
    #[test]
    fn test_string_to_int3()
    {
        assert_eq!(string_to_int("19"),19);

    }
    #[test]
    fn test_string_to_int4()
    {
        assert_eq!(string_to_int("43254355"),43254355);

    }
    #[test]
    fn test_string_to_int5()
    {
        assert_eq!(string_to_int("-1"),-1);

    }
}