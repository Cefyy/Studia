
import { Link } from 'react-router-dom';
import { useBooks } from '../context/BooksContext';
import './AdminManagePage.css';

export function AdminManagePage() {
  const { books, deleteBook } = useBooks();

  return (
    <div>
      <h2>Manage Books</h2>
      <table className="admin-table">
        <thead>
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {books.map(book => (
            <tr key={book.id}>
              <td>{book.title}</td>
              <td>{book.author}</td>
              <td>
                <Link to={`/admin/edit/${book.id}`} className="edit-link">Edit</Link>
                <button onClick={() => deleteBook(book.id)} className="delete-btn">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
