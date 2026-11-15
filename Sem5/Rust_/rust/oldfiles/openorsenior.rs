
fn open_or_senior(data: Vec<(i32, i32)>) -> Vec<String>
{
    let mut output : Vec<String> = vec![];

    data.into_iter().map(|(age,handicap)|
    {
        if(age >= 55 && handicap > 7)
        {
            "Senior"
        }
        else {
            "Open"
        }
        .to_string()
        })
        .collect()
} 

    

fn main()
{
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_open_or_senior()
    {
        assert_eq!(open_or_senior(vec![(45, 12), (55,21), (19, -2), (104, 20)]), vec!["Open", "Senior", "Open", "Senior"]);
    }
    #[test]
    fn test_open_or_senior2()
    {
        assert_eq!(open_or_senior(vec![(3, 12), (55,1), (91, -2), (54, 23)]), vec!["Open", "Open", "Open", "Open"]);
    }
    #[test]
    fn test_open_or_senior3()
    {
        assert_eq!(open_or_senior(vec![(55,1)]), vec!["Open"]); 
    }
    #[test]
    fn test_open_or_senior4()
    {
        assert_eq!(open_or_senior(vec![(56,1)]), vec!["Open"]);
    }
    #[test]
    fn test_open_or_senior5()
    {
        assert_eq!(open_or_senior(vec![(55,8)]), vec!["Senior"]);

    }
}