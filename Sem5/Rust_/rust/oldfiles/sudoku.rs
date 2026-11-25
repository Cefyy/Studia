struct Sudoku{
    data: Vec<Vec<u32>>,
}


impl Sudoku{
    fn is_valid(&self) -> bool {
        let n = self.data.len();
        let k = (n as f64).sqrt() as usize;
        if self.data.iter().any(|row| row.len() != n) {
        return false;
        }
      self.data
        .iter()
        .enumerate()
        .flat_map(|(r,row)| {
            row.iter()
                .enumerate()
                .map(move |(c,&val)| (r,c,val))
        }).try_fold(
            (vec![false; n * n], vec![false; n * n], vec![false; n * n]),
             |(mut rows, mut cols, mut boxes), (r, c, val)|
            {
                if val == 0 || val > n as u32
                {
                    return None;
                }
                let v =(val-1) as usize;
                let b= (r/k)*k + (c/k);
                let r_idx = r*n + v;
                let c_idx = c*n + v;
                let b_idx = b*n + v;
                if rows[r_idx] || cols[c_idx] || boxes[b_idx]{
                    return None;
                }

                rows[r_idx]=true;
                cols[c_idx]=true;
                boxes[b_idx]=true;
                Some((rows,cols,boxes))
            },).is_some()

    }
}


#[cfg(test)]
mod tests {
    use super::*;
    

    #[test]
    fn test_1()
    {
        
        let good_sudoku_2 = Sudoku{
            data: vec![
                    vec![1, 4,  2, 3],
                    vec![3, 2,  4, 1],
            
                    vec![4, 1,  3, 2],
                    vec![2, 3,  1, 4],
                ]
        };
        assert!(good_sudoku_2.is_valid());
    }
    #[test]
    fn test_2() {
        let good_sudoku_1 = Sudoku{
        data: vec![
                vec![7,8,4, 1,5,9, 3,2,6],
                vec![5,3,9, 6,7,2, 8,4,1],
                vec![6,1,2, 4,3,8, 7,5,9],

                vec![9,2,8, 7,1,5, 4,6,3],
                vec![3,5,7, 8,4,6, 1,9,2],
                vec![4,6,1, 9,2,3, 5,8,7],
                
                vec![8,7,6, 3,9,4, 2,1,5],
                vec![2,4,3, 5,6,1, 9,7,8],
                vec![1,9,5, 2,8,7, 6,3,4]
            ]
    };
    assert!(good_sudoku_1.is_valid());
    }

    #[test]
    fn test_3() {
        let bad_sudoku_1 = Sudoku{ data: vec![
                vec![1,2,3, 4,5,6, 7,8,9],
                vec![1,2,3, 4,5,6, 7,8,9],
                vec![1,2,3, 4,5,6, 7,8,9],

                vec![1,2,3, 4,5,6, 7,8,9],
                vec![1,2,3, 4,5,6, 7,8,9],
                vec![1,2,3, 4,5,6, 7,8,9],
                
                vec![1,2,3, 4,5,6, 7,8,9],
                vec![1,2,3, 4,5,6, 7,8,9],
                vec![1,2,3, 4,5,6, 7,8,9],
            ]
    };
         assert!(!bad_sudoku_1.is_valid());
    }
    #[test]
    fn test_4()
    {
         let bad_sudoku_2 = Sudoku{data: vec![
                vec![1,2,3,4,5],
                vec![1,2,3,4],
                vec![1,2,3,4],
                vec![1],
            ]
    };
        assert!(!bad_sudoku_2.is_valid());
    }
    #[test]
    fn test_5()
    {
        let bad_sudoku_2 = Sudoku{data: vec![
    vec![1, 2, 3, 4],
    vec![3, 4, 1, 2],
    vec![2, 1, 4, 3],
    vec![4, 3],
]
    };
        assert!(!bad_sudoku_2.is_valid());

    }
}