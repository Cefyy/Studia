import { useState } from 'react';
import { Navigate, useNavigate, useParams } from 'react-router-dom';
import { useBooks } from '../context/BooksContext';
import { useRole } from '../context/RoleContext';
import './AdminFormPage.css';

export function AdminFormPage() {
  const { role } = useRole();
  const { bookId } = useParams<{ bookId: string }>();
  const { books, addBook, updateBook } = useBooks();
  const navigate = useNavigate();

  const isEdit = Boolean(bookId);
  const currentBook = isEdit ? books.find((book) => book.id === bookId) : undefined;

  if (role !== 'admin') {
    return <Navigate to="/" replace />;
  }

  if (isEdit && !currentBook) {
    return (
      <div>
        <h2>Book not found</h2>
        <button type="button" onClick={() => navigate('/admin')}>
          Back to admin panel
        </button>
      </div>
    );
  }

  return (
    <BookForm
      key={bookId ?? 'new'}
      initialBook={currentBook}
      onSave={(nextBook) => {
        if (isEdit && bookId) {
          updateBook(bookId, nextBook);
        } else {
          addBook(nextBook);
        }

        navigate('/admin');
      }}
      onCancel={() => navigate('/admin')}
      isEdit={isEdit}
    />
  );
}

interface BookFormProps {
  initialBook?: {
    title: string;
    author: string;
    year: number;
    description: string;
  };
  isEdit: boolean;
  onSave: (book: {
    title: string;
    author: string;
    year: number;
    description: string;
  }) => void;
  onCancel: () => void;
}

function BookForm({ initialBook, isEdit, onSave, onCancel }: BookFormProps) {
  const [title, setTitle] = useState(initialBook?.title ?? '');
  const [author, setAuthor] = useState(initialBook?.author ?? '');
  const [year, setYear] = useState(initialBook ? String(initialBook.year) : '');
  const [description, setDescription] = useState(initialBook?.description ?? '');

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();

    onSave({
      title,
      author,
      year: Number(year),
      description,
    });
  };

  return (
    <div className="admin-form-container">
      <h2>{isEdit ? 'Edit Book' : 'Add New Book'}</h2>
      <form onSubmit={handleSubmit} className="admin-form">
        <label>
          Title:
          <input required type="text" value={title} onChange={(event) => setTitle(event.target.value)} />
        </label>
        <label>
          Author:
          <input required type="text" value={author} onChange={(event) => setAuthor(event.target.value)} />
        </label>
        <label>
          Year:
          <input required type="number" value={year} onChange={(event) => setYear(event.target.value)} />
        </label>
        <label>
          Description:
          <textarea required value={description} onChange={(event) => setDescription(event.target.value)} />
        </label>
        <div className="form-actions">
          <button type="submit">Save</button>
          <button type="button" onClick={onCancel}>
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
}


