use crate::Order::Unordered;

#[derive(Debug, PartialEq, Clone, Copy)]
pub enum Order {
    Unordered,
    Increasing,
    NotDecreasing,
    Decreasing,
    NotIncreasing,
    Constant,
}

    
fn sequence_classifier(arr: &[i32]) -> Order {
    let (up,down,flat) = arr.windows(2).fold((false,false,false), |(up,down,flat),win| 
    (
        up || win[0] < win[1], down || win[0] > win[1],flat || win[0]==win[1]
    ),
);

    match(up,down,flat) {
        (true,true,_) => Order::Unordered,
        (true,false,false) => Order::Increasing,
        (true,false,true) => Order::NotDecreasing,
        (false,true,false) => Order::Decreasing,
        (false,true,true) => Order::NotIncreasing,
        (false,false,_) => Order::Constant,
    }
}
fn main()
{
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sequence()
    {
        assert_eq!(sequence_classifier(&[3,5,8,1,14,3]), Order::Unordered);
    }
    #[test]
    fn test_sequence2()
    {
        assert_eq!(sequence_classifier(&[3,5,8,9,14,23]), Order::Increasing);
    }
    #[test]
    fn test_sequence3()
    {
        assert_eq!(sequence_classifier(&[3,5,5,8,8,14]), Order::NotDecreasing);
    }
    #[test]
    fn test_sequence4()
    {
        assert_eq!(sequence_classifier(&[3,3,3,3,3,3]), Order::Constant);
    }
    #[test]
    fn test_sequence5()
    {
        assert_eq!(sequence_classifier(&[14,9,8,7,5,1]), Order::Decreasing);

    }
    #[test]
    fn test_sequence6()
    {
        assert_eq!(sequence_classifier(&[14,14,8,7,5,1]), Order::NotIncreasing);

    }
}