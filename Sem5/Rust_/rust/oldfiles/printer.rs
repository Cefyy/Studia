
fn printer_error(string: &str) -> String
{
    let mut bad=0;

    for c in string.chars()
    {
        if c > 'm'
        {
            bad+=1
        }
    };
    format!("{}/{}",bad,string.len())
}
fn main()
{
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_errors1()
    {
        assert_eq!(&printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"), "3/56");
    }
    #[test]
    fn test_errors2()
    {
        assert_eq!(&printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmm"), "0/53");

    }
    #[test]
    fn test_errors3()
    {
        assert_eq!(&printer_error("aa"), "0/2");

    }
    #[test]
    fn test_errors4()
    {
        assert_eq!(&printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"), "6/60");

    }
    #[test]
    fn test_errors5()
    {
        assert_eq!(&printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"), "11/65");

    }
}