



    
fn my_first_interpreter(code: &str) -> String {
    let mut res = String::new();

    code.chars().fold(0u8,|counter: u8,c| match c { '+' => counter.wrapping_add(1), '.' => {res.push(counter as char); counter},_ => counter });

    res
}
fn main()
{
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_index1()
    {

        assert_eq!(my_first_interpreter("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+."), "ABCDEFGHIJKLMNOPQRSTUVWXYZ");
    }
    #[test]
    fn test_index2() {
        assert_eq!(my_first_interpreter("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+."), "ABCDEFGHIJKLMNOPQRSTUVWXY");
    }

    #[test]
    fn test_index3() {
        assert_eq!(my_first_interpreter("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."), "A");
    }
    #[test]
    fn test_index4()
    {
        assert_eq!(my_first_interpreter("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++."), "AC");
    }
    #[test]
    fn test_index5()
    {
        assert_eq!(my_first_interpreter("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+."), "BC");

    }
}