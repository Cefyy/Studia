use std::fs::File;
use std::io::{self, Write};

#[derive(Debug, Clone, Copy)]
pub struct Color {
    red: u8,
    green: u8,
    blue: u8,
}

impl Color {
    pub fn new(r: u8, g: u8, b: u8) -> Self {
        Self { red: r, green: g, blue: b }
    }
}

pub struct Image {
    height: usize,
    width: usize,
    pixels: Vec<Color>,
}

impl Image {
    pub fn new(w: usize, h: usize) -> Self {
        let pixels = vec![Color::new(0, 0, 0); h * w];
        Self { width: w, height: h, pixels }
    }

    pub fn set_pixel(&mut self, x: usize, y: usize, color: Color) {
        if x < self.width && y < self.height {
            let index = y * self.width + x;
            self.pixels[index] = color;
        }
    }

    pub fn write_to_ppm(&self, filename: &str) -> io::Result<()> {
        let mut file = File::create(filename)?;

        write!(file, "P6\n{} {}\n255\n", self.width, self.height)?;
        
        for pixel in &self.pixels {
            file.write_all(&[pixel.red, pixel.green, pixel.blue])?;
        }

        Ok(())
    }
}