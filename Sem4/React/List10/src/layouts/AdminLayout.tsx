
import { Outlet, NavLink, Navigate } from 'react-router-dom';
import { useRole } from '../context/RoleContext';
import './AdminLayout.css';

export function AdminLayout() {
  const { role } = useRole();

  if (role !== 'admin') {
    return <Navigate to="/" replace />;
  }

  return (
    <div className="admin-layout">
      <aside className="admin-sidebar">
        <h3>Admin Panel</h3>
        <ul>
          <li><NavLink to="/admin" end>Manage Books</NavLink></li>
          <li><NavLink to="/admin/add">Add Book</NavLink></li>
        </ul>
      </aside>
      <section className="admin-content">
        <Outlet />
      </section>
    </div>
  );
}
