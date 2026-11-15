fn count(u: u32) -> u32
{
    if u == 0 as u32
    {
        return 0 as u32
    }
    let res : u32 = (u-1)*2;
    res
}
fn main()
{

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_count_beads1()
    {
        assert_eq!(count(5),8);
    }
    #[test]
    fn test_count_beads2()
    {
        assert_eq!(count(0),0);

    }
    #[test]
    fn test_count_beads3()
    {
        assert_eq!(count(325),648);

    }
    #[test]
    fn test_count_beads4()
    {
        assert_eq!(count(43254355),86508708);

    }
    #[test]
    fn test_count_beads5()
    {
        assert_eq!(count(10),18);

    }
}