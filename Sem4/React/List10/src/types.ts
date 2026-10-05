export interface Book {
  id: string;
  title: string;
  author: string;
  year: number;
  description: string;
}

export type Role = 'guest' | 'admin';
