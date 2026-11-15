use std::{ops::{Add, Div, Mul, Sub}};
use std::fmt;
#[derive(PartialEq,Debug,Copy,Clone)]
pub struct ComplexNumber {
    real : f32,
    imag : f32
}

impl ComplexNumber { 
    pub fn new(real: f32,imag: f32) -> Self {
        Self{real: real,imag: imag}
    }

    pub fn modulus(self) -> f32 {
        (self.real*self.real + self.imag*self.imag).sqrt()
    }

    pub fn conjugate(self) -> Self {
        Self::new(self.real, -self.imag)
    }

    pub fn real(self) -> f32 {self.real}
    pub fn imag(self) -> f32 {self.imag}
}

impl Add for ComplexNumber {
    type Output = Self;
    fn add(self,other: Self) -> Self {
        Self {real: self.real + other.real, imag: self.imag + other.imag}
    }
}

impl Sub for ComplexNumber {
    type Output = Self;
    fn sub(self,other: Self) -> Self {
        Self {real: self.real - other.real, imag: self.imag - other.imag}
    } 
}
impl Mul for ComplexNumber {
    type Output = Self;
    fn mul(self,other: Self) -> Self {
        Self{ real: self.real*other.real - self.imag*other.imag, imag: self.imag*other.real + self.real*other.imag}
    }
}
impl Div for ComplexNumber {
    type Output = Self;
    fn div(self,other: Self) -> Self {
        let mianownik: f32 = other.real*other.real + other.imag*other.imag;
        Self{real: (self.real*other.real + self.imag*other.imag)/mianownik,imag: (self.imag*other.real - self.real*other.imag)/mianownik}
    }
}

impl fmt::Display for ComplexNumber {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        if self.imag < 0.0
        {
            write!(f,"{} - {}i",self.real,self.imag.abs())
        }
        else
        {
            write!(f,"{} + {}i",self.real,self.imag)
        }

    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn add_test() {
        assert_eq!(ComplexNumber{real: 10.0,imag: 16.0},ComplexNumber{real: 3.0,imag: 5.0}+ComplexNumber{real: 7.0,imag: 11.0})
    }

    #[test]
    fn sub_test() {
        assert_eq!(ComplexNumber{real: 10.0,imag: 16.0},ComplexNumber{real: 21.0,imag: 8.0}-ComplexNumber{real: 11.0,imag: -8.0})
    }
    #[test]
    fn mult_test()
    {
        assert_eq!(ComplexNumber{real: 29.0,imag: -29.0},ComplexNumber{real: 5.0,imag: 2.0}*ComplexNumber{real: 3.0,imag: -7.0})
    }

    #[test]
    fn div_test() {
        assert_eq!(ComplexNumber{real: 3.0, imag: -7.0}, ComplexNumber{real: 29.0, imag: -29.0} / ComplexNumber{real: 5.0, imag: 2.0});
    }
    #[test]
    fn modulus_test()
    {
        assert_eq!(ComplexNumber{real:3.0,imag: -4.0}.modulus(),5.0)
    }
}