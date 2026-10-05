
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { RoleProvider } from './context/RoleContext';
import { BooksProvider } from './context/BooksContext';

import { RootLayout } from './layouts/RootLayout';
import { AdminLayout } from './layouts/AdminLayout';

import { HomePage } from './pages/HomePage';
import { CatalogPage } from './pages/CatalogPage';
import { BookDetailsPage } from './pages/BookDetailsPage';
import { AdminManagePage } from './pages/AdminManagePage';
import { AdminFormPage } from './pages/AdminFormPage';

export default function App() {
  return (
    <RoleProvider>
      <BooksProvider>
        <BrowserRouter>
          <Routes>
            <Route path='/' element={<RootLayout />}>
              <Route index element={<HomePage />} />
              <Route path='catalog' element={<CatalogPage />} />
              <Route path='books/:bookId' element={<BookDetailsPage />} />
              
              <Route path='admin' element={<AdminLayout />}>
                <Route index element={<AdminManagePage />} />
                <Route path='add' element={<AdminFormPage />} />
                <Route path='edit/:bookId' element={<AdminFormPage />} />
              </Route>
              
              <Route path='*' element={<Navigate to='/' replace />} />
            </Route>
          </Routes>
        </BrowserRouter>
      </BooksProvider>
    </RoleProvider>
  );
}
