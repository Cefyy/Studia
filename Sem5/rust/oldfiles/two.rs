
fn sum_two_smallest_numbers(numbers: &[u32]) -> u32
{
    let mut sm=u32::MAX;
    let mut sec_sm= u32::MAX;
    for num in numbers
    {
        let numb = *num;
        if numb <= sm
        {
            sec_sm = sm;
            sm = numb;
        }
        if numb > sm && numb <= sec_sm
        {
            sec_sm = numb
        }

    }


    sm+sec_sm
}
fn main()
{
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sum_two_smallest_numbers1()
    {
        assert_eq!(sum_two_smallest_numbers(&[5, 8, 12, 19, 22]),  13, "Incorrect result for [5, 8, 12, 19, 22]");
    }
    #[test]
    fn test_sum_two_smallest_numbers2()
    {
        assert_eq!(sum_two_smallest_numbers(&[15, 28, 4, 2, 43]), 6, "Incorrect result for [15, 28, 4, 2, 43]");

    }
    #[test]
    fn test_sum_two_smallest_numbers3()
    {
        
        assert_eq!(sum_two_smallest_numbers(&[23, 71, 33, 82, 1]), 24, "Incorrect result for [23, 71, 33, 82, 1]");
    }
    #[test]
    fn test_sum_two_smallest_numbers4()
    {
        assert_eq!(sum_two_smallest_numbers(&[52, 76, 14, 12, 4]), 16, "Incorrect result for [52, 76, 14, 12, 4]");;
    }
    #[test]
    fn test_sum_two_smallest_numbers5()
    {
        assert_eq!(sum_two_smallest_numbers(&[1, 1, 5, 5]),  2, "Incorrect result for [1, 1, 5, 5]");

    }
}