
fn compliment(dna: &str) -> String
{
    let mut new_dna =  String::new();
    for c in dna.chars()
    {
        match c
        {
            'A' => new_dna.push('T'),
            'T' => new_dna.push('A'),
            'G' => new_dna.push('C'),
            'C' => new_dna.push( 'G'),
            _ => new_dna.push(' ')
        }
    };
    new_dna
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
        assert_eq!(compliment("AAA"),"TTT");
    }
    #[test]
    fn test_red_area2()
    {
        assert_eq!(compliment("TTT"),"AAA");

    }
    #[test]
    fn test_red_area3()
    {
        assert_eq!(compliment("CCCC"),"GGGG");

    }
    #[test]
    fn test_red_area4()
    {
        assert_eq!(compliment("GGGG"),"CCCC");

    }
    #[test]
    fn test_red_area5()
    {
        assert_eq!(compliment("ATGC"),"TACG");

    }
}