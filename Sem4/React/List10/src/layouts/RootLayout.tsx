
import { Outlet, NavLink } from 'react-router-dom';
import { useRole } from '../context/RoleContext';
import './RootLayout.css';

export function RootLayout() {
  const { role, setRole } = useRole();

  return (
    <div className="layout">
      <header className="header">
        <nav>
          <ul>
            <li><NavLink to="/">Home</NavLink></li>
            <li><NavLink to="/catalog">Catalog</NavLink></li>
            {role === 'admin' && <li><NavLink to="/admin">Admin</NavLink></li>}
          </ul>
        </nav>
        <div className="role-switcher">
          <span>Role: </span>
          <select value={role} onChange={(event) => setRole(event.target.value === 'admin' ? 'admin' : 'guest')}>
            <option value="guest">Guest</option>
            <option value="admin">Admin</option>
          </select>
        </div>
      </header>
      <main className="main-content">
        <Outlet />
      </main>
      <footer className="footer">
        &copy; 2026 Book Library
      </footer>
    </div>
  );
}
