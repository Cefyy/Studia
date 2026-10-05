
import { useParams, Link } from 'react-router-dom';
import { useBooks } from '../context/BooksContext';

export function BookDetailsPage() {
  const { bookId } = useParams<{ bookId: string }>();
  const { books } = useBooks();

  const book = books.find(b => b.id === bookId);

  if (!book) {
    return (
      <div>
        <p>Book not found.</p>
        <Link to="/catalog">Go back to catalog</Link>
      </div>
    );
  }

  return (
    <div>
      <h1>{book.title}</h1>
      <p><strong>Author:</strong> {book.author}</p>
      <p><strong>Year:</strong> {book.year}</p>
      <div style={{ marginTop: '1rem', marginBottom: '1rem' }}>
        <strong>Description:</strong>
        <p>{book.description}</p>
      </div>
      <Link to="/catalog">Back to Catalog</Link>
    </div>
  );
}
