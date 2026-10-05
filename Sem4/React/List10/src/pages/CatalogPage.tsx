import { useMemo } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { useBooks } from '../context/BooksContext';
import './CatalogPage.css';
import type { Book } from '../types';

export function CatalogPage() {
  const { books } = useBooks();
  const [searchParams, setSearchParams] = useSearchParams();

  const query = searchParams.get('query') || '';
  const sort = searchParams.get('sort') || 'title_asc';

  const filteredAndSortedBooks = useMemo(() => {
    let nextBooks = [...books];

    if (query.trim()) {
      const normalizedQuery = query.toLowerCase();
      nextBooks = nextBooks.filter((book) => {
        return (
          book.title.toLowerCase().includes(normalizedQuery) ||
          book.author.toLowerCase().includes(normalizedQuery)
        );
      });
    }

    nextBooks.sort((firstBook, secondBook) => {
      if (sort === 'title_desc') return secondBook.title.localeCompare(firstBook.title);
      if (sort === 'year_asc') return firstBook.year - secondBook.year;
      if (sort === 'year_desc') return secondBook.year - firstBook.year;
      return firstBook.title.localeCompare(secondBook.title);
    });

    return nextBooks;
  }, [books, query, sort]);

  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const nextSearchParams = new URLSearchParams(searchParams);
    const nextValue = event.target.value;

    if (nextValue) {
      nextSearchParams.set('query', nextValue);
    } else {
      nextSearchParams.delete('query');
    }

    setSearchParams(nextSearchParams);
  };

  const handleSortChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const nextSearchParams = new URLSearchParams(searchParams);
    nextSearchParams.set('sort', event.target.value);
    setSearchParams(nextSearchParams);
  };

  return (
    <div>
      <h1>Book Catalog</h1>
      <div className="filters">
        <input
          type="text"
          placeholder="Search by title or author..."
          value={query}
          onChange={handleSearchChange}
        />
        <select value={sort} onChange={handleSortChange}>
          <option value="title_asc">Title (A-Z)</option>
          <option value="title_desc">Title (Z-A)</option>
          <option value="year_asc">Year (Oldest First)</option>
          <option value="year_desc">Year (Newest First)</option>
        </select>
      </div>

      <div className="book-list">
        {filteredAndSortedBooks.map((book: Book) => (
          <article key={book.id} className="book-card">
            <h3>{book.title}</h3>
            <p>{book.author} ({book.year})</p>
            <Link to={`/books/${book.id}`}>View Details</Link>
          </article>
        ))}
        {filteredAndSortedBooks.length === 0 && <p>No books found.</p>}
      </div>
    </div>
  );
}


