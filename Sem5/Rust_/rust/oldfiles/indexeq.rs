

    
fn index_equals_value(arr: &[i32]) -> i32 {
    arr.into_iter().enumerate().find(|&(i,val)| i as i32 == *val).map_or(-1,|(i,_)| i as i32)
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
        let arr = vec![-3, 0, 1, 3, 10];
        let expected = 3;
        assert_eq!(index_equals_value(&arr), expected);
    }
    #[test]
    fn test_index2() {
        let arr = vec![9, 10, 11, 12, 13, 14];
        let expected = -1;
        assert_eq!(index_equals_value(&arr), expected);
    }

    #[test]
    fn test_index3() {
        let arr = vec![-5, 1, 2, 3, 4, 5, 7, 10, 15];
        let expected = 1;
        assert_eq!(index_equals_value(&arr), expected);
    }
    #[test]
    fn test_index4()
    {
        let arr = vec![0,1, 2, 3];
        let expected = 0;
        assert_eq!(index_equals_value(&arr), expected);
    }
    #[test]
    fn test_index5()
    {
        let arr = vec![1, 1, 11, 12, 13, 14];
        let expected = 1;
        assert_eq!(index_equals_value(&arr), expected);

    }
}