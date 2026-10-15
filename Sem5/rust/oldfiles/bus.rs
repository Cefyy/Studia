
fn bus(bus_stops:&[(i32,i32)]) -> i32
{
    let mut people = 0;
    for (stop) in bus_stops
    {
        people = people + stop.0 - stop.1
    }


    people
}
fn main()
{
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_bus1()
    {
        assert_eq!(bus(&[(3,0),(9,1),(4,8),(12,2),(6,1),(7,8)]), 21);
    }
    #[test]
    fn test_bus2()
    {
        assert_eq!(bus(&[(3,0),(9,1),(4,10),(12,2),(6,1),(7,10)]), 17);

    }
    #[test]
    fn test_bus3()
    {
        assert_eq!(bus(&[(10,0),(3,5),(5,8)]), 5);

    }
    #[test]
    fn test_bus4()
    {
        assert_eq!(bus(&[(0,0),(0,0),(0,0)]), 0);

    }
    #[test]
    fn test_bus5()
    {
        assert_eq!(bus(&[(10,0),(0,0)]), 10);

    }
}