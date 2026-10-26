
fn bit_cnt(n : i64) -> u32
{
    let mut mut_n  =n as u64;
    let mut one_cnt:u64  = 0;
    while mut_n>0
    {
        one_cnt += mut_n%2;
        mut_n/=2;
    }


    one_cnt as u32

    
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
        assert_eq!(bit_cnt(0),0);
    }
    #[test]
    fn test_sum_two_smallest_numbers2()
    {
        assert_eq!(bit_cnt(7),3);
    }
    #[test]
    fn test_sum_two_smallest_numbers3()
    {
        assert_eq!(bit_cnt(89),4);    
    }
    #[test]
    fn test_sum_two_smallest_numbers4()
    {
        assert_eq!(bit_cnt(i64::MAX),63);
    }
    #[test]
    fn test_sum_two_smallest_numbers5()
    {
        assert_eq!(bit_cnt(31),5);

    }
}