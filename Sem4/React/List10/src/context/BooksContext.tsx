/* eslint-disable react-refresh/only-export-components */
import { createContext, useContext, useState } from 'react';
import type { ReactNode } from 'react';
import type { Book } from '../types';
import { initialBooks } from '../data/books';

interface BooksContextType {
  books: Book[];
  addBook: (book: Omit<Book, 'id'>) => void;
  updateBook: (id: string, updatedBook: Omit<Book, 'id'>) => void;
  deleteBook: (id: string) => void;
}

const BooksContext = createContext<BooksContextType | undefined>(undefined);

export function BooksProvider({ children }: { children: ReactNode }) {
  const [books, setBooks] = useState<Book[]>(initialBooks);

  const addBook = (book: Omit<Book, 'id'>) => {
    const newBook: Book = { ...book, id: Date.now().toString() };
    setBooks(prev => [...prev, newBook]);
  };

  const updateBook = (id: string, updatedBook: Omit<Book, 'id'>) => {
    setBooks(prev => prev.map(b => b.id === id ? { ...updatedBook, id } : b));
  };

  const deleteBook = (id: string) => {
    setBooks(prev => prev.filter(b => b.id !== id));
  };

  return (
    <BooksContext.Provider value={{ books, addBook, updateBook, deleteBook }}>
      {children}
    </BooksContext.Provider>
  );
}

export function useBooks() {
  const context = useContext(BooksContext);
  if (!context) throw new Error('useBooks must be used within BooksProvider');
  return context;
}
