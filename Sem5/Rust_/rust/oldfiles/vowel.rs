
fn vowel_cnt(string: &str) -> usize
{
    let mut cnt=0;
    for c in string.chars()
    {
        match c
        {
            |'a' | 'e' | 'i' | 'o' | 'u' => cnt+=1,
            _ => continue
        }
    };
    cnt
}
fn main()
{
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_red_area1()
    {
        assert_eq!(vowel_cnt("ab eui"),4);
    }
    #[test]
    fn test_red_area2()
    {
        assert_eq!(vowel_cnt("bcjhf"),0);

    }
    #[test]
    fn test_red_area3()
    {
        assert_eq!(vowel_cnt(" "),0);

    }
    #[test]
    fn test_red_area4()
    {
        assert_eq!(vowel_cnt("bbbbb u"),1);

    }
    #[test]
    fn test_red_area5()
    {
        assert_eq!(vowel_cnt("yyyyyy"),0);

    }
}