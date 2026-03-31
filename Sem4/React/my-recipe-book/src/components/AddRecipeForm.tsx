import { useState } from 'react';
import type { SyntheticEvent } from 'react';
import { useRecipes } from '../RecipeContext';
import './AddRecipeForm.css';

export default function AddRecipeForm() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const { dispatch } = useRecipes();

  const handleSubmit = (e: SyntheticEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!title || !content) return;
    const newRecipe = {
      id: Date.now(),
      title,
      content,
      isFavorite: false,
    };
    dispatch({ type: 'ADD_RECIPE', payload: newRecipe });
    setTitle('');
    setContent('');
  };

  return (
    <form onSubmit={handleSubmit} className="add-recipe-form">
      <input
        type="text"
        placeholder="Recipe Title"
        value={title}
        onChange={e => setTitle(e.target.value)}
      />
      <textarea
        placeholder="Recipe Content"
        value={content}
        onChange={e => setContent(e.target.value)}
      ></textarea>
      <button type="submit">Add Recipe</button>
    </form>
  );
}
