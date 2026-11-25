fn largest_difference(data: &[i32]) -> usize {
    
    data.iter()
    .enumerate()
    .filter_map(|(i,&val)| {
        data[i+1..]
            .iter()
            .rposition(|&x|x >= val)
            .map(|offset| offset+1)
    }).max().unwrap_or(0)
}

fn main()
{
    
}

#[cfg(test)]
mod tests {
    use super::*;
    const ERR_MSG: &str = "\nYour result (left) did not match the expected output (right)";
    
    fn dotest(data: &[i32], expected: usize) {
        assert_eq!(largest_difference(data), expected, "{ERR_MSG} with data = {data:?}")
    }
    #[test]
    fn test_1()
    {

        dotest(&[9, 4, 1, 10, 3, 4, 0, -1, -2], 4);
    }
    #[test]
    fn test_2() {
        dotest(&[3, 2, 1], 0);
    }

    #[test]
    fn test_3() {
         dotest(&[1, 2, 3], 2);
    }
    #[test]
    fn test_4()
    {
        dotest(&[9, 4, 1, 2, 3, 0, -1, -2], 2);
    }
    #[test]
    fn test_5()
    {
        dotest(&[9, 4, 1, 2, 3, 4, 0, -1, -2], 4);

    }
}