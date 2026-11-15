mod complex;
mod image;

use complex::ComplexNumber;
use image::{Image, Color};

fn draw_mandelbrot_set(
    width: usize, 
    height: usize, 
    id: usize, 
    x_min: f32, 
    x_max: f32, 
    y_min: f32, 
    y_max: f32
) -> std::io::Result<()> {
    
    let mut image = Image::new(width, height);
    let max_iter = 100;

    for y in 0..height {
        for x in 0..width {
            
            
            let cx = x_min + (x as f32 / width as f32) * (x_max - x_min);
            let cy = y_min + (y as f32 / height as f32) * (y_max - y_min);

            let c = ComplexNumber::new(cx, cy);
            let mut z = ComplexNumber::new(0.0, 0.0);
            
            let mut iter = 0;

            while z.modulus() <= 2.0 && iter < max_iter {
                z = z * z + c;
                iter += 1;
            }
            
            let color = if iter == max_iter {
                Color::new(0, 0, 0)
            } else {

                let r = (iter as f32 * 9.0) as u8;
                let g = (iter as f32 * 3.0) as u8;
                let b = (iter as f32 * 15.0) as u8;
                Color::new(r, g, b)
            };
            
            image.set_pixel(x, y, color);
        }
    }
    
    let filename = format!("mandelbrot{}.ppm", id);
    image.write_to_ppm(&filename)?;

    Ok(())
}

fn main() {
    println!("Generowanie");
    
    draw_mandelbrot_set(300, 300, 1, -2.0, 1.0, -1.5, 1.5).unwrap();


    draw_mandelbrot_set(800, 800, 2, -0.75, -0.73, 0.1, 0.12).unwrap();

   
    draw_mandelbrot_set(1200, 1200, 3, -1.26, -1.24, -0.04, -0.02).unwrap();

    
    draw_mandelbrot_set(1920, 1080, 4, -2.5, 1.0, -1.0, 1.0).unwrap();
    
    println!("Gotowe");
}